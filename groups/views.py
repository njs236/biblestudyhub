from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Group, StudySession


class IndexView(TemplateView):
    template_name = 'index.html'


class StudyListView(ListView):
    model = StudySession 
    template_name = 'study_list.html'
    context_object_name = "studies"
