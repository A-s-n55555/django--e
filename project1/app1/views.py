from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic,Webpage,Accessrecord

# Create your views here.
def index(request):
    webpages_list = Accessrecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'firstapp/index.html',context=date_dict)

