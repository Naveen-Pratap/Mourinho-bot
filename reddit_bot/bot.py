"""
Functions used by the bot
"""
import os
import random
import re
import time
import logging
import praw

import reddit_bot.constants as constants

logger = logging.getLogger("app")


class CredentialsNotConfiguredError(Exception):
    """
    Raised when credentials are not configured in the environment
    """
    pass


def run():
    """
    Runs the bot and continuously streams comments from Reddit

    Uses configured environment variables to find credentials.
    """
    try:
        username = os.environ["praw_username"]
        password = os.environ["praw_password"]
        client_id = os.environ["praw_client_id"]
        client_secret = os.environ["praw_client_secret"]

    except KeyError:
        print(
            "Please configure your client id and secret as environment variables in the following "
            "format:"
        )
        print(
            "praw_client_id=<client_id>\npraw_client_secret=<client_secret>\npraw_username"
            "=<username>\npraw_password"
            "=<password>"
        )
        logger.error("Failed connecting to Reddit")
        raise CredentialsNotConfiguredError("Failed connecting to Reddit")

    logger.info("Using user u/{}".format(username))
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent=constants.USER_AGENT
    )

    logger.info("Using subreddit: [{}]".format(constants.SUBREDDIT))
    subreddit = reddit.subreddit(constants.SUBREDDIT)

    logger.info("Loading quotes..")
    quotes = get_quotes()

    logger.info("Starting stream")
    # continuously streams comments and posts until manually broken
    for comment in subreddit.stream.comments():
        if re.search(constants.KEYWORD, comment.body, re.IGNORECASE):
            reply = get_random_quote(quotes)

            comment.reply(reply)
            logger.info("Replied to comment [{}] by u/{}".format(comment.id, comment.author.name))
            # reddit APIs allow 1 request for every 2 seconds
            time.sleep(3)


def get_quotes() -> list:
    """
    Fetches quotes from quotes.txt
    :return: List of quotes
    """
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    # Remove empty spaces from quotes
    quotes = [q for q in quotes if q]
    return quotes


def get_random_quote(
        quotes: list = []
) -> str:
    """
    :rtype: str
    :param
        quotes: list of quotes from which a random quote is to be selected
    :return:
        A randomly selected quote
    """
    return random.choice(quotes)
