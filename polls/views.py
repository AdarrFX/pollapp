from django.shortcuts import render, redirect
from .models import Poll

def index(request):
    activepolls = Poll.objects.all()
    return render(request, 'polls/index.html', { 'activepolls': activepolls })

def about(request):
    return render(request, 'polls/about.html')

def poll(request):
    return render(request, 'polls/poll.html')

def voteOnOption(request):
    if request.method == 'POST':
        return redirect('/')
