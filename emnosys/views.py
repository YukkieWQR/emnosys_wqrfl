from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def auth_check(request):
    if request.user.is_authenticated:
        user_auth = True
        return user_auth
    else:
        user_auth = False
        return user_auth


class Main(TemplateView):
    template_name = 'emnosys/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file'] = 'styles.css'
        return context




class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'emnosys/login.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was logged in to your account successfully"





class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('')
    template_name = 'emnosys/registration.html'
    success_message = "Your profile was created successfully"


