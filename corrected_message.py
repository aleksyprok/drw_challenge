"""
Congratulations on decoding the package correctly. More challenges await.
Today, we're pricing options with the classic Black Scholes formula.

Please follow the TODO's.

Alex: Thank you for the message. I think I've done it. Here's the code.
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

    def d1(self) -> float:
        """
        Returns the d1 value used in the Black Scholes formula.

        Formula: d1 = (ln(S/K) + (r + 0.5 * sigma^2) * T) / (sigma * sqrt(T))
        
        Returns
        -------
        float
            The d1 value.
        """
        return (math.log(self.spot / self.strike) +
                (self.risk_free_rate + 0.5 * self.volatility ** 2) * self.time_to_expiry) / \
               (self.volatility * math.sqrt(self.time_to_expiry))

    def d2(self) -> float:
        """
        Returns the d2 value used in the Black Scholes formula.

        Formula: d2 = d1 - sigma * sqrt(T)

        Returns
        -------
        float
            The d2 value.
        """
        return self.d1() - self.volatility * math.sqrt(self.time_to_expiry)

    def black_scholes_call_price(self) -> float:
        """
        Returns the price of a call option using the Black Scholes formula.

        Formula: C = S * N(d1) - K * e^(-rt) * N(d2)

        Returns
        -------
        float
            The price of the call option.
        """
        return self.spot * norm.cdf(self.d1()) - \
               self.strike * math.exp(-self.risk_free_rate * self.time_to_expiry) * \
               norm.cdf(self.d2())

    def black_scholes_put_price(self) -> float:
        """
        Returns the price of a put option using the Black Scholes formula.

        Formula: P = Ke^(-rT)N(-d2) - S*N(-d1)

        Returns
        -------
        float
            The price of the put option.
        """
        return self.strike * math.exp(-self.risk_free_rate * self.time_to_expiry) * \
               norm.cdf(-self.d2()) - \
               self.spot * norm.cdf(-self.d1())

    def call_delta(self) -> float:
        """
        Returns the delta (dV/dS) of a call option using the Black Scholes formula.

        Formula: N(d1)

        Returns
        -------
        float
            The delta of the call option.
        """
        return norm.cdf(self.d1())

    def put_delta(self) -> float:
        """
        Returns the delta (dV/dS) of a put option using the Black Scholes formula.

        Formula: N(d1) - 1

        Returns
        -------
        float
            The delta of the put option.
        """
        return norm.cdf(self.d1()) - 1

    def total_delta(self, num_calls: int, num_puts: int) -> float:
        """	
        Returns the total delta of a portfolio of options.

        Parameters
        ----------
        num_calls : int
            The number of call options.
        num_puts : int
            The number of put options.
        
        Returns
        -------
        float
            The total delta of the portfolio.
        """
        return num_calls * self.call_delta() + num_puts * self.put_delta()

if __name__ == "__main__":

    # t = ticker
    # s = spot
    # k = strike
    # sigma = volatility
    # yte = years to expiry
    # rfr = risk free rate
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
    print(f"The price of the put option is: {call_option.black_scholes_put_price():.2f}")

    total_delta = call_option.total_delta(3, 2)
    print(f"The total delta for 3 calls and 2 puts is: {total_delta:.3f}")

    print(f"The delta of one call option is: {call_option.call_delta():.3f}")
    print(f"The delta of one put option is: {call_option.put_delta():.3f}")
