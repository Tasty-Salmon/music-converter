from ytmusicapi import YTMusic, OAuthCredentials
import os
from dotenv import load_dotenv


load_dotenv()

id = os.getenv('YT_CLIENT_ID')
secret = os.getenv('YT_CLIENT_SECRET')
ytmusic = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=id,client_secret=secret))

