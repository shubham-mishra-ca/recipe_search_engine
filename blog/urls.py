from django.urls import path
from . import views


urlpatterns = [
    #path(URL, View Function you want to execute, 'name of the url')
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
    path('search', views.search, name="search"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")

]
