from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
