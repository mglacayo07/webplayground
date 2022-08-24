from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Page
from .forms import PageForm

# Lista
# todas las Pages
class PageListView(ListView):
    model = Page
    paginate_by = 100


# Se puede ver el detallado de una page
class PageDetailView(DetailView):
    model = Page


# Vista para crear un page
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm

    template_name_suffix = '_update_form'  #Si queremos que vaya a un formulario diferente al de creación.

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
