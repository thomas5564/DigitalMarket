from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from .forms import createItemForm,editItemForm
from django.contrib.auth.decorators import login_required
import logging


def item(req,pk):
    item= get_object_or_404(Item,pk=pk)
    return render(req,"item/item.html",{"item":item})



logger = logging.getLogger(__name__)

def deleteItem(req,pk):
    item=get_object_or_404(Item, pk=pk , created_by=req.user)
    item.delete()
    return redirect("core:index")


def editItem(request, pk):
    user = request.user
    item = get_object_or_404(Item, pk=pk, created_by=user)
    
    if request.method == "POST":
        form = editItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            logger.info(f'Item edited: {item}')  # Log the item creation
            return redirect('item:details', pk=item.id)  # Redirect to the item details page after saving
        else:
            logger.warning('Form is not valid')
    else:
        form = editItemForm(instance=item)  # Initialize the form with the item instance
    
    return render(request, "item/editItem.html", {"form": form, "user": user})


@login_required
def createItem(request):
    user=request.user
    if request.method == "POST":
        form = createItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = user
            item.is_sold=False
            item.save()
            logger.info(f'Item created: {item}')  # Log the item creation
            return redirect('item:details',pk=item.id)  # Redirect to the index page after saving
        else:
            logger.warning('Form is not valid')
    else:
        form = createItemForm()
    return render(request, "item/createItem.html", {"form": form,"user":user})



