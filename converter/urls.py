from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='hello-world'),
]
