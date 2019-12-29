import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyDjangoProject.settings')

import django
django.setup()


import random
from MyDjangoApp.models import AccessRecord,Webpage,Topic,User
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']


def addTopic():
    t = Topic.objects.get_or_create(topName=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        topic = addTopic()
        fakeURL = fakegen.url()
        fakeDate = fakegen.date()
        fakeName = fakegen.name()
        fakeEmail = fakegen.email()

        webpg = Webpage.objects.get_or_create(topic=topic,url=fakeURL,name=fakeName)[0]

        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fakeDate)[0]
        usr = User.objects.get_or_create(fname=fakeName.split()[0],lname=fakeName.split()[1],email=fakeEmail)[0]


if __name__ == '__main__':
    print('Populating ...')
    populate(20)
    print('Populating complete!')
