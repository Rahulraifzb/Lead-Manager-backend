import email
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data["username"],email=validated_data["email"],password=validated_data["password"],first_name=validated_data["first_name"],last_name=validated_data["last_name"])

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","username","email"]