from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('registration', views.registerPage, name='regestration'),
    path('login', views.loginPage, name="login" ),
    path('logout', views.logoutUser, name="logout"),
]