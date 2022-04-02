from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add),
    path('test', views.home),
    path('contact', views.contact)
]
