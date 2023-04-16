from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MarketDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.market_data = {
            "symbol": "BRN",
            "expiry": "2023-11-30",
            "underlying": "ICE Brent Jan-24 Future",
            "spot_price": 80.00,
            "interest_rate": 0.02,
            "volatility": 0.20
        }

    def test_upload_market_data(self):
        url = reverse('upload_market_data')
        response = self.client.post(url, self.market_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_market_data(self):
        url = reverse('get_market_data')
        self.client.post(reverse("upload_market_data"), self.market_data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_calculate_option_price(self):
        option_data = {
            "market_data": 1,
            "type": "Call",
            "strike": 100.0
        }
        url = reverse('calculate_option_price')
        self.client.post(reverse("upload_market_data"), self.market_data)
        response = self.client.post(url, option_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['pv'], '0.60')

    def test_calculate_option_price_invalid_type(self):
        option_data = {
            "market_data": 1,
            "type": "But",
            "strike": 100.0
        }
        url = reverse('calculate_option_price')
        self.client.post(reverse("upload_market_data"), self.market_data)
        response = self.client.post(url, option_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid option type')
 
