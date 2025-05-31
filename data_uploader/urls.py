from django.urls import path
from .views import upload_file, build_faiss_index

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('build_index/', build_faiss_index, name='build_faiss_index'),
]
