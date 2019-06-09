from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Topics
from .serializers import TopicsSerializer


# Create your views here.

class TopicsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class TopicsViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    pagination_class = TopicsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('userid', 'title')
    ordering_fields = ('created_date',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
