from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
