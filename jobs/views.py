from django.shortcuts import render, get_object_or_404

from .models import Job

def home(request):
	currentjobs = Job.objects.filter(current=True)
	pastjobs = Job.objects.filter(current=False)
	return render(request, 'jobs/home.html', {'currentjobs':currentjobs, 'pastjobs':pastjobs})

def aboutme(request):
	return render(request, 'jobs/aboutme.html')

def jobdetail(request, job_id):
	detailedjob = get_object_or_404(Job, pk=job_id)
	return render(request, 'jobs/jobdetail.html', {"job":detailedjob})