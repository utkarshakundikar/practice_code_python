from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobListing
from .scraper import scrape_all_jobs, save_jobs_to_db

class JobScrapeView(APIView):
    def get(self, request):
        # Scrape jobs and save to DB
        jobs = scrape_all_jobs()
        save_jobs_to_db(jobs)
        # Fetch jobs from DB to return
        job_listings = JobListing.objects.all().values('job_role', 'company_name', 'hiring_posted_date', 'location', 'apply_link')
        return Response({'jobs': list(job_listings)})
