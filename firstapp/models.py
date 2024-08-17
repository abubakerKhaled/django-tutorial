from django.db import models
from django.contrib.auth.models import User
import os


def get_profile_image_path(instance, filename):
    # Ensures unique filenames based on the primary key
    return os.path.join("profile_images", f"{instance.pk}_{filename}")


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250, unique=True)  # Required field
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=250)  # Required field
    company = models.CharField(max_length=250, blank=True)
    job = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to=get_profile_image_path, blank=True, null=True
    )

    def __str__(self):
        return self.name
