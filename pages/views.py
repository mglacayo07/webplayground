from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Page


# Lista todas las Pages
class PageListView(ListView):
    model = Page
    paginate_by = 100


# Se puede ver el detallado de una page
class PageDetailView(DetailView):
    model = Page


# Vista para crear un page
class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']  # campos que son editables
    success_url = reverse_lazy('pages:pages')


class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'  #Si queremos que vaya a un formulario diferente al de creación.

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
