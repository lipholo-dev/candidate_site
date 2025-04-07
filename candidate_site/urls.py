from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Main app URLs
    path('polls/', include('polls.urls')),  # Polls app URLs
    # path('user_auth/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('user_auth/', include('user_auth.urls')),  # Custom user_auth app URLs
]