import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import JobListing

Job_roles = [
    "Full Stack Developer",
    "Full Stack Engineer",
    "Python Full Stack Developer",
    "MERN Stack Developer",
    "Full Stack Web Developer",
    "Django + React Full Stack Developer",
    "Backend Developer (Python)",
    "Python Developer",
    "Django Developer",
    "Python Backend Developer",
    "Python Django REST API Developer",
    "Flask Developer",
    "API Developer (Django/Flask)",
    "Frontend Developer (React/JavaScript)",
    "React.js Developer",
    "JavaScript Frontend Developer"
]

company_career_sites = {
    "Meta": "https://careers.meta.com",
    "Google": "https://careers.google.com",
    "Amazon": "https://www.amazon.jobs",
    "Apple": "https://jobs.apple.com",
    "Microsoft": "https://careers.microsoft.com",
    "Netflix": "https://jobs.netflix.com",
    "Nvidia": "https://www.nvidia.com/en-us/about-nvidia/careers",
    "Stripe": "https://stripe.com/careers",
    "OpenAI": "https://openai.com/careers",
    "Anthropic": "https://www.anthropic.com/careers",
    "Citadel": "https://www.citadel.com/careers",
    "Jane Street": "https://www.janestreet.com/careers",
    "Optiver": "https://optiver.com/careers",
    "IMC Trading": "https://www.imc.com/careers",
    "Two Sigma": "https://twosigma.com/careers",
    "Airbnb": "https://careers.airbnb.com",
    "Uber": "https://www.uber.com/careers",
    "LinkedIn": "https://careers.linkedin.com",
    "Adobe": "https://www.adobe.com/careers",
    "Salesforce": "https://www.salesforce.com/company/careers",
    "VMware": "https://careers.vmware.com",
    "Atlassian": "https://www.atlassian.com/company/careers",
    "Snap": "https://www.snap.com/jobs",
    "Spotify": "https://www.spotifyjobs.com",
    "Twitter": "https://careers.twitter.com",
    "Tesla": "https://www.tesla.com/careers",
    "Plaid": "https://plaid.com/careers",
    "Databricks": "https://databricks.com/company/careers",
    "Coinbase": "https://www.coinbase.com/careers",
    "Roblox": "https://corp.roblox.com/careers",
    "ServiceNow": "https://www.servicenow.com/careers",
    "Intuit": "https://www.intuit.com/careers",
    "SAP": "https://careers.sap.com",
    "Cisco": "https://www.cisco.com/c/en/us/about/careers.html",
    "Square": "https://squareup.com/us/en/careers",
    "Splunk": "https://www.splunk.com/en_us/careers.html",
    "Shopify": "https://www.shopify.com/careers",
    "MongoDB": "https://www.mongodb.com/careers",
    "Dropbox": "https://www.dropbox.com/jobs",
    "Zoom": "https://zoom.us/careers",
    "Box": "https://www.box.com/careers",
    "Fortinet": "https://www.fortinet.com/careers",
    "Palo Alto Networks": "https://jobs.paloaltonetworks.com",
    "Cloudflare": "https://www.cloudflare.com/careers",
    "Twilio": "https://www.twilio.com/company/jobs",
    "ZoomInfo": "https://www.zoominfo.com/careers",
    "Snowflake": "https://www.snowflake.com/careers",
    "GitHub": "https://github.com/about/careers",
    "HashiCorp": "https://www.hashicorp.com/careers",
    "Oracle": "https://www.oracle.com/corporate/careers",
    "IBM": "https://www.ibm.com/careers",
    "Bloomberg": "https://www.bloomberg.com/careers",
    "PayPal": "https://www.paypal.com/careers",
    "Red Hat": "https://www.redhat.com/en/jobs",
    "Motorola": "https://www.motorola.com/jobs",
    "Nokia": "https://www.nokia.com/about-us/careers",
    "Siemens": "https://jobs.siemens.com",
    "Philips": "https://www.philips.com/a-w/careers.html",
    "Ericsson": "https://www.ericsson.com/en/careers",
    "PhonePe": "https://www.phonepe.com/careers",
    "Zomato": "https://careers.zomato.com",
    "Hotstar": "https://www.hotstar.com/in/career",
    "Infosys": "https://www.infosys.com/careers",
    "TCS": "https://www.tcs.com/careers",
    "Wipro": "https://www.wipro.com/careers",
    "HCL Technologies": "https://www.hcltech.com/careers",
    "Flipkart": "https://www.flipkartcareers.com",
    "Myntra": "https://www.myntra.com/careers",
    "Ola": "https://www.olacabs.com/careers",
    "Paytm": "https://careers.paytm.com",
    "Udaan": "https://careers.udaan.com",
    "Delhivery": "https://careers.delhivery.com",
    "Cure.fit": "https://www.cure.fit/careers",
    "Zendesk": "https://www.zendesk.com/company/careers",
    "Honeywell": "https://careersathoneywell.com",
    "Mastercard": "https://mastercard.jobs",
    "Xero": "https://www.xero.com/careers",
    "Workday": "https://www.workday.com/en-us/company/careers",
    "DocuSign": "https://www.docusign.com/company/careers",
    "Adyen": "https://www.adyen.com/careers",
    "WeTransfer": "https://wetransfer.com/careers",
    "Airwallex": "https://www.airwallex.com/careers",
    "Expedia": "https://careers.expedia.com",
    "Reddit": "https://www.redditinc.com/careers",
    "ThirstySprout": "https://thirstysprout.com/careers",
    "Tomorrow Health": "https://www.tomorrowhealth.com/careers",
    "Latitude": "https://www.joinlatitude.com/careers",
    "Cogoport": "https://www.cogoport.com/careers",
    "Fractal Analytics": "https://fractalanalytics.com/careers",
    "Skit.ai": "https://skit.ai/careers",
    "Razorpay": "https://razorpay.com/careers",
    "InMobi": "https://www.inmobi.com/company/careers",
    "Freshworks": "https://www.freshworks.com/company/careers"
}

def scrape_naukri(job_role):
    # Implement scraping logic for Naukri.com for the given job_role
    # This is a placeholder function
    results = []
    # Example scraping code (to be replaced with actual scraping logic)
    url = f"https://www.naukri.com/{job_role.replace(' ', '-')}-jobs"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse job listings here and append to results
    return results

def scrape_linkedin(job_role):
    # Implement scraping logic for LinkedIn for the given job_role
    # This is a placeholder function
    results = []
    # Example scraping code (to be replaced with actual scraping logic)
    url = f"https://www.linkedin.com/jobs/search?keywords={job_role.replace(' ', '%20')}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse job listings here and append to results
    return results

def scrape_all_jobs():
    all_jobs = []
    for job_role in Job_roles:
        naukri_jobs = scrape_naukri(job_role)
        linkedin_jobs = scrape_linkedin(job_role)
        all_jobs.extend(naukri_jobs)
        all_jobs.extend(linkedin_jobs)
    return all_jobs

def save_jobs_to_db(jobs):
    for job in jobs:
        JobListing.objects.update_or_create(
            job_role=job.get('job_role'),
            company_name=job.get('company_name'),
            location=job.get('location'),
            apply_link=job.get('apply_link'),
            defaults={'hiring_posted_date': job.get('hiring_posted_date')}
        )
