from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class SingUpView(CreateView):
    form_class = UserCreationForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # Modificar en tiempo real el formulario
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Nombre de usuario'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class': 'form-control mb-2',
                                                                'placeholder': 'Confirmación de contraseña'})

        return form