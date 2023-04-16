from decimal import Decimal, getcontext
import math
from datetime import datetime

getcontext().prec = 28

class OptionPricing:
    
    def __init__(self, market_data):
        self.spot_price =market_data.spot_price
        self.volatility =market_data.volatility
        self.interest_rate =market_data.interest_rate
        self.expiry =market_data.expiry

    def calculate_call_price(self, strike):
        """
        Calculates the price of a European call option using the Black76 model.
        
        Parameters:
        -----------
        strike : Decimal
            The strike price of the option.
            
        Returns:
        --------
        call_price : Decimal
            The calculated price of the call option.
        """
        t = self.calculate_time_to_expiry()
        d1 = self.calculate_d1(strike, t)
        d2 = d1 - self.volatility * Decimal(math.sqrt(float(t)))
        return self.spot_price * self.norm_cdf(d1) - strike * Decimal(math.exp(-self.interest_rate * t)) * self.norm_cdf(d2)

    def calculate_put_price(self, strike):
        """
        Calculates the price of a European put option using the Black76 model.
        
        Parameters:
        -----------
        strike : Decimal
            The strike price of the option.
            
        Returns:
        --------
        put_price : Decimal
            The calculated price of the put option.
        """
        t = self.calculate_time_to_expiry()
        d1 = self.calculate_d1(strike, t)
        d2 = d1 - self.volatility * Decimal(math.sqrt(float(t)))
        return strike * Decimal(math.exp(-self.interest_rate * t)) * self.norm_cdf(-d2) - self.spot_price * self.norm_cdf(-d1)

    def calculate_time_to_expiry(self):
        """
        Calculates the time to expiry of an option in years.
        
        Returns:
        --------
        time_to_expiry : Decimal
            The time to expiry of the option in years.
        """
        now = datetime.now().date()
        time_to_expiry = Decimal((self.expiry - now).days) / Decimal(365)
        return time_to_expiry

    def calculate_d1(self, strike, time_to_expiry):
        """
        Calculates the d1 parameter used in the Black76 model.
        
        Parameters:
        -----------
        strike : Decimal
            The strike price of the option.
        time_to_expiry : Decimal
            The time to expiry of the option in years.
            
        Returns:
        --------
        d1 : Decimal
            The calculated value of the d1 parameter.
        """
        d1 = (Decimal(math.log(self.spot_price / strike)) + (self.interest_rate + self.volatility ** 2 / Decimal(2)) * time_to_expiry) / (self.volatility * Decimal(math.sqrt(float(time_to_expiry))))
        return d1

    def norm_cdf(self, x):
        """
        Calculates the cumulative distribution function of a standard normal distribution.
        
        Parameters:
        -----------
        x : Decimal
            The value to calculate the CDF for.
            
        Returns:
        --------
        cdf : Decimal
            The calculated value of the CDF.
        """
        x_float = float(x)
        cdf= (Decimal(1) + Decimal(math.erf(x_float / Decimal(math.sqrt(2.0)).__float__()))) / Decimal(2)
        return cdf