# 3. Moduł obsługi klienta zawierający 4 funkcje
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Klient podaje swoje dane, nadawany jest klientowi losowy numer ID (3 cyfry))
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej przez klienta książki oraz
## data wypożyczenia a potem zwrotu książki
## funkcja 3: usuwanie danych klienta opcje: względem ID lub NAME
import random
import os
import pandas as pd
def new_client_sign_up(**kwargs):

    last_id = kwargs['ID'] if 'ID' in kwargs else list_of_books.iloc[-1]['ID'] + 1
    dataframe_to_add = {'ID': last_id,
                        'AUTHOR': kwargs['AUTHOR'],
                        'TITLE': kwargs['TITLE'],
                        'PAGES': kwargs['PAGES'],
                        'CREATED': kwargs['CREATED'],
                        'UPDATED': date.today()}
    return list_of_books._append(dataframe_to_add, ignore_index=True)


    print('1')
def client_delete(id_name):
    print('2')

def operation_on_client(lower_order_function):
    global list_of_addresses, list_of_customers
    list_of_addresses = pd.read_csv('address.csv')
    list_of_customer = pd.read_csv('customer.csv')
    lower_order_function

    list_of_addresses.to_csv('address.csv', index=False)
    list_of_customer.to_csv('customer.csv', index=False)


