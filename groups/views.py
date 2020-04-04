from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Group, StudySession


class IndexView(TemplateView):
    template_name = 'index.html'


class StudyListView(ListView):
    model = StudySession 
    template_name = 'study_list.html'
    context_object_name = "studies"


class StudyDetailView(DetailView):
    template_name = "study_detail.html"
    model = StudySession 
    context_object_name = "study"
