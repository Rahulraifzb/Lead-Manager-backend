from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [ 
    path("",LeadListCreateAPIView.as_view(),name="lead-list"),
    path("<str:pk>/",LeadDeatilUpdateDestroyAPIView.as_view(),name="lead-detail"),
]