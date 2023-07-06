from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name="register"),
    path("blogs/",views.BlogListView.as_view(),name="blogs"),
    path("bloggers/",views.BloggerListView.as_view(),name="bloggers"),
    path("blog/<int:pk>",views.BlogDetailView.as_view(),name="blog-detail"),
    path("blogger/<int:pk>/",views.BloggerDetailView.as_view(),name="blogger-detail"),
    path('commentblog/<int:pk>',views.add_comment,name="add-comment"),
    path('createblog',views.CreateBlog.as_view(),name="create-blog"),
    path('updateblog/<int:pk>',views.UpdateBlog.as_view(),name="update-blog"),
    path('deleteblog/<int:pk>',views.DeleteBlog.as_view(),name="delete-blog"),
]
