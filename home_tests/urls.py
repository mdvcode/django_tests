from django.urls import path
from . import views

app_name = 'home_tests'

urlpatterns = [
    path('home/', views.home, name='home'),

]
