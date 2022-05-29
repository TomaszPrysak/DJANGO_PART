import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

#Fake pop script
import random
from second_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

topic_to_create = ['Search', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic_to_create))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        # get topic for the entry
        top = add_topic()
        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fakte_name = fakegen.company()
        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, name=fakte_name, url=fake_url)[0]
        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script START')
    populate(20)
    print('populating script END')
