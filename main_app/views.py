from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Baby, Toy
from .forms import FeedingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def baby_index(request):
  babies = Baby.objects.filter(user=request.user)
  return render(request, 'babies/index.html', { 'babies': babies})

@login_required
def baby_detail(request, baby_id):
  baby = Baby.objects.get(id=baby_id)
  toys_baby_doesnt_have = Toy.objects.exclude(id__in = baby.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'babies/detail.html', { 
    'baby': baby, 'feeding_form': feeding_form, 'toys': toys_baby_doesnt_have
  })

@login_required
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

@login_required
def assoc_toy(request, baby_id, toy_id):
  Baby.objects.get(id=baby_id).toys.add(toy_id)
  return redirect('baby-detail', baby_id=baby_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('baby-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class BabyCreate(LoginRequiredMixin, CreateView):
  model = Baby
  fields = ['name', 'diet', 'description', 'age']

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the baby
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class BabyUpdate(LoginRequiredMixin, UpdateView):
  model = Baby
  fields = ['diet', 'description', 'age']

class BabyDelete(LoginRequiredMixin, DeleteView):
  model = Baby
  success_url = '/babies/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'