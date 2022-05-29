import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'three_exercise.settings')

import django
django.setup()

#Fake pop script
from exercise_app.models import Users
from faker import Faker

fakegen = Faker()

def create_fake_users(i=5):
    for item in range(i):
        # create the fake data
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        # create the new user
        user = Users.objects.get_or_create(user_firstname=fake_firstname, user_lastname=fake_lastname, user_email=fake_email)[0]

if __name__ == '__main__':
    print('populating script START')
    create_fake_users(20)
    print('populating script END')
