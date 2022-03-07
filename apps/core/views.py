from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#from apps.job.scraping import elements

from apps.job.models import job
from apps.userprofile.models import Userprofile
from .forms import CustomUserCreationForm


def  frontpage(request):
    jobs = job.objects.order_by('-created_at')[0:3]
    return render(request, 'core/frontpage.html', {'jobs':jobs})

def signup(request):
    if request.method == 'POST':
         form = CustomUserCreationForm(request.POST)
         
         if form.is_valid():
             user = form.save()

             account_type = request.POST.get('account_type', 'jobseeker')

             if account_type == 'employer':
                 userprofile = Userprofile.objects.create(user=user, is_employer=True)
                 userprofile.save()
             else:
                 userprofile = Userprofile.objects.create(user=user)
                 userprofile.save()

             login(request, user)

             return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
   
    return render(request, 'core/signup.html', {'form':form})


#def  aggregation(request):
 #   print(elements.metiers)
  ## return render(request, 'core/aggregation.html', {'jobs':jobs})