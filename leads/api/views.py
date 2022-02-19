from rest_framework import generics
from rest_framework import mixins
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from leads.utils import *

class LeadListCreateAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = LeadSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    # throttle_classes = [UserRateThrottle]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['name', 'email']
    search_fields = ["id","name","email","owner__id"]
    ordering_fields = ['id', 'name',"email","owner"]
    # pagination_class = CustomPageNumberPagination
    # queryset = Lead.objects.all().order_by("-created_at")
    

    def get_queryset(self):
        return Lead.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        print(" ---- requested data ---- ",request.data)
        return self.create(request, *args, **kwargs)

class LeadDeatilUpdateDestroyAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = LeadSerializer
    # queryset = Lead.objects.all().order_by("-created_at")
    
    

    def get_queryset(self):
        return Lead.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)