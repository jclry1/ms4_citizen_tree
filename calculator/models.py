from django.db import models

class faq(models.Model):
    question_name = models.CharField(max_length=50)
    question_answer = models.TextField()

    def __str__(self):
        return self.question_name
