from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('registration/', views.RegistrationView, name='registration'),
    path('signin/', views.SigninView, name='signin'),
    path('signout/', views.SignoutView, name='signout'),
    path('personalpage/', PersonalPageView.as_view(), name='personalpage'),
    path('addcontact/', views.ContactCreateView, name='addcontact'),
    path('send_email/', views.SendEmailView, name='sendemail'),
    path('verify/<auth_token>', views.VerificationView, name="verify"),

]






