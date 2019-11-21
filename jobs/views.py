from django.shortcuts import render

from .models import Job

def home(request):
	currentjobs = Job.objects.filter(current=True)
	pastjobs = Job.objects.filter(current=False)
	return render(request, 'jobs/home.html', {'currentjobs':currentjobs, 'pastjobs':pastjobs})

	