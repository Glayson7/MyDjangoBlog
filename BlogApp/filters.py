import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    author__username = django_filters.CharFilter()

    class Meta:
        model = Post
        fields = ["title", "author__username", "categories"]
