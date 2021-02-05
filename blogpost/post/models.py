from django.db import models
from blogpost.profile_username.models import UserProfileModel

class PostModel(UserProfileModel, models.Model):
    """ Model Post """
    post_user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, related_name="user_posts")
    title     = models.CharField(max_length=55)
    content   = models.CharField(max_length=8000)
    likes     = models.IntegerField(default=0)
