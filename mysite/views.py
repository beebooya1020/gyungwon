from  django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class aboutView(TemplateView):
    template_name = 'about.html'