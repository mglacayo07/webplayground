from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Mi super Web Playground"
    #     return context

    # Este metodo sobre escribe la respuesta de si mismta
    def get(self,request, *args, **kwargs):
        kw = {
            'title': "Mi Super Web Playground"
        }
        return render(request,self.template_name, kw)

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
