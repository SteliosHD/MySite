from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Post,PortfolioPost

from .forms import ContactForm 
from django.contrib import messages

import json


# import sys;sys.path.insert(1,'/home/hodropetsos/Documents/Information Technology/Programming Projects/Django/django_project/django_project') insert dir to path

class HomeView(ListView):
    model = Post
    template_name = 'contact/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tab_title'] = 'home'
        return context
    # and object_list is passed in the html immediatly


class PortfolioView(ListView):
    model = PortfolioPost
    template_name = 'contact/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tab_title'] = 'portfolio'
        return context
    # and object_list is passed in the html immediatly
