import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

# fake pop script
import random
from app1.models import Accessrecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['search','social','marketplace','news','games']

def add_topic():
    t =Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N):
    
    for entry in range(N):

        # gets the topic for the entry
        top = add_topic
        # create fake data
        fake_url =fakegen.url()
        fake_date = fakegen.date()
        fake_name =fakegen.company()

        webpg = Webpage.objects.get_or_create(topic =top,url=fake_url,name=fake_name)[0]

        acc_rec =Accessrecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("population script")
    populate(20)
    print("population complete")
    