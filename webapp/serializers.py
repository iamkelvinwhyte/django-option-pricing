from rest_framework import serializers
from .models import MarketData
from .models import Option

class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketData
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    underlying = serializers.CharField(source='market_data.underlying', read_only=True)
    symbol = serializers.CharField(source='market_data.symbol', read_only=True)
    class Meta:
        model = Option
        fields = ('id', 'market_data', 'type', 'strike', 'pv','underlying','symbol')
        
class OptionValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ( 'market_data', 'type', 'strike')
