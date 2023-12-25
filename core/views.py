from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ServiceView(TemplateView):
    template_name = 'service.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class WhyView(TemplateView):
    template_name = 'why.html'
