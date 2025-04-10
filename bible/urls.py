from django.urls import path

from .api import *

urlpatterns = [
    path('versions/', VersionList.as_view(), name='version-list'),
    path('versions/<int:version_id>', VersionDetail.as_view(), name='version-detail'),
]