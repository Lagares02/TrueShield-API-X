import asyncio
from twikit import Client
from configparser import ConfigParser
from datetime import datetime
import random

# Cargar credenciales de inicio de sesión desde config.ini
config = ConfigParser()
config.read('config.ini')
USERNAME = config['X']['username']
EMAIL = config['X']['email']
PASSWORD = config['X']['password']

client = Client(
   user_agent='Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion',
   language='en-US',
)

async def search_tweets(Keywords: list):
    # Convertir todas las palabras clave a minúsculas
    keywords = [keyword.lower() for keyword in Keywords]

    await client.login(
        auth_info_1=USERNAME, 
        auth_info_2=EMAIL, 
        password=PASSWORD
    )

    results = []

    # Realizar búsqueda utilizando las palabras clave combinadas
    query = " OR ".join(keywords)
    print(f"Buscando tweets con las palabras clave: {query}")
    print(f"keywords: {len(keywords)}")

    # Buscar tweets con todas las palabras clave combinadas
    tweets = await client.search_tweet(query, product = 'Top')#, 'Latest')

    for tweet in tweets:
        # Contar el número de coincidencias de palabras clave en el texto del tweet
        tweet_text = (tweet.text or "").lower()
        matches = sum(1 for keyword in keywords if keyword in tweet_text)

        # Calcular el nivel de contexto basado en coincidencias
        #ContextLevel = round(float(matches / len(keywords)), 2) if matches > 0 else 0.0
        
        if matches >= 1:
            Domain = round(float(matches / len(keywords)), 2)
        else:
            Domain = 0.0

        # Solo añadir tweets que tengan al menos dos coincidencia
        if matches >= 2:
            tweet_data = {
                "Id": tweet.id,
                "DatePub": datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d'),
                "UserProfile": tweet.user.screen_name,
                "NameProfile": tweet.user.name,
                "TextPub": tweet.text,
                "CantLike": tweet.favorite_count,
                "CantRetwits": tweet.retweet_count,
                "CantComents": tweet.reply_count,
                "Confidence": 0.60,
                "matches": matches,
                "Domain": Domain,
                "Inference": random.choice(["affirmation", "assumption", "denial"]),
                "Type_item": "X"
            }
            results.append(tweet_data)

    # Ordenar los resultados por el número de coincidencias
    results = sorted(results, key=lambda x: x.get("matches", 0), reverse=True)
    
    return results