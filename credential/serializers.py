from rest_framework import serializers
from .models import SocialCredential
from user.models import User


class SocialCredentialSerializer(serializers.ModelSerializer):

	class Meta:
		model = SocialCredential
		fields = '__all__'

	def update(self, instance, validated_data):
		instance.user_name = validated_data.get('user_name', instance.user_name)
		instance.user = User.objects.get(id=validated_data.get('user', instance.user))
		instance.password = validated_data.get('password', instance.password)
		instance.email = validated_data.get('email', instance.email)
		instance.phone_number = validated_data.get('phone_number', instance.phone_number)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		self.instance = instance
		return instance
