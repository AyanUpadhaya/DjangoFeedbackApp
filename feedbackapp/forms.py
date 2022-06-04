from django.forms import ModelForm

from .models import Feedback


class CreateFeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['name','email','feedback']

