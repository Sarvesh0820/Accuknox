# Yes, by default, Django signals run in the same database transaction as the caller. 
# This means if the signal is triggered as part of a database operation (like post_save), the signal handler's execution is tied to the same transaction. 
# If the transaction is rolled back, changes made in both the caller and the signal handler are discarded.

import os
import django
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Set the environment variable and initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Signal handler that attempts to modify a field in the same transaction
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, created, **kwargs):
    print("Signal handler executing.")
    # Modify a field in the User instance
    instance.email = "signal@example.com"
    instance.save()

# Function to create a user and trigger the signal within a transaction
def create_user_in_transaction():
    try:
        with transaction.atomic():  # Start a transaction
            print("Transaction started.")
            user = User.objects.create(username="testuser")
            print("User created.")
            # Simulate an exception that will roll back the transaction
            raise Exception("Simulated error, rolling back transaction.")
    except Exception as e:
        print(f"Exception caught: {e}")

# Call the function
create_user_in_transaction()

# Check if the user was saved in the database
if User.objects.filter(username="testuser").exists():
    print("User exists in the database.")
else:
    print("User does not exist, transaction was rolled back.")

# Expected Output:
# Transaction started.
# User created.
# Signal handler executing.
# Exception caught: Simulated error, rolling back transaction.
# User does not exist, transaction was rolled back.