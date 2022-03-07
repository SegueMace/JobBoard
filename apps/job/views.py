from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import job
from .forms import AddJobForm, ApplicationForm

from apps.notification.utilities import create_notification

# Create your views here.


def search(request):
    return render(request, 'job/search.html')




def job_detail(request, job_id):
    jobid = job.objects.get(pk=job_id)
    return render(request, 'job/job_detail.html', {'jobid':jobid})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form':form})



@login_required
def apply_for_job(request, job_id):
    jobid = job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job =jobid
            application.created_by = request.user
            application.save()

            create_notification(request, jobid.created_by, 'application', extra_id=application.id)
            
            return redirect('dashboard')
    else:
         form = ApplicationForm()
        
    return render(request, 'job/apply_for_job.html', {'form':form, 'jobid':jobid})





    