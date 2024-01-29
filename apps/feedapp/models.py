from django.db import models
from apps.login.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    message = models.TextField()
    like = models.ManyToManyField(User,related_name="liked_msgs")
    created_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name = "comments",on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = "comments",on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.ManyToManyField(User,related_name="liked_cmnts")
    created_at = models.DateTimeField(auto_now_add = True)
