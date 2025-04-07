from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Login page
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),  # Authenticate user
    path('show_user/', views.show_user, name='show_user'),  # Show user details
    path('register/', views.register, name='register'),  # User registration
]