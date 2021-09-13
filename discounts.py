from budget import Budget
import discounts

class DiscountFiveItens(object):

    def __init__(self, next_discount) -> None:
        super().__init__()

        self.__next_discount = next_discount

    def calculate(self, budget: Budget) -> float:

        if budget.total_itens > 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.calculate(budget)


class DiscountTotal500(object):
    def __init__(self, next_discount) -> None:
        super().__init__()

        self.__next_discount = next_discount

    def calculate(self, budget: Budget) -> float:

        if budget.value > 499:
            return budget.value * 0.7
        else:
            return self.__next_discount.calculate(budget)


class NoDiscount(object):

    def calculate(budget: Budget) -> float:
        return 0.0
