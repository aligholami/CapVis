from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^matching_list', views.matches, name='matching_list'),
    url(r'^captioning_list', views.captions, name='captioning_list')
]