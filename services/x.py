import asyncio
from twikit import Client
from configparser import ConfigParser
from datetime import datetime

# Cargar credenciales de inicio de sesión desde config.ini
config = ConfigParser()
config.read('config.ini')
USERNAME = config['X']['username']
EMAIL = config['X']['email']
PASSWORD = config['X']['password']

client = Client('en-US')

async def search_tweets(Keywords: list):
    # Convertir todas las palabras clave a minúsculas
    keywords = [keyword.lower() for keyword in Keywords]

    await client.login(
        auth_info_1=USERNAME, 
        auth_info_2=EMAIL, 
        password=PASSWORD
    )

    tweets_found = []

    # Realizar búsqueda utilizando las palabras clave combinadas
    query = " OR ".join(keywords)
    print(f"Buscando tweets con las palabras clave: {query}")

    # Buscar tweets con todas las palabras clave combinadas
    tweets = await client.search_tweet(query, 'Latest')

    for tweet in tweets:
        # Contar el número de coincidencias de palabras clave en el texto del tweet
        tweet_text = (tweet.text or "").lower()
        matches = sum(1 for keyword in keywords if keyword in tweet_text)

        # Calcular el nivel de contexto basado en coincidencias
        ContextLevel = round(float(matches / len(keywords)), 2) if matches > 0 else 0.0

        # Solo añadir tweets que tengan al menos una coincidencia
        if matches >= 1:
            tweet_data = {
                "Id": tweet.id,
                "DatePub": datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d'),
                "UserProfile": tweet.user.screen_name,
                "NameProfile": tweet.user.name,
                "TextPub": tweet.text,
                "CantLike": tweet.favorite_count,
                "CantRetwits": tweet.retweet_count,
                "CantComents": tweet.reply_count,
                "TrueLevel": 0.60,
                "ContextLevel": ContextLevel,
                "Type_item": "x"
            }
            tweets_found.append(tweet_data)

    # Ordenar los resultados por el número de coincidencias
    tweets_found = sorted(tweets_found, key=lambda x: x["ContextLevel"], reverse=True)

    return tweets_found