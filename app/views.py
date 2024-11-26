from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from app.models import *
class SchoolList(ListView):
    model = School
    context_object_name='schools'


class SchoolDetail(DetailView):
    model=School
    context_object_name='scobject'

class SchoolCreate(CreateView):
    model = School
    fields = '__all__'

class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'