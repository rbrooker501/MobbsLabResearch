from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='posts')
    image = models.ImageField(null=True, blank=True, upload_to="images/")


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' || ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def __str__(self):
	    return str(self.user)

    def get_absolute_url(self):
        return reverse('home')