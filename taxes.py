
from budget import Budget


class ISS(object):
    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.1


class ICMS(object):
    def calculate(self, budget: Budget) -> float:
        return budget.value * 0.06


class ICPP(object):
    def calculate(self, budget: Budget) -> float:
        if budget.value > 500:
            return budget.value * 0.07
        else:
            return budget.value * 0.05


class IKCV(object):
    def calculate(self, budget: Budget) -> float:
        if budget.value > 500 and self.__more_than_100():
            return budget.value * 0.1
        else:
            return budget.value * 0.06

    def __more_than_100(self, budget: Budget):
        for item in budget.get_itens():
            if item.value > 100:
                return True
        return False
