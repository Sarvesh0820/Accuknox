# By default, Django signals are executed synchronously. 
# This means that when a signal is triggered, it is executed immediately, blocking further execution until the signal handler finishes.

import os
import django
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Set the environment variable and initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Define the signal handler
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(3)  # Simulate delay
    print("Signal handler finished")

# Function to create a user and trigger the signal
def create_user():
    print("Before saving user")
    user = User.objects.create(username="testuser")
    print("User saved")

# Call the function
create_user()

# Expected Output:
# Before saving user
# Signal handler started
# Signal handler finished
# User saved
