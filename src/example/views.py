from django.views.generic.base import TemplateView

class One(TemplateView):
    template_name = 'sample/one.html'

class Two(TemplateView):
    template_name = 'sample/two.html'

class Three(TemplateView):
    template_name = 'sample/three.html'

class A(TemplateView):
    template_name = 'sample/a.html'

class B(TemplateView):
    template_name = 'sample/b.html'

class C(TemplateView):
    template_name = 'sample/c.html'

class D(TemplateView):
    template_name = 'sample/d.html'