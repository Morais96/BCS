from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soon_page, name='Coming Soon'),
]