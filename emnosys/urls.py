from django.urls import path
from . import views
from .views import Main, PersonalPage


urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('registration/', views.Registration, name='registration'),
    path('signin/', views.Signin, name='signin'),
    path('signout/', views.Signout, name='signout'),
    path('personalpage/', PersonalPage.as_view(), name='personalpage'),
]






