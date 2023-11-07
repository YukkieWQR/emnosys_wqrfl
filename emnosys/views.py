from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login



class Main(TemplateView):
    template_name = 'emnosys/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file'] = 'styles.css'
        return context

#################################
####################################
#################################


def Registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, emnail, password1)
        myuser.save()

        messages.succes(request, "Account created")
        return redirect('emnosys/signin')
    return render(request, "emnosys/registration.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['pass1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Bad Creditals")
            return redirect('home')
    return render(request, "emnosys/signin.html")





def signout(request):
    pass
