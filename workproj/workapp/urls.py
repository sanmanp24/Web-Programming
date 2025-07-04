from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ This handles the root URL
    path('insert/', views.insert_data, name='insert'),
    path('retrieve/', views.retrieve_data, name='retrieve'),
]
