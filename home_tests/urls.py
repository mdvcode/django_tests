from django.urls import path
from . import views

app_name = 'home_tests'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:question_id>/', views.question, name='question'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('home_tests/<int:pk>/', views.DetailView.as_view(), name='detail'),

]
