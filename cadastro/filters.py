import django_filters
from .models import Reserva, Stand

class ReservaFilter(django_filters.FilterSet):
    nome_empresa = django_filters.CharFilter(lookup_expr='icontains')
    quitado = django_filters.BooleanFilter()
    data = django_filters.DateFilter(lookup_expr='icontains')
    stand__valor = django_filters.CharFilter()

    class Meta:
        model = Reserva
        fields = ('nome_empresa', 'quitado', 'data', 'stand__valor')
        
