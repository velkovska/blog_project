from django.urls import path
from . import views  # relative import

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='blog-home')
]
