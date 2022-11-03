from django.shortcuts import render
from .models import Upload
from django.views.generic import ListView

# Create your views here.

class UploadList(ListView):
    model = Upload
    context_object_name = 'uploads'
    template_name='uploads/upload_list.html'

