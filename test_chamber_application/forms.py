from django.forms import ModelForm
from django.forms.widgets import TextInput, EmailInput, Select, Textarea, CheckboxInput

from .models import TestChamberApplication

class TestChamberApplicationForm(ModelForm):
    class Meta:
        model = TestChamberApplication
        fields = [
            'name',
            'email_address',
            'attended_event',
            'staffed_event',
            'contact_me',
            'slack_invite',
            'idea_description',
            'idea_needs',
            'idea_resources'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'field text medium'}),
            'email_address': EmailInput(attrs={'class': 'field text medium'}),
            'attended_event': CheckboxInput(attrs={'class':'field checkbox'}),
            'staffed_event': CheckboxInput(attrs={'class':'field checkbox'}),
            'contact_me': CheckboxInput(attrs={'class':'field checkbox'}),
            'slack_invite': CheckboxInput(attrs={'class':'field checkbox'}),
            'idea_description': Textarea(attrs={'class':'field textarea large'}),
            'idea_needs': Textarea(attrs={'class':'field textarea large'}),
            'idea_resources': Textarea(attrs={'class':'field textarea large'})
        }