"""
Entry script to start the bot
"""

import logging
import sys
from mourinho_bot.bot import run

# set logging config here
logging.basicConfig(format='%(levelname)s - %(message)s')
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Running bot.. Press Ctrl+c to exit")
    try:
        run()
    except KeyboardInterrupt:
        print("Stopping bot and terminating..")
        sys.exit()
