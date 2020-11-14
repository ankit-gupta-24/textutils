from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='index'),
    # path('index/',views.index, name='index'),
    path('analyze/',views.analyze,name='analyze'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services')
]