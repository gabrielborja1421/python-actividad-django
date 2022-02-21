from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# importación de modelos
from django.contrib.auth.models import User

# importación de serializadores
from register.serializers import RegisterSerializer

class PrimerRegisterView(APIView):
    
    permission_classes=[permissions.AllowAny]
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)