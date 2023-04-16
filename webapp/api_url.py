from django.urls import path

from webapp.api_views import upload_market_data, get_market_data, calculate_option_price
from webapp import api_document as webapp_api_document

urlpatterns = [

    # Defined URL
    path('v1/marketdata/', upload_market_data, name='upload_market_data'),
    path('v1/marketdata/list/', get_market_data, name='get_market_data'),
    path('v1/optionprice/', calculate_option_price, name='calculate_option_price'),
    path('', webapp_api_document.schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    
]
handler404 = 'webapp.api_views.error_404_view'