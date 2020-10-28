import django_filters
from django_filters import FilterSet, RangeFilter
from django_filters.widgets import RangeWidget, SuffixedMultiWidget
from .models import Estate


class PriceRangeWidget(RangeWidget):
     def __init__(self, min_attrs=None, max_attrs=None, attrs=None):
        super(PriceRangeWidget, self).__init__(attrs)

        if min_attrs:
            self.widgets[0].attrs.update(min_attrs)
        if max_attrs:
            self.widgets[1].attrs.update(max_attrs)

class EstateFilter(django_filters.FilterSet):
    
    price = RangeFilter(widget=PriceRangeWidget(
        min_attrs={'placeholder':'Mínimo'},
        max_attrs={'placeholder':'Máximo'},
    ))

    class Meta:
        model = Estate
        fields = ['business', 'structure', 'price']
