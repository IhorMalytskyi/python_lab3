from rest_framework.views import APIView
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer


class UserList(APIView):

	@staticmethod
	def get(request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return JsonResponse(serializer.data, safe=False)
