from django.urls import path
from . import views

app_name = 'download-page'
urlpatterns = [
    path('download/', views.download, name='download'),
]