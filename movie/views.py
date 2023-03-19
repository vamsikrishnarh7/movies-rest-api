from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializer import MovieSerializer

# Create your views here.
@api_view(['GET'])
def getMovie(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)