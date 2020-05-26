import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from appTwo.models import Topic, Webpage, AccessRecord, User

fakegen = Faker()
topics = ['music', 'comedy', 'wrestling', 'social network', 'art', 'culture']

def add_topic():
    top = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    top.save()
    return top

def populate(N = 5):
    for entry in range(N):

        t = add_topic()
        fake_url =fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_n = fakegen.name().split()
        fake_f_name = fake_n[0]
        fake_l_name = fake_n[1]
        fake_email = fakegen.email()

        webpg = Webpage.objects.get_or_create(topic=t, name = fake_name, url = fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]
        user_rec = User.objects.get_or_create(first_name = fake_f_name, last_name = fake_l_name, emial = fake_email)[0]

if __name__ == '__main__':
    print('POPULATING')
    populate(40)
    print('POPULATING SUCCESSFUL')
