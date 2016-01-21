import django_filters
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import filters
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')
