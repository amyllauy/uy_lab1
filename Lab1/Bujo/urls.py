"""Bujo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from Pages import views

urlpatterns = [
	path('', views.redir_view, name='home'),
	path('home/', views.home_view, name='home'),
    
    path('admin/', admin.site.urls),

    path('profile/', views.profile_view, name='profile'),
    path('profile/edit_nickname/', views.edit_nickname_view, name='profile_edit_nickname'),
    path('profile/edit_bio/', views.edit_bio_view, name='profile_edit_bio'),

    path('key/', views.key_view, name='key'),
    path('key/add_key/', views.add_key_view, name='key_add'),

    path('this_week/', views.week_view, name='this_week'),
    path('this_week/add_week/', views.add_week_view, name='this_week_add'),
    path('this_week/edit_week/)', views.edit_week_view, name='this_week_edit'),
    path('this_week/delete_week/', views.delete_week_view, name='this_week_delete'),
    path('this_week/delete_week/<int:pk>/', views.delete_week_view, name='this_week_delete_pk'),

    path('today/', views.today_view, name='today'),
    path('today/add_today/', views.add_today_view, name='today_add'),
    path('today/edit_today/)', views.edit_today_view, name='today_edit'),
    path('today/delete_today/', views.delete_today_view, name='today_delete'),
    path('today/delete_today/<int:pk>/', views.delete_today_view, name='today_delete_pk'),
]
