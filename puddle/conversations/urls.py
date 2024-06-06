from django.urls import path
from .views import create_conversation,inbox,chat

app_name = "conversations"

urlpatterns=[path("conversations/<int:item_pk>/",create_conversation,name="new"),
             path("",inbox,name="inbox"),
             path("chat/<int:pk>/",chat,name="chat")]