from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home page
    path('madlib/<int:step>/', views.madlib_question, name='madlib_question'),
    path('madlib/result/', views.madlib_result, name='madlib_result'),
]