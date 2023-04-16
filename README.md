# Django Option Pricing 

The requirements are:

##  Project setup

    * git clone https://github.com/iamkelvinwhyte/django-option-pricing.git
    * python -m venv venv
    * pip install -r requirements.txt
    * python manage.py runserver
    * Navigate to http://127.0.0.1:8000/ to run API
   
## Sample data

### Market data sample
    {
    "symbol": "BRN",
    "expiry": "2023-11-30",
    "underlying": "ICE Brent Jan-24 Future",
    "spot_price": 80.00,
    "interest_rate": 0.02,
    "volatility": 0.20
    }
### Option data sample
    {
    "market_data": 1,
    "type": "Call",
    "strike": 100.0
    }
    

##  Project Test 
    cd to project 
    python manage.py test