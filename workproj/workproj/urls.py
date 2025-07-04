from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('insert/')),  # ✅ Redirect to insert
    path('', include('workapp.urls')),  # ✅ Make sure this is AFTER the redirect
]
