from django.contrib import admin

# Register your models here.
from .models import TestChamberApplication

class TestChamberApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'attended_event', 'staffed_event', 'contact_me', 'slack_invite')

admin.site.register(TestChamberApplication, TestChamberApplicationAdmin)
