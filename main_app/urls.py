from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for babies index
  path('babies/', views.baby_index, name='baby-index'),
]
