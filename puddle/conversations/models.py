from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Conversation(models.Model):
    members=models.ManyToManyField(User,related_name="conversations")
    item= models.ForeignKey(Item,related_name="conversations", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    edited_at=models.DateTimeField(auto_now=True)

class Message(models.Model):
    created_by=models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    conversation= models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)