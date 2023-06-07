# mypy: disallow-untyped-defs
import math
from typing import Union
from decimal import Decimal, getcontext


class Calculator:

    def __init__(self, value=0) -> None:
        self.__state: Decimal = Decimal(value)

    def add(self, value: Union[float, int]) -> float:
        self.__state += value
        return self.value

    def sub(self, value: Union[float, int]) -> float:
        self.__state -= value
        return self.value

    def div(self, value: Union[float, int]) -> float:
        self.__state /= value
        return self.value

    def mult(self, value: Union[float, int]) -> float:
        self.__state *= value
        return self.value

    def root(self, n: int = 2) -> float:
        self.__state = self.__state ** (1 / Decimal(n))
        # # return self.__state
        # div = Decimal(1) / n
        # self.__state = self.__state.exp(div)
        return self.value

    def clear(self) -> None:
        self.__state = 0

    @property
    def value(self) -> float:
        return float(self.__state)
