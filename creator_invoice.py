from datetime import date
from invoice import Invoice, Item

class CreatorInvoice(object):

    def __init__(self) -> None:
        super().__init__()

        self.__social_name = None
        self.__cnpj = None
        self.__emission_date = None
        self.__details = None
        self.__itens = None

    def social_name(self, social_name:str) -> object:
        self.__social_name = social_name
        return self

    def cnpj(self, cnpj:str) -> object:
        self.__cnpj = cnpj
        return self

    def emission_date(self, emission_date:date) -> object:
        self.__emission_date = emission_date
        return self

    def details(self, details:str) -> object:
        self.__details = details
        return self

    def itens(self, itens) -> object:
        self.__itens = itens
        return self

    def constructor(self):

        if self.__social_name is None:
            raise Exception("Social name must be informed!")
        if self.__cnpj is None:
            raise Exception("CNPJ must be informed!")
        if self.__itens is None:
            raise Exception("Itens must be informed!")
        if self.__emission_date is None:
            raise Exception("Emission date must be informed!")

        return Invoice(social_name=self.__social_name, 
                    cnpj=self.__cnpj, 
                    itens=self.__itens, 
                    emission_date=self.__emission_date, 
                    details=self.__details)
