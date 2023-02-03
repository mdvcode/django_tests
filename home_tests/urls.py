from django.urls import path
from . import views

app_name = 'home_tests'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/<int:pk>/', views.take_quiz, name='take_quiz'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path("<int:catalog_id>/questions/<int:question_id>", views.display_question, name="display_question"),
    # path('<int:question_id>/results/', views.results, name='results'),

]
