from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PollQuestion(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    poll_name = models.CharField(max_length=122)
    que_text = models.TextField()
    que_image = models.ImageField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField(default=True)
    def __str__(self) :
        return str(self.id)

class Choice(models.Model):
    poll_question = models.ForeignKey(PollQuestion,on_delete=models.CASCADE)
    choice_text = models.TextField(null=True)
    choice_image = models.ImageField(null=True)
    votes = models.IntegerField(default=0)
    def __str__(self) :
        return str(self.id)
    

class Person(models.Model):    
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField()
    phone=models.BigIntegerField()
    email = models.EmailField()
    birthday=models.DateField()

    def __str__(self):
        return self.username
