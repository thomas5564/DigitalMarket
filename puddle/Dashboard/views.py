from django.shortcuts import render
from item.models import Item,Category
from django.contrib.auth.decorators import login_required;

@login_required
def Dashboard(req):
    Catergories=Category.objects.all()
    Items=Item.objects.all()
    return render(req,"Dashboard/Dashboard.html",{'Categories':Catergories,'Items':Items})