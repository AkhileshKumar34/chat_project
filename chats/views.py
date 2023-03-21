from django.shortcuts import render,redirect
from .models import Thread,ChatMessage
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse

User = get_user_model()

def home(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    
    return render(request, 'chats/index.html',context)

def send(request):
    user_id = request.POST['user_id']
    thread_id = request.POST['thread_id']
    msg = request.POST['message']

    user = User.objects.filter(id=user_id).first()
    thread = Thread.objects.filter(id=thread_id).first()

    ChatMessage.objects.create(thread=thread, user=user, message=msg)
    return HttpResponse("Hi, Message Sent Successfully!!")