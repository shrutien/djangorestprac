from django import forms
from .models import Status
from django.core.exceptions import ValidationError

class StatusForm(forms.ModelForm):
	class Meta:
		model = Status
		fields= '__all__'


	def clean_content(self,*args,**kwargs):
		content = self.cleaned_data.get('content')
		if len(content) > 240:
			raise ValidationError('Content is too long.')
		return content

	def clean(self,*args,**kwargs):
		data = self.cleaned_data
		content = self.cleaned_data.get('content',None)
		image = self.cleaned_data.get('image',None)
		if content == "":
			content = None
		if content is None and image is None:
			raise ValidationError('Image or Content is Required.')

		return super().clean(*args,**kwargs)