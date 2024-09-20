# Yes, Django signals run in the same thread as the caller by default. 
# When a signal is triggered, it is executed synchronously in the same thread that triggered the signal. 
# This means the signal handler will block further code execution until it finishes, running in the same execution context.

import os
import django
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Set the environment variable and initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Define the signal handler
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, created, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Function to create a user and trigger the signal
def create_user():
    print(f"Caller running in thread: {threading.current_thread().name}")
    user = User.objects.create(username="testuser")

# Call the function
create_user()

# Expected Output:
# Caller running in thread: MainThread
# Signal handler running in thread: MainThread