from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    published_date = models.DateTimeField()