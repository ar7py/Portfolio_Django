from django.contrib import admin
from django.db import models
from django.db.models import fields
from pfapp import models
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ['email', 'subject', 'message']
    search_fields = ['email', 'subject']
    list_filter = ['email', 'subject']
    list_display = ['email', 'subject']


admin.site.register(Contact, ContactAdmin)
