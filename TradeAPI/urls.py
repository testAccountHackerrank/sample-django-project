from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from API.views import *

urlpatterns = [
    url(r'^trading/traders$', TraderSearchView.as_view()),
    url(r'^trading/traders/(?P<trader_id>[\w]+)$', TraderIDView.as_view()),
    url(r'^trading/stocks$', StocksDataView.as_view()),
    url(r'^trading/stocks/(?P<symbol>[\w]+)$', StocksSymbolView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
