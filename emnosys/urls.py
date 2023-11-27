from django.urls import path
from . import views
from .views import Main, PersonalPage, add_contact


urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('registration/', views.Registration, name='registration'),
    path('signin/', views.Signin, name='signin'),
    path('signout/', views.Signout, name='signout'),
    path('personalpage/', PersonalPage.as_view(), name='personalpage'),
    path('addcontact/', views.add_contact, name='addcontact'),
    path('send_email/', views.send_email, name='send_email')
]






