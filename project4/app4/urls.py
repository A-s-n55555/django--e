from django.urls import path
from app4 import views
# ṭemplet tagging
app_name = 'app4'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
