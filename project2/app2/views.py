from django.shortcuts import render
# from app2.models import User
from app2.forms import newuserform
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
   

   form =newuserform()

   if request.method =="POST":
       form = newuserform(request.POST)
   
       if form.is_valid():
           form.save(commit=True)
           return index(request)
       else:
           print("error form invalid")

   return render(request,'apptwo/forms.html',{'form': form})