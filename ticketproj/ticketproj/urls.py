"""ticketproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from userapp import views as user_views
from mainapp import views as main_views
from adminapp import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # mainapp
    path('',main_views.index,name='index-page'),

    # adminapp
    path('admin-login',admin_views.admin_login,name='admin-login'),
    path('admin-view-ticket',admin_views.admin_view_ticket,name='admin-view-ticket'),
    path('accept-ticket/<int:id>/',admin_views.accept,name='accept-ticket'),
    path('reject-ticket/<int:id>/',admin_views.reject,name='reject-ticket'),

    # userapp
    path('user-register',user_views.user_register,name='user-register'),
    path('user-login',user_views.user_login,name='user-login'),
    path('user-home',user_views.user_home,name='user-home'),
    path('user-view-status',user_views.user_view_status,name='user-view-status'),
]