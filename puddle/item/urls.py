from django.urls import path
from .views import item,createItem,deleteItem,editItem

app_name="item"

urlpatterns=[
    path('<int:pk>',item, name="details"),
    path('createItem',createItem, name="createItem"),
    path('<int:pk>/delete/',deleteItem,name="delete"),
    path('<int:pk>/edit/',editItem,name="edit"),]