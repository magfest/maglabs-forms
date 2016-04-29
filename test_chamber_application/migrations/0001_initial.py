# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestChamberApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'Please enter your name'}, help_text='Give us a name that we can use to call you by', max_length=25, verbose_name='Name')),
                ('email_address', models.EmailField(error_messages={'required': 'Please enter a valid e-mail address'}, help_text='Give us an e-mail address we can use to get in touch with you', max_length=254, verbose_name='Email')),
                ('attended_event', models.BooleanField(default=False, verbose_name="I've been to a MAGFest event before")),
                ('staffed_event', models.BooleanField(default=False, verbose_name="I've staffed a MAGFest event before")),
                ('contact_me', models.BooleanField(default=False, help_text='If you do not check this box, people expressing interest in your event will be instructed to contact you via email.', verbose_name="I'd prefer not to be contacted by people interested in helping")),
                ('slack_invite', models.BooleanField(default=False, verbose_name='Please send me an invite to the MAGFest Slack instance to coordinate with other volunteers/staff')),
                ('idea_description', models.TextField(error_messages={'required': 'You must submit a description'}, help_text='Briefly describe your idea, what it offers attendees, and how you plan to implement it', verbose_name='Describe your idea')),
                ('idea_needs', models.TextField(blank=True, help_text='Please list any resources (volunteers, equipment, space, power, etc) you need to execute your idea', verbose_name='What do you need to make your idea happen?')),
                ('idea_resources', models.TextField(blank=True, help_text='Please list any resources you currently have, or will have, that will help you execute your idea', verbose_name='What do you already have to make this happen?')),
            ],
        ),
    ]
