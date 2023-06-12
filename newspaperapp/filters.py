import django_filters
from django_filters import FilterSet
from .models import Post, Category


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'dateCreation': ['gt'], 'title': ['icontains'], 'author__authorUser': ['exact']}


#class PostCategoryFilter(FilterSet):
#    postCategory = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), empty_label=None)
