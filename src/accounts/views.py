from logging import raiseExceptions
from django.shortcuts import redirect, render, resolve_url
from requests import request
from rest_framework import viewsets
from yaml import serialize

from .models import CustomUser, cotisation, versement
from rest_framework import generics, permissions
from .serializers import CotisationSerializers, UserSerializer, VersementSerializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.
def my_view(request):
    ...
    return redirect('https://www.oarh.cg/')
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
   

class LoginAPI(KnoxLoginView,):
    permission_classes = (permissions.AllowAny,)
   

    def post(self, request, format=None,id=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
       
       
        return super(LoginAPI, self).post(request, format=None)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    filterset_fields =["email",]

class CotisationViewSet(viewsets.ModelViewSet): 
        queryset = cotisation.objects.all()
        serializer_class = CotisationSerializers
class VersementViewSet(viewsets.ModelViewSet): 
        queryset = versement.objects.all()
        serializer_class = VersementSerializers

