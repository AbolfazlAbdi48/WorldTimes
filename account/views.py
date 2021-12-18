from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


# Create your views here.
class RegisterView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    form_class = RegisterForm
