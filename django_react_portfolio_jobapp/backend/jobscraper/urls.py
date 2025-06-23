from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.JobScrapeView.as_view(), name='job-scrape'),
]
