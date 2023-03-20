from rest_framework.response import Response
from app.serializer import CategorySerializer, EntryFieldSerializer, EntryFieldPutSerializer, CategoryPutSerializer
from app.models import Category, EntryField
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoryView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    def get(self, request):
        objs = Category.objects.all()
        serializer = CategorySerializer(objs, many=True)
        return Response(serializer.data)

class CategoryPost(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = CategoryPutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryPut(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404
            
    def put(self, request, pk):
        data = request.data
        obj = Category.objects.get(id=pk)
        print(obj)
        serializer = CategoryPutSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
class EntryFieldView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        objs = EntryField.objects.all()
        serializer = EntryFieldSerializer(objs, many=True)
        return Response(serializer.data)

class EntryFieldPost(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = EntryFieldPutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class EntryFieldPut(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return EntryField.objects.get(id=pk)
        except EntryField.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        data = request.data
        obj = self.get_object(pk)
        serializer = EntryFieldPutSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
