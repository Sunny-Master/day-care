from django.shortcuts import render

class Baby:
  def __init__(self, name, diet, description, age):
    self.name = name
    self.diet = diet
    self.description = description
    self.age = age

babies = [
  Baby('April', 'vegetarian', 'always playful.', 1),
  Baby('May', 'vegan', 'likes to fiddle with things.', 3),
  Baby('June', 'lactose-free', 'hyperactive at all times.', 2),
  Baby('August', 'nut-free', 'calm and curious.', 0)
]
# Create your views here.

def home(request):
  return render (request, 'home.html')

def about(request):
  return render(request, 'about.html')

def baby_index(request):
  return render(request, 'babies/index.html', { 'babies': babies })
