from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView

from django.conf import settings
from sparkpost import SparkPost
from slackclient import SlackClient

from .forms import TestChamberApplicationForm
# Create your views here.
class CreateTestChamberApplicationView(FormView):
    form_class = TestChamberApplicationForm
    template_name = 'index.html'
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
    success_url = reverse_lazy('submission-success')

    def form_valid(self, form):
        email = SparkPost(settings.SPARKPOST_API_KEY)
        slack = SlackClient(settings.SLACK_TOKEN)

        sub_data = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email_address'],
            'idea_description': form.cleaned_data['idea_description'],
        }
        if form.cleaned_data['idea_needs']:
            sub_data['idea_needs'] = form.cleaned_data['idea_needs']
        if form.cleaned_data['idea_resources']:
            sub_data['idea_resources'] = form.cleaned_data['idea_resources']
        if form.cleaned_data['attended_event']:
            sub_data['attended_event'] = 'yes'
        if form.cleaned_data['staffed_event']:
            sub_data['staffed_event'] = 'yes'
        if form.cleaned_data['contact_me']:
            sub_data['contact_me'] = 'yes'
        if form.cleaned_data['slack_invite']:
            sub_data['slack_invite'] = 'yes'

        email.transmissions.send(
            recipients=[form.cleaned_data['email_address']],
            template='maglabs-test-chamber-submission-acknowledge',
            substitution_data=sub_data
        )
        email.transmissions.send(
            recipient_list='maglabs-research-team',
            template='maglabs-test-chamber-submission-notification',
            substitution_data=sub_data
        )
        slack.api_call(
            'chat.postMessage',
            channel=settings.SLACK_CHANNEL,
            text='New Show Application: %s from %s &lt;%s&gt;' % (sub_data['show_name'], sub_data['name'], sub_data['email']),
            username=settings.SLACK_USERNAME
        )
        return super(CreateTestChamberApplicationView, self).form_valid(form)

class SubmissionSuccessView(TemplateView):
    template_name = 'success.html'