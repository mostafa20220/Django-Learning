from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, default=None ,on_delete=models.CASCADE,)
    date_posted = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(blank=True,default='default.jpg')

    def __str__(self):
        return self.title
