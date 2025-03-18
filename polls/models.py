from django.db import models

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
