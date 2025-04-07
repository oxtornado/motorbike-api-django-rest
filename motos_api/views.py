from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Moto
from .serializers import MotoSerializer


# Create your views here.
class MotoListApiView(APIView):
    """
    List all motos
    """
    def get(self, request):
        motos = Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new moto
        """
        data = {
            'trademark': request.data.get('trademark'),
            'model': request.data.get('model'),
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MotoDetailApiView(APIView):
    """
    Retrieve, update or delete a moto instance.
    """
    def get_object(self, moto_id):
        try:
            return Moto.objects.get(id=moto_id)
        except Moto.DoesNotExist:
            return None

    def get(self, request, moto_id):
        moto = self.get_object(moto_id)
        if moto is None:
            return Response({"error": "Moto not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MotoSerializer(moto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, moto_id):
        moto = self.get_object(moto_id)
        if moto is None:
            return Response({"error": "Moto not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MotoSerializer(moto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, moto_id):
        moto = self.get_object(moto_id)
        if moto is None:
            return Response({"error": "Moto not found"}, status=status.HTTP_404_NOT_FOUND)
        
        moto.delete()
        return Response({"message": "Moto deleted successfully"}, status=status.HTTP_204_NO_CONTENT)