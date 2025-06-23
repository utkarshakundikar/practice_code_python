from django.urls import path
from . import views

urlpatterns = [
    path('themes/', views.ThemeList.as_view(), name='theme-list'),
]
