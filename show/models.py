from django.db import models

# Create your models here.

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    location = models.TextField()
    img = models.ImageField(upload_to = 'images', null=True, blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name