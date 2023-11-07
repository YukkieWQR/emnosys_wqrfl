from django.urls import path
from . import views
from .views import Main


urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('registration/', views.Registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]






