from django.shortcuts import render,redirect
from .models import Thread

def home(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'chats/index.html',context)
