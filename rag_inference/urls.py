from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_rag, name='query_rag'),  # Handles /rag/
    path('rag_inference/', views.query_rag, name='rag_inference'), 
]
