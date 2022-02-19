from pyexpat import model
from rest_framework import serializers
from leads.models import *


class LeadSerializer(serializers.ModelSerializer):

    image_path = serializers.SerializerMethodField()
    def get_image_path(self,lead):
        return lead.image.url

    class Meta:
        model = Lead
        fields = ["id","name","email","message","image_path","image"]
        extra_kwargs = {
            "owner":{
                "required":False
            },
            "name":{
                "required":True
            },
            "email":{
                "required":True
            },
            "message":{
                "required":True
            },
            "image":{
                "write_only":True
            }
        }
        