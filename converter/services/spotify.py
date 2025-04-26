import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_spotify_access_token():
    id = os.getenv("SPOTIFY_CLIENT_ID")
    secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    print(id, secret)
    data = {
            "grant_type": "client_credentials",
            "client_id": id,
            "client_secret": secret
        }
    
    r = requests.post("https://accounts.spotify.com/api/token",
                      data = data)
    
    if r.status_code != 200:
        print(f"Error: {r.status_code}")

    print(r.text['access_token'])

    return (r.text['access_token'])


if __name__ == "__main__":
    get_spotify_access_token()