from django.db import transaction
from rest_framework import viewsets

from api.serializers import LetterSerializer, PackageSerializer
from posts.models import Letter, Package


@transaction.atomic
class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


@transaction.atomic
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
