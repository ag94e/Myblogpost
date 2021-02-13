from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostModel(models.Model):
    """ Model Post """

    status_post = (('draft','Draft'),('published','Published'))
    author    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    title     = models.CharField(max_length=250)
    slugname  = models.SlugField(max_length=50, unique_for_date='date')
    content   = models.TextField()
    date      = models.DateTimeField(default=timezone.now)
    status    = models.CharField(max_length=10, choices=status_post, default='draft')   

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.slugname