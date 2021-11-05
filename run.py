import logging
from mourinho_bot.bot import run

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    print("Running bot.. Press Ctrl+c to exit")
    try:
        run()
    except KeyboardInterrupt:
        print("Stopping bot and terminating..")