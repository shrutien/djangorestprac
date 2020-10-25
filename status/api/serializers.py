from rest_framework import serializers
from status.models import Status 
from django.core.exceptions import ValidationError

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = '__all__'
		read_only_field = ['user']

	def validate_content(self,content):
		if len(content) > 500:
			raise ValidationError('content is too long!')
		return content

	def validate(self,data):
		content = data.get("content",None)
		if content == "":
			content = None
		image = data.get('image',None)
		if content is None and image is None:
			raise ValidationError('image Or content is required')
		return data