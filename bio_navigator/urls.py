from django.urls import path
from . import views

app_name = 'bio_navigator'  # <-- This is critical

urlpatterns = [
    path('', views.ask_question, name='ask_question'),
]