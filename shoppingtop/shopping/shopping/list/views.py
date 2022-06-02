from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

class ShoppingListView(LoginRequiredMixin, ListView): 
    model = models.List

class ShoppingDetailView(LoginRequiredMixin, DetailView): 
    model = models.List

class ShoppingUpdateView(LoginRequiredMixin, UpdateView): 
    model = models.List
    fields = "__all__"

class ShoppingDeleteView(LoginRequiredMixin, DeleteView): 
    model = models.List

class ShoppingCreateView(LoginRequiredMixin, CreateView): 
    model = models.List
    fields = "__all__"

