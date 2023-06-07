# mypy: disallow-untyped-defs
from decimal import Decimal


class Calculator:
    """
    Initialize an instance of the calculator.
    :type value: float
    :param value: Initial value

    """

    def __init__(self, value: float = 0) -> None:
        self.__state: Decimal = Decimal(value)

    def add(self, value: float) -> float:
        """
        Add the given number to the value stored in the calculator

        :param value: numeric value
        :type: float
        :return: result of the operation which is stored in the calculator object
        :rtype: float
        """
        self.__state += Decimal(value)
        return self.value

    def sub(self, value: float) -> float:
        """
        Subtract the given number from the value stored in the calculator

        :param value: numeric value
        :type: float
        :return: result of the operation which is stored in the calculator object
        :rtype: float
        """
        self.__state -= value
        return self.value

    def div(self, value: float) -> float:
        """
        Divide the value stored in the calculator by the given number

        :param value: numeric value
        :type: float
        :return: result of the operation which is stored in the calculator object
        :rtype: float
        """
        self.__state /= Decimal(value)
        return self.value

    def mult(self, value: float) -> float:
        """
        Multiply the value stored in the calculator by the given number

        :param value: numeric value
        :type: float
        :return: result of the operation which is stored in the calculator object
        :rtype: float
        """
        self.__state *= Decimal(value)
        return self.value

    def root(self, value: float = 2) -> float:
        """
        Take the nth root of the value stored in the calculator,
        if no n is given the square root will be taken.

        :param value: numeric value
        :type: float
        :return: result of the operation which is stored in the calculator object
        :rtype: float
        """
        self.__state = self.__state ** (1 / Decimal(value))
        # # return self.__state
        # div = Decimal(1) / n
        # self.__state = self.__state.exp(div)
        return self.value

    def clear(self) -> None:
        """
        Reset the current value stored in the calculator and set it to 0
        """

        self.__state = 0

    @property
    def value(self) -> float:
        return float(self.__state)
