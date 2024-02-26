from rest_framework import viewsets

from api.serializers import LetterSerializer
from posts.models import Letter


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
