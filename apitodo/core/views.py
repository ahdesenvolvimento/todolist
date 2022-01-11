from django.http.response import Http404, JsonResponse
# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ListSerializer, UserGetSerializer, UsersSerializer
from rest_framework import serializers, status


from core.models import List, Users

# Create your views here.
def index(request):
    return JsonResponse({}, safe=False)

class ListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None): 
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ListDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        list = self.get_object(pk)
        list.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
            
class UserList(APIView):
    def get(self, request, format=None):
        user = Users.objects.all()
        serializer = UserGetSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        user = UsersSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return JsonResponse(user.data, safe=False, status=status.HTTP_201_CREATED)

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Users.objects.get(id=pk)
        except Users.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserGetSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return JsonResponse({}, safe=False, status=status.HTTP_200_OK)
    