from django.db import models

# Create your models here.
class Team(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='photos/%Y/%M/%S')
    facebook_link=models.URLField(max_length=100)
    twitter_link=models.URLField(max_length=100)
    google_link=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name