from django.urls import path

from network.apps import NetworkConfig
from network.views import (
    NetworkLinkCreateAPIView,
    NetworkLinkDestroyAPIView,
    NetworkLinkListAPIView,
    NetworkLinkRetrieveAPIView,
    NetworkLinkUpdateAPIView
)

app_name = NetworkConfig.name

urlpatterns = [
    path("links/", NetworkLinkListAPIView.as_view(), name="link-list"),
    path("links/<int:pk>/", NetworkLinkRetrieveAPIView.as_view(), name="link-retrieve"),
    path("links/create/", NetworkLinkCreateAPIView.as_view(), name="link-create"),
    path("links/<int:pk>/update/", NetworkLinkUpdateAPIView.as_view(), name="link-update"),
    path("links/<int:pk>/delete/", NetworkLinkDestroyAPIView.as_view(), name="link-delete"),
]
