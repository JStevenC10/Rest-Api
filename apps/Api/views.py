from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CinemaSerializer, GenderSerializer, MovieListserializer,\
                        Movieserializer

class CinemaViewset(ModelViewSet):
    serializer_class = CinemaSerializer
    
    def get_queryset(self, pk=None):
        if pk == None:
            return self.serializer_class.Meta.model.objects.all()
        else:
            return self.serializer_class.Meta.model.objects.filter(pk=pk).first()

class GenderViewset(ModelViewSet):
    serializer_class = GenderSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return self.serializer_class.Meta.model.objects.all()
        else:
            return self.serializer_class.Meta.model.objects.filter(pk=pk).first()

class MovieViewset(ModelViewSet):
    serializer_class = Movieserializer
    list_serializer_class = MovieListserializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(state=True)
    
    # METHOD LIST MODIFIED FOR SEE MOVIE INFORMATION RESUME
    def list(self, request, *args, **kwargs):
        all_movies = self.serializer_class.Meta.model.objects.values('id', 'name', 'image', 'release_date', 'gender').filter(state=True)
        if all_movies:
            serializer = self.list_serializer_class(instance=all_movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {
                'message': 'Movies not founds!'
            }
            return JsonResponse(data=data)
    
    # METHOD DELETE MODIFIED FOR CHANGE  THE STATE OF MOVIE TO FALSE
    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        if movie:
            movie.state = False
            movie.save()
            data = {
                'message': 'The movie has been deleted'
            }
        else:
            data = {
                'Not found': 'Movie not found!'
            }
        return JsonResponse(data=data)

    