from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalogue import serializers
from apps.catalogue.models import Dress


__all__ = ('DressList', )


class DressList(generics.ListAPIView):
    serializer_class = serializers.DressSerializer
    model = Dress
    queryset = model.objects.all()
