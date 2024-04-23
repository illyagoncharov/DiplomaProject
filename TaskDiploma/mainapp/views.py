from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from mainapp.forms import RegistrationForm

# Create your views here.
class Index(TemplateView):
    template_name = "mainapp/index.html"


class LoginApp(LoginView):
    template_name = 'mainapp/login.html'
    next_page = '/'


class RegisterApp(CreateView):
    form_class = RegistrationForm
    template_name = 'mainapp/registration.html'
    success_url = "/login"

class LogoutApp(LoginRequiredMixin, LogoutView):
    next_page = '/'