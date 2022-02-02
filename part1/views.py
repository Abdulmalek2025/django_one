
from pyexpat import model
from re import template
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Flower
#the name of views shuold postfix with View word
# class HomeView(View):
#     def get(self, request,*args,**kwargs):
#         return render(request,'part1/home.html')
class HomeView(ListView):
    template_name = 'part1/home.html'
    model = Flower
    paginate_by = 5


class FlowerDetailView(DetailView):
    template_name = 'part1/detail.html'
    model = Flower
    context_object_name = 'flower'
