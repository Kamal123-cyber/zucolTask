from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20)
    series = models.IntegerField()

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer
