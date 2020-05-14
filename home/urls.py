from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('analyze/',views.analyze),
    path('about/',views.about),
    path('services/',views.services)
]