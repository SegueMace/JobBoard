from django.contrib import admin
from .models import ConversationMessage, Userprofile

# Register your models here.
admin.site.register(ConversationMessage)
admin.site.register(Userprofile)
