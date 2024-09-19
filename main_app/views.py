from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Baby
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'babies/detail.html', { 
    'baby': baby, 'feeding_form': feeding_form
  })

def add_feeding(request, baby_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the baby_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.baby_id = baby_id
    new_feeding.save()
  return redirect('baby-detail', baby_id=baby_id)

class BabyCreate(CreateView):
  model = Baby
  fields = ['name', 'diet', 'description', 'age']

class BabyUpdate(UpdateView):
  model = Baby
  fields = ['diet', 'description', 'age']

class BabyDelete(DeleteView):
  model = Baby
  success_url = '/babies/'
