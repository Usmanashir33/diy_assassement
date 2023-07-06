from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Blogger(models.Model):
    """classs of each blogger that has or can have blogs on the web site"""
    Countries =[
        ('Nigeria',"Nigeria"),
        ('Niger',"Niger"),
        ('Saudi Arabia',"Saudi Arabia"),
        ('Sudan',"Sudan"),
        ('USA',"United State of America"),
        ('UK',"United Kingdom"),
        ('Others',"Others"),
    ]
    first_name = models.CharField(verbose_name='F-Name',max_length=20,help_text="Enter your first name (e.g Usman)")
    last_name = models.CharField(verbose_name="L-Name",max_length=20,help_text="Enter your last name (e.g Ashir)")
    nationality = models.CharField(max_length=20,choices=Countries,default="Nigeria")
    date_of_birth = models.DateField(help_text="Write Your Date of Birth (e.g 14/03/2001)")
    biograpy = models.TextField(max_length=200,help_text="Write a short history about your life")
    
    def display_biograpy(self):
        return self.biograpy[:40] + " ..."
    
    class meta : 
        ordering = ['first_name']
        
    def get_absolute_url(self):
        return reverse("blogger-detail", args=[str(self.id)])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Blog(models.Model) :
    """ class that manages the blog thats posted """
    blogger = models.ForeignKey(Blogger,on_delete=models.SET_NULL,null=True)
    title = models.CharField("Title",max_length=50,help_text="Title of the blog (e.g Success of Hardworker)")
    post_date = models.DateTimeField(auto_now_add=True)
    discription = models.TextField(max_length=200,help_text="Title of the blog (e.g Success of Hardworker)")
    
    def display_discription (self) :
        return self.discription[:30] + " ..."
    
    class Meta :
        ordering = ["-post_date"]
        permissions=(
            ("can_edit_blog","Edit blog"),
            ("can_add_blog", 'Add blog'),
        )
        
    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.id)])
    def __str__(self) :
        if len(self.title) > 60 :
            return self.title[:60]
        else :
            return self.title
    
    
class Comment(models.Model):
    """ class of all the comments thats to bea created for a blog """
    blog =models.ForeignKey(Blog,on_delete=models.CASCADE)
    commenter=models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(help_text="Write your comment here!",max_length=200)
    comment_date =models.DateTimeField(auto_now_add=True)
    def display_comment(self):
        return self.comment[:40] + " ..."
    
    class meta :
        ordering=['-comment_date']
        verbose_name_plural = 'comments'
        
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse("comment-detail", args=[str(self.id)])
    