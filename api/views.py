from django.shortcuts import render
from rest_framework import generics
from tform.models import TForm, Email
from .serializers import TFormSerializer, EmailSerializer

# Create your views here.

class TFormAPIView(generics.ListAPIView):
    queryset = TForm.objects.all()
    serializer_class = TFormSerializer


class TFormUserDetailView(generics.RetrieveAPIView):
    queryset = TForm.objects.all()
    serializer_class = TFormSerializer


class TFormCreate(generics.ListCreateAPIView):
    queryset = TForm.objects.all()
    serializer_class = TFormSerializer


class AdminEmail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
