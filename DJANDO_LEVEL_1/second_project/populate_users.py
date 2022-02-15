import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from AppUsers.models import User
from faker import Faker

def populate(N=5):
    fakegen = Faker()
    for entry in range(N):
        # Create the Fake data for that entry
        fake_fname = fakegen.first_name()
        fake_sname = fakegen.last_name()
        fake_email = fakegen.email()
        user = User.objects.get_or_create(first_name=fake_fname, second_name=fake_sname, email=fake_email)[0]


if __name__ == '__main__':
    print("Populating script")
    populate(10)
    print("Populating complete.")