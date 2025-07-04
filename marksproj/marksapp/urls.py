from django.urls import path
from . import views
urlpatterns=[
    path('',views.pageone,name='pageone'),
    path('pagetwo/',views.pagetwo,name='pagetwo'),
]