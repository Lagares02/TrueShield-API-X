import asyncio
from twikit import Client
from configparser import ConfigParser

# Cargar credenciales de inicio de sesión desde config.ini
config = ConfigParser()
config.read('config.ini')
USERNAME = config['X']['username']
EMAIL = config['X']['email']
PASSWORD = config['X']['password']

client = Client('en-US')

async def search_tweets(Keywords: list):
    
    await client.login(
        auth_info_1=USERNAME, 
        auth_info_2=EMAIL, 
        password=PASSWORD
    )

    tweets_found = []
    
    # Realizar búsquedas para cada palabra clave
    for keyword in Keywords:
        print(f"Buscando tweets con la palabra clave: {keyword}")
        tweets = await client.search_tweet(keyword, 'Latest')
        
        for tweet in tweets:
            tweet_data = {
                "Id": tweet.id,
                "DatePub": str(tweet.created_at),
                "UserProfile": tweet.user.screen_name,
                "NameProfile": tweet.user.name,
                "CantLike": tweet.favorite_count,
                "CantRetwits": tweet.retweet_count,
                "CantComents": tweet.reply_count,
                "TrueLevel": 0.60,
                "Type_item": "x"
            }
            tweets_found.append(tweet_data)

    return tweets_found