from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .option_pricing import OptionPricing
from .models import MarketData, Option
from .serializers import MarketDataSerializer, OptionSerializer,OptionValidateSerializer

@swagger_auto_schema(method='post', request_body=MarketDataSerializer, responses={
    201: openapi.Response('MarketData successfully created', MarketDataSerializer),
    400: 'Invalid request body'
})
@api_view(['POST'])
def upload_market_data(request):
    """
    API endpoint to upload market data.
    
    Parameters:
    -----------
    request : Request object
        The incoming request object containing the market data.
        
    Returns:
    --------
    response : Response object
        The response object containing the serialized market data if valid, or error messages if invalid.
    """
    serializer = MarketDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', responses={200: MarketDataSerializer(many=True)})
@api_view(['GET'])
def get_market_data(request):
    """
    API endpoint to get all market data.
    
    Parameters:
    -----------
    request : Request object
        The incoming request object.
        
    Returns:
    --------
    response : Response object
        The response object containing the serialized market data.
    """
    market_data = MarketData.objects.all()
    serializer = MarketDataSerializer(market_data, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=OptionValidateSerializer, responses={
    201: openapi.Response('Option successfully calculated', OptionSerializer),
    400: 'Invalid request body or option type'
})
@api_view(['POST'])
def calculate_option_price(request):
    """
    API endpoint to calculate the option price.
    
    Parameters:
    -----------
    request : Request object
        The incoming request object containing the option data.
        
    Returns:
    --------
    response : Response object
        The response object containing the serialized option if valid, or error messages if invalid.
    """
    serializer = OptionValidateSerializer(data=request.data)
    if serializer.is_valid():
        market_data = serializer.validated_data['market_data']
        option_type = serializer.validated_data['type']
        strike = serializer.validated_data['strike']
        OP = OptionPricing(market_data)
        try:
            if option_type == 'Call':
                price = OP.calculate_call_price(strike)
            elif option_type == 'Put':
                price = OP.calculate_put_price(strike)
            else:
                raise ValueError("Invalid option type")
            option = Option(market_data=market_data, type=option_type, strike=strike, pv=price)
            option.save()
            serializer = OptionSerializer(option)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def error_404_view(request, exception):
    """
    Handler for 404 errors.
    
    Parameters:
    -----------
    request : Request object
        The incoming request object.
    exception : Exception object
        The exception object that was raised.
        
    Returns:
    --------
    response : Response object
        The response object containing the 404 error message.
    """
    return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
