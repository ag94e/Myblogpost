from django.db import models
from django.contrib.auth.models import User

class UserProfileModel(User, models.Model):
    """ User profile model. """
    profile_username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_by_user")
    description      = models.CharField(max_length=400)
    created_at       = models.DateTimeField(auto_now_add=True)
