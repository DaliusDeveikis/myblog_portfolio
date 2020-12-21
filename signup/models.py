from django.db import models
from django.contrib.auth.models import User
# from django_ckeditor_5.fields import CKEditor5Field

class UserBlog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +" User: "+ str(self.user)