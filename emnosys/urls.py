from django.urls import path
from . import views
from .views import Main
from .views import SignUpView
from .views import RegisterView

urlpatterns = [
    path('', Main.as_view(), name = 'emnosy'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='register'),

]






