from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
    path('feedapp',views.feedapp),
    path('logout',views.logout),
    path('post_message',views.post_message),
    path('post_comment/<int:msg_id>',views.post_comment),
    path('delete/<int:msg_id>',views.delete_msg),
    path('user_posts',views.user_posts),
    path('like_msg/<int:msg_id>',views.liked_messages),
    path('like_cmnt/<int:cmnt_id>',views.liked_comments),
    path('user_posts/<int:user_id>',views.user_posts),
    
]