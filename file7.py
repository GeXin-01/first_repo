
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import math
@dataclass
class FinancialInstrument(ABC):

    symbol: str
    current_price: float

@abstractmethod
def calculate_value(self) -> float:
     pass
@dataclass
class option(FinancialInstrument):
     strike_price: float
     time_to_maturity: float
     risk_free_rate: float
     volatility: float
     implied_volatility: float = field(default=0.0, init=False)

     def set_implied_volatility(self, value:float) -> None:
          if value < 0:
               