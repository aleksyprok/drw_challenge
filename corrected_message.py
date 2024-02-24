"""
Congratulations on decoding the package correctly. More challenges await.
Today, we're pricing options with the classic Black Scholes formula.

Please follow the TODO's.
"""

# TODO: 0. we're missing some imports.

@dataclass
class Option:
    ticker: str
    strike: float
    time_to_expiry: float
    volatility: float
    spot: float
    risk_free_rate: float   
    def black_scholes_call_price(self) -> float:
        ... 
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

# TODO: 1. price the option package above, round to 2 decimal places.

# TODO: 2. what if the above option was a put instead?

# TODO: 3. Bonus: if you hold 3 such calls and 2 such puts, how much total delta do you have? Round final result to 3 decimals.
