#Observer pattern
#Used to execute multiples actions based of an event 

from invoice import Invoice, Item


def prints(invoice: Invoice) -> str:
    return f"Printing invoice {invoice.cnpj}"


def send_by_email(invoice: Invoice) -> str:
    return f"Sending  invoice {invoice.cnpj} by email!"


def save_database(invoice: Invoice) -> str:
    return f"Saving invoice {invoice.cnpj}"