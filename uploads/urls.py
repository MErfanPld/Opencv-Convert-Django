from django.urls import path, include
from .views import UploadList

urlpatterns = [
    path('', UploadList.as_view())
] 
