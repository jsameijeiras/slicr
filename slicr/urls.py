from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('download', views.download_view, name='download'),
    path('about', views.about_view, name='about'),
]