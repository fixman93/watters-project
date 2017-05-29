from rest_framework import serializers
from .models import Dress



class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        depth = 2