from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from .models import Poll, Option

class LoginView(LoginView):
    template_name = "polls/login.html"  # Your login template

def index(request):
    activepolls = Poll.objects.all()
    return render(request, 'polls/index.html', { 'polls': activepolls })

def about(request):
    return render(request, 'polls/register.html')

def thing(request):
    return render(request, 'polls/register.html')

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
            return redirect('index')  # Redirect to homepage or dashboard
        else:
            # IMPORTANT: If form is not valid, return the register page with errors
            return render(request, 'polls/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'polls/register.html', {'form': form})

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('index')  # Redirect to homepage