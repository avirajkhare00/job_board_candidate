"""job_board_candidate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app2.views import job_show_page, index_page
from app.api import fetch_data_for_db
from common_app.views import forget_password_view

urlpatterns = [
    re_path(r'^job/[0-9a-z-]', job_show_page, name='job_show_page'),
    path('candidate/', include('app.urls')),
    path('candidate/api/v1/', include('app.urls')),
    path('employer/', include('app2.urls')),
    path('employer/api/v1/', include('app.urls')),
    path('forget_password/', forget_password_view, name='forget_password_view'),
    path('admin/', admin.site.urls),
    path('', index_page, name='index_page'),
    path('fetch_everything/', fetch_data_for_db),
]
