from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    room = models.CharField(max_length=100)
    user = models.CharField(max_length=100,default="annonymous")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.room} - {self.user} , {self.content[:20]}"
    
    