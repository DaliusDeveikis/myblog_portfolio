from django.forms import ModelForm
from .models import UserBlog

class UserCreatForm(ModelForm):
    class Meta:
        model = UserBlog
        fields = ['title', 'description', 'important']