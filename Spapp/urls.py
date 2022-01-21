"""Spcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Spapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('signup/', views.signup, name="signup"),
    path('signup_ajax/', views.signup_ajax, name="signup_ajax"),
    path('productview/<int:id>',views.productview, name='productview'),
    path('login_ajax/', views.login_ajax, name='login_ajax'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('logout/', views.user_logout, name='user_logout'),
    path('forgot_password_ajax/', views.forgot_password_ajax, name='forgot_password_ajax'),
    path('forgot_change_password/<token>/', views.forgot_change_password, name='forgot_change_password'),
    path('forgot_change_password_ajax/', views.forgot_change_password_ajax, name='forgot_change_password_ajax'),
    path('checkout/', views.checkout, name='checkout'),
    path('place_order_ajax/', views.place_order_ajax, name='place_order_ajax'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
