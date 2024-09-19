from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for babies index
  path('babies/', views.baby_index, name='baby-index'),
  path('babies/<int:baby_id>/', views.baby_detail, name='baby-detail'),
  path('babies/create/', views.BabyCreate.as_view(), name='baby-create'),
  path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name='baby-update'),
  path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name='baby-delete'),
  path('babies/<int:baby_id>/add-feeding', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]
