from django.urls import include, path
from rest_framework import routers

from .views import LetterViewSet, PackageViewSet

router = routers.DefaultRouter()
router.register(prefix='letters', viewset=LetterViewSet, basename='letters')
router.register(prefix='package', viewset=PackageViewSet, basename='package')

urlpatterns = [path('', include(router.urls))]
