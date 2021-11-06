import os

import praw
import re
import time
import logging

import mourinho_bot.constants as constants
from mourinho_bot.utils import get_random_quote

logger = logging.getLogger("app")


class CredentialsNotConfiguredError(Exception):
    """
    Raised when credentials are not configured in the environment
    """
    pass


def run():
    try:
        username = os.environ["praw_username"]
        password = os.environ["praw_password"]
        client_id = os.environ["praw_client_id"]
        client_secret = os.environ["praw_client_secret"]

    except KeyError:
        print("Please configure your client id and secret as environment variables in the following format:")
        print(
            "praw_client_id=<client_id>\npraw_client_secret=<client_secret>\npraw_username=<username>\npraw_password=<password>")
        logger.error("Failed connecting to Reddit")
        raise CredentialsNotConfiguredError("Failed connecting to Reddit")

    logger.debug("Using user u/{}".format(username))
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent="Mourinho Bot 0.1"
    )

    logger.debug("Using subreddit: [{}]".format(constants.subreddit))
    subreddit = reddit.subreddit(constants.subreddit)

    logger.info("Starting stream")
    # continuously streams comments and posts until manually broken
    for comment in subreddit.stream.comments():
        if re.search(constants.keyword, comment.body, re.IGNORECASE):
            reply = get_random_quote()

            comment.reply(reply)
            logger.info("Replied to comment [{}] by u/{}".format(comment.id, comment.author.name))
            # reddit APIs allow 1 request for every 2 seconds
            time.sleep(3)
