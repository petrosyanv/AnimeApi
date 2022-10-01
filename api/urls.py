from django.urls import path, include
from rest_framework import routers

from api.views import AnimeViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('anime', AnimeViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
