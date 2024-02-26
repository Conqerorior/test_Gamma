from rest_framework import viewsets

from api.serializers import LetterSerializer, PackageSerializer
from posts.models import Letter, Package


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
