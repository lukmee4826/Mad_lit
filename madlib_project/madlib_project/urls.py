"""madlib_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from madlib_app import views
from django.shortcuts import redirect 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('madlib/<int:step>/', views.madlib_question, name='madlib_question'),
    path('madlib/result/', views.madlib_result, name='madlib_result'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/madlib/1/')),  # ✅ Redirect root URL
    path('madlib/', include('madlib_app.urls'))
]
