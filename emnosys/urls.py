from django.urls import path
from . import views
from .views import Main

urlpatterns = [
    path('', Main.as_view(), name = 'emnosy'),

]






