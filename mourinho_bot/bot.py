import praw
import re
import time
import logging

import mourinho_bot.constants as constants
from mourinho_bot.utils import get_random_quote

logger = logging.getLogger("app")


def run():
    logger.debug("Using config: [{}]".format(constants.bot_name))
    reddit = praw.Reddit(constants.bot_name)

    logger.debug("Using subreddit: [{}]".format(constants.subreddit))
    subreddit = reddit.subreddit(constants.subreddit)

    logger.info("Starting stream")
    # continuously streams comments and posts until manually broken
    for comment in subreddit.stream.comments():
        if re.search(constants.keyword, comment.body, re.IGNORECASE):
            reply = get_random_quote()
            comment.reply(reply)
            logger.info("Replied to comment [{}]".format(comment.id))
            # reddit APIs allow 1 request for every 2 seconds
            time.sleep(3)
