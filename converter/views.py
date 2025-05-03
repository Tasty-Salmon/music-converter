from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.spotify import get_all_songs

#.\.venv\Scripts\Activate.ps1
#{'playlist': {'id': 123, 'tracks': {'song name': 'song id'}}}

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, DRF is working!"})
    

class FetchSong(APIView):
    def _allowed_methods(self):
        return ['POST', 'GET']
    
    def get(self, request):
        playlists = get_all_songs()
        return Response(playlists)