from rest_framework.pagination import LimitOffsetPagination


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    """Paginate only when limit/offset params are explicitly provided."""

    def paginate_queryset(self, queryset, request, view=None):
        has_limit = 'limit' in request.query_params
        has_offset = 'offset' in request.query_params
        if not has_limit and not has_offset:
            return None
        return super().paginate_queryset(queryset, request, view)
