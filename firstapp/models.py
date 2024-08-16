from django.db import models
import os


def get_profile_image_path(instance, filename):
    return os.path.join("profile_images", f"{instance.name}_{filename}")


class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    about = models.CharField(max_length=500)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to=get_profile_image_path, blank=True, null=True
    )

    def __str__(self):
        return self.name
