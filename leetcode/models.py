import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Solution(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    solution_code = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.solution_code