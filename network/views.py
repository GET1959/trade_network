from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from network.models import NetworkLink
from network.serializers import NetworkLinkSerializer


class NetworkLinkCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkLinkSerializer
    queryset = NetworkLink.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class NetworkLinkListAPIView(generics.ListAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer


class NetworkLinkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer


class NetworkLinkUpdateAPIView(generics.UpdateAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer


class NetworkLinkDestroyAPIView(generics.DestroyAPIView):
    queryset = NetworkLink.objects.all()
    serializer_class = NetworkLinkSerializer
