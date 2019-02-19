from django.urls import path
from app2.views import register_page

urlpatterns = [
    path('register/', register_page, name='register_page'),
]
