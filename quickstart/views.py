from asyncio import tasks
import imp
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from quickstart import serializers


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/tast-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create View' : '/task-create/',
        'Update View' : '/task-update/',
        'Delete View' : '/task-delete/',
    }

    return Response(api_urls)

def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):

    """ API endpoint that allows users to be viewed or edited. """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    """ API endpoint that allows groups to be viewed or edited. """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]