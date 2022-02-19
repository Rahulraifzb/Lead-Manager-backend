from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class LoginAPIView(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            "token":token.key,
            "user_id":user.pk,
            "email":user.email
        })

class RegisterAPIView(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={"request":request})
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.objects.get_or_create(user=user)
            data = serializer.data
            data["token"]=token.key
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        request.user.auth_token.delete()
        return Response({"message":"Logout Successfully!"},status=status.HTTP_200_OK)

class UserDetailAPIView(generics.RetrieveAPIView):
  permission_classes = [
    IsAuthenticated,
  ]
  authentication_classes = (TokenAuthentication,)
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user