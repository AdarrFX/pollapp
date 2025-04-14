from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Poll, Option

def index(request):
    activepolls = Poll.objects.all()
    return render(request, 'polls/index.html', { 'polls': activepolls })

def about(request):
    return render(request, 'polls/about.html')

def active_polls(request):
    active_polls = Poll.objects.all()
    return render(request, 'polls/poll.html')

def voteOnOption(request):
    if request.method == 'POST':
        option_id = request.POST.get('option_id')
        poll_id = request.POST.get('poll_id')
        optionToVoteOn = get_object_or_404(Option, id=option_id)
        pollContainingOption = get_object_or_404(Poll, id=poll_id)

        # Add a vote
        optionToVoteOn.votes += 1
        optionToVoteOn.save()

        timeoutScript = "<script>setTimeout(function() {window.location.href = '/'}, 2000);</script>"

        return HttpResponse(f"""Poll updated: {pollContainingOption.question}. 
        Voted for option {optionToVoteOn.option_text}
        {timeoutScript}
        """)

def register(request):
    # https://www.pythontutorial.net/django-tutorial/django-registration/
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("home")  # Redirect to homepage or dashboard
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})