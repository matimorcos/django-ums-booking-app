from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import ProfileSerializer

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view using Postman or cURL commands

    def get(self, request):
        """Return the user's profile data."""
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)

    def post(self, request):
        """Allow users to update their profile data."""
        serializer = ProfileSerializer(request.user.profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
