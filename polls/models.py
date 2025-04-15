from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=200)  # The poll question
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the poll is created

    def __str__(self):
        return self.question

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=100)  # Text for the poll option
    votes = models.IntegerField(default=0)  # Number of votes for this option

    def __str__(self):
        return f"{self.option_text} ({self.votes} votes)"

class VoteTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Track which user voted
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)  # Track which poll they voted in
    option = models.ForeignKey(Option, on_delete=models.CASCADE)  # Track their choice

    class Meta:
        unique_together = ("user", "poll")  # Prevents duplicate votes on the same poll