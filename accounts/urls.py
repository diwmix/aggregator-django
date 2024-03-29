from django.urls import path
from .views import user_register, user_login, user_logout, user_profile, user_update_profile

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/edit/', user_update_profile, name='update_profile')
]   