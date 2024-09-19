from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for babies index
  path('babies/', views.baby_index, name='baby-index'),
  path('babies/<int:baby_id>/', views.baby_detail, name='baby-detail'),
  path('babies/create/', views.BabyCreate.as_view(), name='baby-create')
]
