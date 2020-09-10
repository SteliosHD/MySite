from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

CATEGORY_CHOICES = (
    ('L','success'),
    ('UC','warning'),
    ('F','info')
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default=timezone.now)# timezone.now is a function but we dont want it to run so no brackets
    # author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many author-User and models.CASCADE if user is deleted the post is removed

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'pk': self.pk})


class PortfolioPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='/media/work.jpg')
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=50)
    date = models.DateField(default=date.today,auto_now=False, auto_now_add=False)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.title
