from taxes import ICMS, ISS, ICPP, IKCV
from discounts import DiscountFiveItens, DiscountTotal500, NoDiscount
from budget import Budget


class DiscountCalculator(object):

    def calculate(self, budget: Budget, tax) -> float:

        discount = DiscountFiveItens(DiscountTotal500 (NoDiscount)).calculate(budget)

        return discount


if __name__ == '__main__':

    from budget import Budget, Item
    
    calculator = DiscountCalculator()
    budget = Budget()
    
    budget.add_item(Item("ITEM-1", 100))
    budget.add_item(Item("ITEM-2", 100))
    budget.add_item(Item("ITEM-3", 100))

    print("ISS e ICMS")
    discount = calculator.calculate(budget, ISS())
    discount = calculator.calculate(budget, ICMS())

    print("ICPP e IKCV")
    discount = calculator.calculate(budget, ICPP())
    discount = calculator.calculate(budget, IKCV())