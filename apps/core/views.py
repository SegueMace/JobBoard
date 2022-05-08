from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#from apps.job.scraping import elements

from apps.job.models import job
from apps.userprofile.models import Userprofile
from .forms import CustomUserCreationForm
from scraping import elements
from scraping2 import elements2
from scraping3 import elements3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from scraping1 import datas
from actualites import Base
from blogs import Content
from scraping4 import Cote
from actualites1 import ActuCote
from actu import get_actu, top_news




def  frontpage(request):
    jobs = job.objects.order_by('-created_at')[0:3]
    return render(request, 'core/frontpage.html', {'jobs':jobs})


def  aggregator(request):

    el = elements()
    el2 = elements2()
    el3 = elements3()
    ele = datas()
    values = ele.data()
    taille = range(ele.tailles())

    paginator = Paginator(values, 10) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
  

   
    return render(request, 'core/aggregation.html', {'taille':taille, 'page':page,'posts':posts})





def  cote(request):

    ele = Cote()
    values = ele.coteivoire()

    paginator = Paginator(values, 10) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
  

   
    return render(request, 'core/coteivoire.html', {'page':page,'posts':posts})


    
def actualitescameroun(request):

 
    ele = Base()
    values = ele.datas()

    paginator = Paginator(values, 10) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
  

   
    return render(request, 'core/actualites-cameroun.html', {'page':page,'posts':posts})



    




def blogs(request):

 
    ele = Content()
    values = ele.datas()

    paginator = Paginator(values, 10) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
  

   
    return render(request, 'core/blogs.html', {'page':page,'posts':posts})



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