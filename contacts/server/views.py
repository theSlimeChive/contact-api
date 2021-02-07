from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .serializers import ContactSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/contact-list/',
        'Detail': '/contact-detail/<str:pk>/',
        'Create': '/contact-create/',
        'Update': '/contact-update/<str:pk>/',
        'Delete': '/contact-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def list(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    contact = Contact.objects.get(id=pk)
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)