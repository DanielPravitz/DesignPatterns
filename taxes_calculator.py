from budget import Budget, Item
from taxes import ISS, ICMS, IKCV, ICPP

class taxes_calculator(object):

    def calculate(self, budget: Budget, tax) -> None:
        
        return print(tax.calculate(budget))

if __name__ == '__main__':

    from budget import Budget

    calculate = taxes_calculator()
    budget = Budget()

    budget.add_item(Item("ITEM-1", 100))
    budget.add_item(Item("ITEM-2", 100))
    budget.add_item(Item("ITEM-3", 100))

    print("ISS e ICMS")
    calculate.calculate(budget, ISS())
    calculate.calculate(budget, ICMS())

    print("ISS com ICMS")
    calculate.calculate(budget, ISS(ICMS()))
    
    print("IKCV e ICPP")
    calculate.calculate(budget, IKCV())
    calculate.calculate(budget, ICPP())