from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="exam-index"),
    path('create_exam', views.create_exam, name='create_exam'),
    path('<int:exam_pk>/', views.exam, name="exam-view"),
]