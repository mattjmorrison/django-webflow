from django.views.generic.base import TemplateView

class One(TemplateView):
    template_name = 'sample/one.html'

class Two(TemplateView):
    template_name = 'sample/two.html'

class Three(TemplateView):
    template_name = 'sample/three.html'