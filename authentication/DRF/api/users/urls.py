from django.urls import path
from django.conf.urls import include


'''
Endpoint List
-------------
GET   /users/              => list
POST  /users/              => create
GET   /users/me/           => retrieve
PATCH /users/set_password/ => partial_update
PATCH /users/set_username/ => partial_update 
'''
urlpatterns = [
    path('', include('djoser.urls')),
]
