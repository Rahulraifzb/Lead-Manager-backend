from django.urls import path,include
from .views import *

urlpatterns = [ 
    path("login/",LoginAPIView.as_view(),name="login"),
    path("register/",RegisterAPIView.as_view(),name="register"),
    path("logout/",LogoutAPIView.as_view(),name="logout"),
    path("user-details/",UserDetailAPIView.as_view(),name="user-details"),
    path("api-auth/", include("rest_framework.urls")),  
]