from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Blog(models.Model):
    title = models.CharField('Title', max_length=200)
    description = CKEditor5Field('description', config_name='extends')
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title
