from abc import ABCMeta, abstractmethod
from budget import Budget


class Tax(object):
    def __init__(self, tax= None) -> None:
        super().__init__()

        self.__tax = tax

    def calculate_another_tax(self, budget: Budget) -> float:
        if self.__tax is None:
            return 0

        return self.__tax.calculate(budget)

    @abstractmethod
    def calculate(self, budget: Budget) -> float:
        pass


class TaxCondicionalTemplate(Tax):
    __metaclass__ = ABCMeta

    def calculate(self, budget: Budget) -> float:
        if self.if_max_tax(budget):
            return self.max_tax(budget) + self.calculate_another_tax(budget)
        else:
            return self.min_tax(budget) + self.calculate_another_tax(budget)

    @abstractmethod
    def if_max_tax(self, object) -> bool:
        pass

    @abstractmethod
    def max_tax(self, object) -> float:
        pass

    @abstractmethod
    def min_tax(self, object) -> float:
        pass


class ISS(Tax):
    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.1 + self.calculate_another_tax(budget)


class ICMS(Tax):
    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.06 + self.calculate_another_tax(budget)


class ICPP(TaxCondicionalTemplate):
    def if_max_tax(self, budget: Budget) -> bool:
        return budget.value > 500

    def max_tax(self, budget: Budget) -> float:
        return budget.value * 0.07

    def min_tax(self, budget: Budget) -> float:
        return budget.value * 0.05


class IKCV(TaxCondicionalTemplate):

    def if_max_tax(self, budget: Budget):
        return budget.value > 500 and self.__more_than_100(budget)

    def max_tax(self, budget: Budget) -> float:
        return budget.value * 0.1

    def min_tax(self, budget: Budget) -> float:
        return budget.value * 0.06

    def __more_than_100(self, budget: Budget):
        for item in budget.get_itens():
            if item.value > 100:
                return True
        return False
