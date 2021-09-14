from discounts import DiscountFiveItens, DiscountTotal500, NoDiscount
from budget import Budget


class DiscountCalculator(object):

    def calculate(self, budget: Budget) -> float:

        discount = DiscountFiveItens(DiscountTotal500 (NoDiscount)).calculate(budget)

        return discount


if __name__ == '__main__':

    from budget import Budget, Item
    
    calculator = DiscountCalculator()
    budget = Budget()
    budget.add_item(Item("ITEM-1", 100))
    budget.add_item(Item("ITEM-2", 100))
    budget.add_item(Item("ITEM-3", 100))

    
    discount = calculator.calculate(budget)

    print(f"Calculated discount:{discount}")
