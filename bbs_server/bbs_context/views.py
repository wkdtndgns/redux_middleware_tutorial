from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Type, Post, Memo
from .serializers import TypeSerializer, PostSerializer, MemoSerializer
from .utils import ListPagination

class TypeViewSet(viewsets.ModelViewSet) :
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class PostViewSet(viewsets.ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('type',)
    search_fields = ('title', 'context', 'writer',)
    ordering_fields = ('updated_at',)
    ordering = ('-updated_at',)
    pagination_class = ListPagination

class MemoViewSet(viewsets.ModelViewSet) :
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('title', 'context',)
    ordering_fields = ('updated_at',)
    ordering = ('-updated_at',)
    pagination_class = ListPagination