from unittest import TestCase

from reddit_bot.bot import get_random_quote


class TestGetRandom(TestCase):
    def test_get_random_quote(self):
        quotes = [
            "hello",
            "foo",
            "bar"
        ]

        quote = get_random_quote(quotes)

        assert quote in quotes
        assert isinstance(quote, str)
