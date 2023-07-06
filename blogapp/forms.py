from django import  forms
from .models import Comment,Blog,Blogger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm) :
   # comment_field = forms.CharField(max_length=50,help_text="comment here")
    class Meta :
        model=Comment
        fields=["comment"]
from django.contrib.auth.models import User    
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _   
class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=30,help_text="Write a real name (e.g usman)")
    last_name=forms.CharField(max_length=30,help_text="Write a real name (e.g ashir)")
    email=forms.EmailField(help_text="Write a valid email adress")
    
    class Meta :
        model = User
        fields = ["username","first_name",'last_name',"email",'password1','password2']
        
    def clean_email(self):
        data = self.cleaned_data["email"]
        users = User.objects.all()
        users_email = [user.email for user in users]
        if data in users_email :
            raise ValidationError(_("the email is already used by another user"))
        return data
    
