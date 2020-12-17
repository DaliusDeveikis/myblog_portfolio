from django.db import models

class About(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    skills = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='aboutme/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.name
