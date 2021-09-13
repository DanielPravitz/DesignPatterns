from budget import Budget
from taxes import ISS, ICMS

class taxes_calculator(object):

    def calculate(self, budget: Budget, tax ) -> None:
        
        return print(tax.calculate(budget.value))

if __name__ == '__main__':

    from budget import Budget

    calculate = taxes_calculator()
    budget = Budget(500)

    calculate.calculate(budget, ISS())

    calculate.calculate(budget, ICMS())