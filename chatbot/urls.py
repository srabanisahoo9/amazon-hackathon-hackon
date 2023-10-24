from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'), 
    path('chat/', views.chat, name='chat'),
=======
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name = "register"),
    path('home/', views.home, name="home"),
    path('chat/', views.chat, name="chat"),
    path('profile/', views.profile, name='profile'),
>>>>>>> 3e458008b1e13f6d37ffe6bbd64d9453cea5867c
]