from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView

from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, EmailForm
from .models import Profile

from django.urls import reverse_lazy
from django import forms


class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    #success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # Modificar en tiempo real el formulario
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailField(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Confirmación de contraseña'})

        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self, queryset=None):
        # recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self, queryset=None):
        # recuperar el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real el formulario
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2',
                                                             'placeholder': 'Email'})
        return form

