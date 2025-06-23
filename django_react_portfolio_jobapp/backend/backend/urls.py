from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/jobscraper/', include('jobscraper.urls')),
]
