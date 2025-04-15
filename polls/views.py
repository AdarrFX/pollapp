from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from .models import Poll, Option, VoteTracking
import logging

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

class LoginView(LoginView):
    template_name = "polls/login.html"  # Your login template

def index(request):
    activepolls = Poll.objects.all()
    polls_with_vote_status = []  # Store polls with vote status
    for poll in activepolls:
        if request.user.is_authenticated:
            poll.user_has_voted = VoteTracking.objects.filter(user=request.user, poll=poll).exists()
        else:
            poll.user_has_voted = False  # Default to False if user is not logged in

        # build the structure containing the poll and whether the user has voted on it
        polls_with_vote_status.append({
        "poll": poll,
        "userHasVoted": poll.user_has_voted  # Store per poll
    })
    print("Request received:", request.method)
    return render(request, 'polls/index.html', { 'polls': polls_with_vote_status })

def about(request):
    return render(request, 'polls/register.html')

def thing(request):
    return render(request, 'polls/register.html')

# def active_polls(request):
#     active_polls = Poll.objects.all()
#     print("Request received:", request.method)
#     for poll in active_polls:
#         poll.user_has_voted = VoteTracking.objects.filter(user=request.user, poll=poll).exists()
#         logger.info(poll.user_has_voted)
#     return render(request, 'polls/poll.html')

@login_required
def voteOnOption(request):
    if request.method == 'POST':
        option_id = request.POST.get('option_id')
        poll_id = request.POST.get('poll_id')
        optionToVoteOn = get_object_or_404(Option, id=option_id)
        pollContainingOption = get_object_or_404(Poll, id=poll_id)
        user = request.user

        timeoutScript = "<script>setTimeout(function() {window.location.href = '/'}, 2000);</script>"

        # Check if the user already voted on this poll
        if VoteTracking.objects.filter(user=user, poll=pollContainingOption).exists():
            
            # Get the user's voted option
            voted_option = VoteTracking.objects.get(user=user, poll=pollContainingOption).option
            
            return HttpResponse(f"""<div>You already voted on: {pollContainingOption.question}. 
                Voted for option {voted_option.option_text}.</div>
                <a href='/'>Click here or wait to return.</a>
                {timeoutScript}
                """)  # Show error page if they already voted

        # Otherwise, add a vote
        # Register vote
        VoteTracking.objects.create(user=user, poll=pollContainingOption, option=optionToVoteOn)
        optionToVoteOn.votes += 1
        optionToVoteOn.save()

        return HttpResponse(f"""<div style='margin: 0'>Poll updated: {pollContainingOption.question}. 
        Voted for option {optionToVoteOn.option_text}.</div> <a href='/'>Click here or wait to return.</a>
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