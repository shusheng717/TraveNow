from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class Pre_HomePage(TemplateView):
    template_name='pre_index.html'

class HomePage(TemplateView):
    template_name='index.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class AboutPage(TemplateView):
    template_name='about.html'
