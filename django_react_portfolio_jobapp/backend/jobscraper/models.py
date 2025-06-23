from django.db import models

class JobListing(models.Model):
    job_role = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    hiring_posted_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    apply_link = models.URLField()

    def __str__(self):
        return f"{self.job_role} at {self.company_name}"
