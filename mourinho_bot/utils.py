"""
Utility functions used in the package
"""
import random

import mourinho_bot.quotes


def get_random_quote(
        quotes: list = mourinho_bot.quotes.quotes
) -> str:
    """
    :rtype: str
    :param
        quotes: list of quotes from which a random quote is to be selected
    :return:
        A randomly selected quote
    """
    return random.choice(quotes)
