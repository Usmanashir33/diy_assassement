from django.contrib import admin
from .models import Blog,Blogger,Comment

# Register your models here.
class CommentInline(admin.TabularInline) :
    model = Comment
    extra= 0
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','blogger','display_discription','post_date']
    list_filter=['post_date',"blogger"]
    fieldsets=(
        ("naming",{"fields":(( "title","discription"),"blogger")}),
    )
    inlines = [CommentInline]

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','nationality','date_of_birth','display_biograpy']
    list_filter = ['nationality']
    fieldsets = (
        ("personal info.",{"fields":(("first_name","last_name"),'date_of_birth')}),
        ("more",{"fields":("nationality","biograpy")})
    )
     

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['display_comment',"blog",'comment_date']
    list_filter = ['comment_date',"blog"]