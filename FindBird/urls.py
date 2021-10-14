from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="IndexPage"),
    path('predictionAudio/', views.predFunc.predictionsAudio, name='PredAudio'),
    path('predictionPhoto/', views.predFunc.predictionsPhoto, name='PredPhoto'),
    path('search/', views.predFunc.search, name="search"),
    path('result/<str:slug>', views.result, name="ResultPage"),
    path('find/', views.find, name='find'),
    path('error/', views.error, name='error'),
    path('sub/', views.predFunc.SUB, name='submit'),
    path('about/', views.about, name='about'),
    path('birdset/',views.Allset, name="birdset"),
]