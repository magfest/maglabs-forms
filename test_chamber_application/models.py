from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestChamberApplication(models.Model):
    name = models.CharField(
        verbose_name='Name',
        help_text='Give us a name that we can use to call you by',
        error_messages={'required': 'Please enter your name'},
        max_length=25)
    email_address = models.EmailField(
        verbose_name='Email',
        help_text='Give us an e-mail address we can use to get in touch with you',
        error_messages={'required': 'Please enter a valid e-mail address'})
    attended_event = models.BooleanField(
        default=False,
        verbose_name="I've been to a MAGFest event before")
    staffed_event = models.BooleanField(
        default=False,
        verbose_name="I've staffed a MAGFest event before")
    contact_me = models.BooleanField(
        default=False,
        verbose_name="I'd prefer not to be contacted by people interested in helping",
        help_text="If you do not check this box, people expressing interest in your event will be instructed to contact you via email.")
    slack_invite = models.BooleanField(
        default=False,
        verbose_name="Please send me an invite to the MAGFest Slack instance to coordinate with other volunteers/staff")
    idea_description = models.TextField(
        verbose_name="Describe your idea",
        help_text="Briefly describe your idea, what it offers attendees, and how you plan to implement it",
        error_messages={'required': 'You must submit a description'})
    idea_needs = models.TextField(
        verbose_name="What do you need to make your idea happen?",
        help_text="Please list any resources (volunteers, equipment, space, power, etc) you need to execute your idea",
        blank=True)
    idea_resources = models.TextField(
        verbose_name="What do you already have to make this happen?",
        help_text="Please list any resources you currently have, or will have, that will help you execute your idea",
        blank=True)
