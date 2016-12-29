from django.http import JsonResponse
from rest_framework.views import APIView

from .models import SocialCredential
from .serializers import SocialCredentialSerializer


class SocialCredentialList(APIView):
	@staticmethod
	def get(request):
		social_credential_list = SocialCredential.objects.all()
		serializer = SocialCredentialSerializer(social_credential_list, many=True)
		return JsonResponse(serializer.data, safe=False)

	@staticmethod
	def post(request):
		serializer = SocialCredentialSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors)


class SocialCredentialDetail(APIView):
	@staticmethod
	def delete(request, social_credential_id):
		social_credential = SocialCredential.objects.filter(id=social_credential_id)
		if len(social_credential) == 0:
			return JsonResponse("No cred with id=" + social_credential_id, safe=False)

		social_credential.delete()
		return JsonResponse("Deleted", safe=False)

	@staticmethod
	def post(request):
		social_credential = SocialCredential.objects.get(id=request.data['id'])
		serializer = SocialCredentialSerializer(data=request.data)
		if serializer.is_valid():
			serializer.update(social_credential, request.data)
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors)
