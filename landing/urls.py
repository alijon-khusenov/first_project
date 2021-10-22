from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about/<int:pk>', views.about, name='about'),
]