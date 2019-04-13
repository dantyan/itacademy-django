import django_filters

from forum.models import Post, Thread


class ThreadFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    pc_gt = django_filters.CharFilter(
        lookup_expr='gt', field_name='post_cnt'
    )
    less_then = django_filters.CharFilter(
        lookup_expr='lt', field_name='post_cnt'
    )

    foo = django_filters.CharFilter(method='filter_foo', field_name='post_cnt')

    class Meta:
        model = Thread
        fields = ['title', 'pc_gt', 'less_then', 'foo']

    def filter_foo(self, queryset, name, value):
        queryset = queryset.filter(
            post_cnt__lte=value
        )

        return queryset


class PostFilter(django_filters.FilterSet):
    thread = django_filters.ModelChoiceFilter(
        queryset=Thread.objects.all()
    )

    class Meta:
        model = Post
        fields = ['thread']
