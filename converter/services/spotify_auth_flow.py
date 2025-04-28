import requests
import os
from dotenv import load_dotenv
import base64
from urllib.parse import urlencode
load_dotenv()

id = os.getenv("SPOTIFY_CLIENT_ID")
secret = os.getenv("SPOTIFY_CLIENT_SECRET")


def obtain_auth_code():
    #one-time use function to obtain code from user authentication
    id = os.getenv("SPOTIFY_CLIENT_ID")

    login_url = "https://accounts.spotify.com/authorize?"

    params = {
        'client_id': id,
        'response_type': 'code',
        'redirect_uri': 'http://127.0.0.1:3000'
    }
    
    login_url += urlencode(params)
    print(login_url)



def exchange_code_for_token():
    id = os.getenv("SPOTIFY_CLIENT_ID")
    secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    code = 'AQCteVEiUOCwcbCFzyCvCiUej4APqCvb_x70WXWssweei_O5bj-qkZG7aabsvGT1W6DOCBXCBhQS9CVAE829RgS6gg6fPqg96H50zg7mYYEUUc3oQ-R2uRm5YdEat5jYsMFwSKNtEnIy9Xn_vi_GpYgEg99nbeejiw'

    url = ("https://accounts.spotify.com/api/token")
    creds = f"{id}:{secret}"
    creds_64 = base64.b64encode(creds.encode()).decode()

    headers = {
        "Authorization": f"Basic {creds_64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:3000'
    }

    r = requests.post(url, data=params, headers=headers)
    print(r.text)


def get_access_token():
    token = os.getenv('SPOTIFY_REFRESH_TOKEN')

    url = "https://accounts.spotify.com/api/token"

    encoded = f"{id}:{secret}"
    encoded = base64.b64encode(encoded.encode()).decode()

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': token
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f"Basic {encoded}"
    }

    r = requests.post(url, data=data, headers=headers)
    data = r.json()
    return data['access_token']


def get_private_playlist_names():
#returns array of all playlists

    access_token = get_access_token()
    url = 'https://api.spotify.com/v1/me/playlists'

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    r = requests.get(url, headers=headers) 
    data = r.json()

    playlists = []

    for item in data['items']:
        playlists.append(item['name'])

    return playlists



if __name__ == "__main__":
   #obtain_auth_code()
   #exchange_code_for_token()
   #get_access_token()
   get_private_playlist_names()