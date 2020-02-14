from django.db import models

# Create your models here.
class MyQuestion (models.Model):
    question_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
class MyChoice (models.Model):
    question=models.ForeignKey(MyQuestion, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text