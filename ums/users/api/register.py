from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializers import RegisterSerializer

class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        """Returns the registration form."""
        serializer = self.serializer_class()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Processes the registration form."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Asumiendo que `save` crea el usuario
            return Response(
                {"message": f"User {user.username} created successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)