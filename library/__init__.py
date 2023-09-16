'''
Name:
    library

Description:
    Pakiet służy do obsługi biblioteki

Package contains:
    address.csv
    customer.csv
    book.csv
    client(module)
    books(module)
    rentbooks(module)
    globals(module)

'''
from books import addrembook, add, remove
from client import operation_on_client, change_existing_data, new_client_sign_up, client_delete
from rentbook import rentbooks, returnbook
