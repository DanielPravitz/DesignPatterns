from datetime import date


class Item(object):
    def __init__(self, description: str, value: float) -> None:
        super().__init__()

        self.__description = description
        self.__value = value

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value


class Invoice(object):

    def __init__(self, social_name: str, cnpj: str, itens: list, emission_date: str = date.today(), details: str = "", observers=[]) -> None:
        super().__init__()

        self.__social_name = social_name
        self.__cnpj = cnpj
        self.__emission_date = emission_date
        self.__details = details
        self.__itens = itens

        for observer in observers:
            observer(self)

    @property
    def social_name(self):
        return self.__social_name

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def emssion_date(self):
        return self.__emission_date

    @property
    def details(self):
        return self.__details

    @property
    def itens(self):
        return self.__itens


if __name__ == '__main__':
    from creator_invoice import CreatorInvoice
    from observers import prints, send_by_email, save_database

    itens = [Item("Item-A", 100), Item("Item-B", 200)]

    invoice_by_builder = CreatorInvoice().social_name("FHSA Limited").emission_date(
        date.today()).cnpj("123456").itens(itens).constructor()

    invoice = Invoice(social_name="LTDA", cnpj="123", itens=itens, emission_date=date.today())