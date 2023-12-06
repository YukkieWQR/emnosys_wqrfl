from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import SendEmail


####################################################

class MainView(TemplateView):
    template_name = 'emnosys/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file'] = 'styles.css'
        return context

###################################################



def RegistrationView(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()

        return redirect('signin')
    return render(request, "emnosys/registration.html")

###############################################

def SigninView(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['pass1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return render(request, "emnosys/main.html")
        else:
            return redirect('signin')
    return render(request, "emnosys/signin.html")

################################################

def SignoutView(request):
    logout(request)
    return redirect('home')

######################################################

class PersonalPageView(TemplateView):
    template_name = 'emnosys/personalpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file'] = 'styles.css'
        return context

####################################################

@login_required
def ContactCreateView(request):
    if request.method == 'POST':
        username = request.POST.get('about--username')
        message = request.POST.get('about--textarea')
        email = request.POST.get('about--email')
        if not all([username, message, email]):
            return render(request, 'emnosys/addcontacts.html')
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'emnosys/addcontacts.html')
        contact = Contact(username=username, message=message, email=email, contactowner=request.user)
        contact.save()
        return HttpResponseRedirect(reverse('personalpage'))
    return render(request, 'emnosys/addcontacts.html')


##################################


def SendEmailView(request):
    SendEmail(request)
    return redirect('/')
