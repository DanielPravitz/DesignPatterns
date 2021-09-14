from budget_states import InApproval


class Item(object):

    def __init__(self, name: str, value: float) -> None:
        super().__init__()

        self.__name = name
        self.__value = value

    @property
    def value(self) -> float:
        return self.__value

    @property
    def name(self) -> str:
        return self.__name


class Budget(object):

    def __init__(self) -> None:
        super().__init__()

        self.current_state = InApproval()
        self.__itens = []
        self.__extra_discount = 0.0

    @property
    def extra_discount(self) -> float:
        return self.__extra_discount

    @property
    def value(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.value
        return total - self.__extra_discount

    @property
    def total_itens(self) -> int:
        return len(self.__itens)

    def get_itens(self) -> tuple:
        return tuple(self.__itens)

    def add_item(self, item: Item) -> None:
        self.__itens.append(item)

    def apply_extra_discout(self) -> None:
        self.current_state.apply_extra_discount(self)

    def add_extra_discount(self, discount: float) -> None:
        self.__extra_discount += discount

    def approve(self):
        self.current_state.aprove(self)

    def reprove(self):
        self.current_state.reprove(self)

    def finish(self):
        self.current_state.finish(self)

if __name__ == '__main__':
    budget = Budget()

    budget.add_item(Item("ITEM-1", 100))
    budget.add_item(Item("ITEM-2", 50))
    budget.add_item(Item("ITEM-3", 400))

    print(budget.value)

    budget.approve()
    budget.approve()
   

    print(budget.value)
