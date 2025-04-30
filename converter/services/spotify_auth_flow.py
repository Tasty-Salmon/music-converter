import requests
import os
from dotenv import load_dotenv
import base64
from urllib.parse import urlencode
from typing import Dict, List
load_dotenv()

id = os.getenv("SPOTIFY_CLIENT_ID")
secret = os.getenv("SPOTIFY_CLIENT_SECRET")



#reusable helper functions

def get_private_playlist_ids(access_token):
#returns array of all playlists

    url = 'https://api.spotify.com/v1/me/playlists'

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    r = requests.get(url, headers=headers) 
    data = r.json()

    playlists = {}

    for item in data['items']:
        name = item['name']
        id = item['id']
        playlists[name] = {
            'id': id,
            'tracks': []
            }

    return playlists


def get_all_songs():
    #returns nested dictionary of songs.
    #{'playlist': {'id': 123, 'tracks': ['abc','xyz']}}

    access_token = get_access_token()
    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    playlists = get_private_playlist_ids(access_token)

    for name, data in playlists.items():
        id = data['id']
        url = f'https://api.spotify.com/v1/playlists/{id}/tracks'

        r = requests.get(url, headers=headers)
        r = r.json()
        
        for item in r['items']:
            song_name = item['track']['name']
            playlists[name]['tracks'].append(song_name)
    print(playlists)
    return playlists


#reusable function exchanging refresh token for access token
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

if __name__ == "__main__":
   #obtain_auth_code()
   #exchange_code_for_token()
   
   get_all_songs()

#one-time use functions to obtain refresh token in spotify authorization code flow

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


