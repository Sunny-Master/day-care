from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Baby

# Create your views here.

def home(request):
  return render (request, 'home.html')

def about(request):
  return render(request, 'about.html')

def baby_index(request):
  babies = Baby.objects.all()
  return render(request, 'babies/index.html', { 'babies': babies})

def baby_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  return render(request, 'babies/detail.html', { 'baby': baby})

class BabyCreate(CreateView):
  model = Baby
  fields = ['name', 'diet', 'description', 'age']

class BabyUpdate(UpdateView):
  model = Baby
  fields = ['diet', 'description', 'age']

class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'
