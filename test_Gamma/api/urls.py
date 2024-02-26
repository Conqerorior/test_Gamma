from django.urls import include, path
from rest_framework import routers

from .views import LetterViewSet

router = routers.DefaultRouter()
router.register(prefix='letter', viewset=LetterViewSet, basename='letter')

urlpatterns = [path('', include(router.urls))]
