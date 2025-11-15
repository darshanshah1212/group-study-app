from django.contrib import admin
from .models import ChatMessage

# Register your models here.

@admin.register(ChatMessage)
class MessageAdmin(admin.ModelAdmin):
    '''Admin View for Message'''
    
    list_display = ('room', 'user', 'content', 'timestamp')