from rest_framework import viewsets

from api.serializers import LetterSerializer
from posts.models import Letter


class LetterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    pagination_class = None
