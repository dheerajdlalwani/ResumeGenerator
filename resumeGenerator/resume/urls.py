from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/userdetails', views.user_details, name='user_details'),
    path('resume/previewdata', views.preview_data, name='preview_data'),
]


