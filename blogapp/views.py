from django.db import models
from django.shortcuts import render,get_object_or_404,redirect
#importing all the models 
from . models import Blog,Blogger,Comment
from django.views.generic import ListView,DetailView
#import forms
from blogapp.forms import CommentForm,RegistrationForm
#authentication models
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,"blogapp/index.html")
class BlogListView(ListView):
    model=Blog
    paginate_by = 5
    def get_queryset(self):
        ordered_blogs = Blog.objects.all().order_by("-post_date")
        return ordered_blogs
    
class BlogDetailView(DetailView):
    model = Blog 
    
    def get_context_data(self, **kwargs):
        id = self.kwargs.get("pk")
        blog=get_object_or_404(Blog,pk=id)
        blog_comments=blog.comment_set.all().order_by("-comment_date")
        context = super().get_context_data(**kwargs)
        context["blog_comments"] = blog_comments
        return context
    
class BloggerListView(ListView):
    model=Blogger
    paginate_by = 10
    
class BloggerDetailView(DetailView):
    model = Blogger
    
    def get_context_data(self, **kwargs):
        id=self.kwargs.get("pk")
        blogger=get_object_or_404(Blogger,id=id)
        blogger_blogs=blogger.blog_set.all().order_by("-post_date")
        context = super().get_context_data(**kwargs)
        context["blogger_blogs"] = blogger_blogs
        return context
    

from django.http import HttpResponseRedirect
from django.urls import reverse
@login_required
def add_comment(request,pk):
    comment_blog= get_object_or_404(Blog,id=pk)
    if request.method != "POST" :
        form =CommentForm()
    else:
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.commenter = request.user
            new_comment.blog = comment_blog
            new_comment.save()
            return redirect("blog-detail",pk=comment_blog.pk)
    context={
        "form":form,
        "blog":comment_blog,    
    }
    return render(request,"blogapp/add_comment.html",context)

def register(request):
    if request.method == "POST" :
        form=RegistrationForm(request.POST)
        if form.is_valid() :
            form.save()
            #import user to login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("You have successfully Logged in"))
            return redirect("index")
    else :
        form= RegistrationForm()
    context={'form':form}
    return render(request,"blogapp/registration/register.html",context)
            
            
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class CreateBlog(PermissionRequiredMixin,CreateView):
    model = Blog
    fields = "__all__"
    permission_required=['blogapp.can_add_blog']
    
class UpdateBlog(PermissionRequiredMixin,UpdateView):
    model= Blog
    fields=["blogger","title","discription"]
    template_name_suffix="_update"
    permission_required=['blogapp.can_edit_blog']
    
class DeleteBlog(PermissionRequiredMixin,DeleteView):
    model = Blog
    success_url= reverse_lazy("blogs") 
    permission_required=['blogapp.can_edit_blog']