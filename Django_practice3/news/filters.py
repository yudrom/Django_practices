import django_filters
from news import models


class NewsFilter(django_filters.FilterSet):
    is_published = django_filters.BooleanFilter()
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()
    class Meta:
        model = models.News
        exclude = ('photo', )
