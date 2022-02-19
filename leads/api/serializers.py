from pyexpat import model
from rest_framework import serializers
from leads.models import *


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id","name","email","message"]
        extra_kwargs = {
            "owner":{
                "required":False
            }
        }
        