from django_filters import rest_framework as filters
from .models import Service

class ServiceFilter(filters.FilterSet):
    creation_date = filters.DateFilter(field_name="creation_date", lookup_expr="exact")
    delivery_date = filters.DateFilter(field_name="delivery_date", lookup_expr="exact")
    service_unit_price = filters.NumberFilter(field_name="service_unit_price", lookup_expr="exact")
    client_name = filters.CharFilter(field_name="client_name", lookup_expr="icontains")
    client_phone = filters.CharFilter(field_name="client_phone", lookup_expr="exact")
    service_type = filters.CharFilter(field_name="service_type", lookup_expr="icontains")
    service_description = filters.CharFilter(field_name="service_description", lookup_expr="icontains")
    amount_service = filters.NumberFilter(field_name="amount_service", lookup_expr="exact")

    class Meta:
        model = Service
        fields = ["creation_date","delivery_date","service_unit_price", "client_name","client_phone","service_type","service_description","amount_service"]