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

        self.__itens = []

    @property
    def value(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.value
        return total

    def get_itens(self) -> tuple:
        return tuple(self.__itens)

    @property
    def total_itens(self) -> int:
        return len(self.__itens)

    
    def add_item(self, item: Item) -> None:
        self.__itens.append(item)


