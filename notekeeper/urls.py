from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),               # existing HTML routes
    path('api/', include('notes.api_urls')),       # ✅ new API routes added here
]
