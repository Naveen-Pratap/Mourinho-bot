# Reddit Chatbot
Standard Reddit chatbot which replies to comments containing a keyword in your favourite subreddit. Simply modify the parameters mentioned in the setup to create your own custom reddit chatbot to add some life to your subreddit!

## Setup and usage

1. Clone this repo to your local machine.
2. Add the following values to your environment
      ```sh
      praw_client_id=<client_id>
      praw_client_secret=<client_secret>
      praw_username=<reddit_username>
      praw_password=<reddit_password>
      ```
   You can obtain a client id and secret by registering a script app at https://www.reddit.com/prefs/apps/.
    
3. Add your list of possible replies to `quotes.txt`. Take care to save each new reply in a new line. The bot will choose a random reply from the ones supplied.
4. Add the subreddit, the keyword to trigger your bot and the user agent to `reddit_bot/constants.py`. Make sure to read about [reddit etiquette](https://www.reddit.com/wiki/bottiquette) while choosing these values.
5. Install requirements with 
   ```sh
      pip install -r requirements.txt
   ```
6. Start your bot with
   ```sh
      python run.py
   ```
   The bot keeps reading from reddit until terminated.
7. Whenever a comment that matches the keyword is posted, the bot replies with a random quote chosen from `quotes.txt`. The profile of the user whose username and password are supplied(and for whom the reddit app was created) is used for replying.

