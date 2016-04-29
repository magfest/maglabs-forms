from django.conf.urls import patterns, include, url

from .views import CreateTestChamberApplicationView, SubmissionSuccessView

urlpatterns = [
    url(r'^$', CreateTestChamberApplicationView.as_view(), name='application-submit'),
    url(r'^success/', SubmissionSuccessView.as_view(), name='submission-success')
]