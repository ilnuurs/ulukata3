from django.db.models import Q
from rest_framework import viewsets

from .pagination import StandardResultsSetPagination


class BaseCustomViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        search = request.query_params.get('search')
        if search and hasattr(self, 'search_fields'):
            q_object = Q()
            for field in self.search_fields:
                q_object |= Q(**{f"{field}__icontains": search})
            queryset = queryset.filter(q_object)


        if hasattr(self, 'filter_fields'):
            for field in self.filter_fields:
                val = request.query_params.get(field)
                if val is not None:
                    if isinstance(val, str):
                        val_lower = val.lower()
                        if val_lower in ['true', '1', 'yes']:
                            val = True
                        elif val_lower in ['false', '0', 'no']:
                            val = False
                    
                    queryset = queryset.filter(**{field: val})

      
        ordering = request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        elif hasattr(self, 'default_ordering') and self.default_ordering:
            queryset = queryset.order_by(self.default_ordering)

        return queryset