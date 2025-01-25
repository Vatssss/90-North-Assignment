from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/index.html', {'users': users})

@login_required
def chat_room(request, username):
    user = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat/chat_room.html', {'other_user': user, 'messages': messages})
