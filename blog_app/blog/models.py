from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    heading = models.CharField(max_length=200)
    subheadings = models.TextField(blank=True, null=True)
    blog_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading
