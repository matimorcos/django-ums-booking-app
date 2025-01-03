from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from users.serializers import LoginSerializer

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        """Return the login form."""
        serializer = self.serializer_class()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Process the login form."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            
            # Create or get a token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            # Return the token and a welcome message
            return Response(
                {"message": f"Welcome, {user.username}", "token": token.key},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
