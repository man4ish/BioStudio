from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.variant_interpreter_view, name='upload_vcf'),
]
