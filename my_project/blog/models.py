from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #User is a default table provided by Djano Authentication Model

class Post(models.Model):  #Post is Table Name. Django ORM allows us to create Tables in Object Oriented Format.
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #when an instance of Post model is created, the date_posted attribute will be configured with current date and time.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if a user who created the post gets deleted, it will delete the post as well (Viceversa is not true)
    
    
    def __str__(self):
        return self.title


