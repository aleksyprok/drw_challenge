"""
Congratulations on decoding the package correctly. More challenges await.
Today, we're pricing options with the classic Black Scholes formula.

Please follow the TODO's.
"""

from dataclasses import dataclass
import math
from scipy.stats import norm

@dataclass
class Option:
    """
    A class to represent an option.
    """
    ticker: str
    strike: float
    time_to_expiry: float
    volatility: float
    spot: float
    risk_free_rate: float
    def black_scholes_call_price(self) -> float:
        """
        Returns the price of a call option using the Black Scholes formula.

        Returns
        -------
        float
            The price of the call option.
        """
        d1 = (math.log(self.spot / self.strike) + (self.risk_free_rate + 0.5 * self.volatility ** 2) \
           * self.time_to_expiry) / (self.volatility * math.sqrt(self.time_to_expiry))
        d2 = d1 - self.volatility * math.sqrt(self.time_to_expiry)

        call_price = self.spot * norm.cdf(d1) \
                   - self.strike * math.exp(-self.risk_free_rate * self.time_to_expiry) * norm.cdf(d2)
        return call_price
    
    def black_scholes_put_price(self) -> float:
        ...


call = {
    "t": "DRW",
    "s": 90,
    "k": 100,
    "sigma": 0.4,
    "yte": 0.3,
    "rfr": 0.05
}

call_option = Option(
    ticker=call["t"],
    strike=call["k"],
    time_to_expiry=call["yte"],
    volatility=call["sigma"],
    spot=call["s"],
    risk_free_rate=call["rfr"]
)

print(f"The price of the call option is: {call_option.black_scholes_call_price():.2f}")

# TODO: 1. price the option package above, round to 2 decimal places.

# TODO: 2. what if the above option was a put instead?

# TODO: 3. Bonus: if you hold 3 such calls and 2 such puts, how much total delta
# do you have? Round final result to 3 decimals.
