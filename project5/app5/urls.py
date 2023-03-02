from django.urls import path
from app5 import views

app_name='app5'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
