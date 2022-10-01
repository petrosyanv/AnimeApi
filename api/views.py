from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Anime, Rating
from api.serializers import AnimeSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    @action(detail=True, methods=['POST'])
    def rate_anime(self, request, pk=None):
        if 'stars' in request.data:
            anime = Anime.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user  # to not provide access unauthorithed user
            #user = User.objects.get(id=1)
            print('user', user.username)
            try:
                rating = Rating.objects.get(user=user.id, anime=anime.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating updated", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.get(user=user, anime=anime, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating created", 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': "You need to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        response = {'message': "You can not create rating in that way"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': "You can not update rating in that way"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
