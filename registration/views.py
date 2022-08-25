from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SingUpView(CreateView):
    form_class = UserCreationForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
