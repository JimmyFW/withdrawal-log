from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from wlapi.models import Visit
from django.http import JsonResponse
from django.views.generic.edit import CreateView

# Create your views here.

class VisitView(ListView):

    model = Visit

class VisitCreate(CreateView):

    model = Visit
    fields = ['reason']

class HomeView(TemplateView):

    template_name = 'wlapi/home.html'