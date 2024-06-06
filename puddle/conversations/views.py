from django.shortcuts import render,redirect,get_object_or_404
from item.models import Item
from .models import Conversation
from .forms import MessageForm

def create_conversation(req,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    user=req.user
    if item.created_by==user:
        redirect('core:index')
    conversations=Conversation.objects.filter(members__in=[req.user.id]).filter(item=item)
    if conversations:
        pass
    if req.method=='POST':
        form = MessageForm(req.POST)
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(req.user)
            conversation.members.add(item.created_by)
            conversation.save()

            message=form.save(commit=False)
            message.conversation=conversation
            message.created_by=req.user
            message.save()

            return redirect('item:details',pk=item_pk)
    else:
        form=MessageForm()
        return render(req,"conversations/new.html",{
            "form":form
        })
    
def inbox(req):
    conversations=Conversation.objects.filter(members__in=[req.user.id])
    return render(req,"conversations/inbox.html",{"conversations":conversations})



def chat(req, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    messages = conversation.messages.all()
    
    if req.method == 'POST':
        form = MessageForm(req.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = req.user
            message.save()
            return redirect('conversations:chat', pk=pk)
    else:
        form = MessageForm()
    
    return render(req, "conversations/chat.html", {
        "form": form,
        "msgs": messages
    })
