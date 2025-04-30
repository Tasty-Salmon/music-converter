from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

#.\.venv\Scripts\Activate.ps1

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, DRF is working!"})
