"""
Name:
    client

Description:
    Moduł client jest odpowiedzialny za zarządzanie klientem oraz jego danymi

Functions:
    operation_on_client(lower_order_function, **kwargs) - funkcja nadrzędna, odczytuje dataframes oraz zapisuje do pliku
    client_delete(**kwargs) - usuwa dane klienta, zwraca listę z df_of_customers i df_of_addresses
    change_existing_data(**kwargs) - modyfikuje dane klienta, zwraca listę z df_of_customers i df_of_addresses
    new_client_sign_up(**kwargs) - dodaje nowego klienta, zwraca listę z df_of_customers i df_of_addresses

"""
import random
import os
import pandas as pd
from datetime import date
from globals import PATH
from itertools import product

df_of_customers = pd.DataFrame()
df_of_addresses = pd.DataFrame()


def operation_on_client(lower_order_function, **kwargs):
    global df_of_addresses, df_of_customers
    df_of_addresses = pd.read_csv(PATH + 'address.csv')
    df_of_customers = pd.read_csv(PATH + 'customer.csv')
    lists = lower_order_function(**kwargs)
    lists[0].to_csv(PATH + 'customer.csv', index=False)
    lists[1].to_csv(PATH + 'address.csv', index=False)


def delete_info_from_books(id_of_client):
    df_of_books = pd.read_csv(PATH + 'book.csv')
    f = open(PATH + 'DATABASE/' + str(id_of_client))
    list_of_rented_books = f.read().split(',')
    list_of_rented_books.remove('')
    f.close()
    for id_of_rented_book in list_of_rented_books:
        df_of_books.loc[df_of_books['ID'] == int(id_of_rented_book), 'UPDATE'] = date.today()
    df_of_books.to_csv(PATH + 'book.csv', index=False)


def client_delete(**kwargs):
    '''
    Funkcja odpowiedzialna za usuwanie klienta.

        Args:
            **kwargs(string): Argumenty z nazwą w formie słownika

        Kwargs:
            ID (str): ID klienta
            NAME(str): Imię i nazwisko klienta

        Raises:
            KeyError: Wystąpi kiedy użytkownik nie poda ID oraz NAME w kwargsach
            FileNotFoundError: Wystąpi kiedy plik użytkownika nie został utworzony

        Returns:
            list: Lista w której znajdują się dwa zaaktualizowane DataFrame'y, df_of_customers oraz df_of_addresses
    '''
    global df_of_addresses
    if not ('ID' in kwargs or 'NAME' in kwargs):
        raise KeyError('Argumenty wejściowe są niepoprawne')
    if 'ID' in kwargs:
        id_of_client = [int(kwargs['ID'])]
    else:
        index_of_client = df_of_customers.loc[kwargs['NAME'] == df_of_customers['NAME']].index
        id_of_client = [df_of_customers.at[i, 'ID'] for i in index_of_client]
    question = str()
    for i in id_of_client:
        try:
            delete_info_from_books(i)
            os.remove(PATH + 'DATABASE/' + str(i))
        except FileNotFoundError as e:
            print('Plik użytkownika nie został utworzony: ' + e.filename)
        else:
            question = 'y'
        finally:
            if question is str():
                question = input('Czy aby na pewno chcesz usunąć dane użytkownika? (y/n)')
            match question:
                case 'y':
                    function_row_to_drop(i, df_of_customers)
                    function_row_to_drop(i, df_of_addresses)
                case 'n':
                    print('Dane nie zostaną usunięte')
                case _:
                    print('Odpowiedź niezgodna ze schematem, dane nie zostaną usunięte')
    return [df_of_customers, df_of_addresses]


def function_row_to_drop(id_to_drop, chosen_list):
    row_to_drop = chosen_list.loc[chosen_list['ID'] == id_to_drop].index
    return chosen_list.drop(row_to_drop, axis=0, inplace=True)


def change_existing_data(**kwargs):
    global df_of_customers, df_of_addresses
    if not (df_of_customers['ID'] == int(kwargs['ID'])).any():
        print('ID nie występuje w bazie danych, wpisz ponownie')
        return [df_of_customers, df_of_addresses]
    kwargs_tuple = list(kwargs.items())
    nazwy_kolumn = df_of_customers.columns.tolist()
    nazwy_kolumn.extend(df_of_addresses.columns.tolist())
    nazwy_kolumn = list(filter(lambda x: 'ID' not in x, nazwy_kolumn))
    nazwy_kolumn.remove('CREATED')
    is_something_changed = False
    for column, (key, value) in product(nazwy_kolumn, kwargs_tuple):
        if column.replace('-', '') == key:
            if column in df_of_customers.columns.tolist():
                df_of_customers = change_data(kwargs['ID'], column, value, df_of_customers)
            else:
                df_of_addresses = change_data(kwargs['ID'], column, value, df_of_addresses)
            is_something_changed = True
    if is_something_changed:
        df_of_customers = change_data(kwargs['ID'], 'UPDATED', date.today(), df_of_customers)
    return [df_of_customers, df_of_addresses]


def new_client_sign_up(**kwargs):
    list_of_ids = []
    for i in df_of_customers['ID']: list_of_ids.append(i)
    while True:
        id_client = str(random.choice(range(100, 1000)))
        if id_client not in list_of_ids: break
    print('Przydzielone id: '+id_client)
    save_to_file(id_client)
    dataframe_to_add_customer = {'ID': id_client,
                                 'NAME': kwargs['NAME'],
                                 'E-MAIL': kwargs['EMAIL'],
                                 'PHONE': kwargs['PHONE'],
                                 'CREATED': date.today(),
                                 'UPDATED': date.today()}
    dataframe_to_add_address = {'ID': id_client,
                                'STREET': kwargs['STREET'],
                                'CITY': kwargs['CITY'],
                                'COUNTRY': kwargs['COUNTRY']}
    return [df_of_customers._append(dataframe_to_add_customer, ignore_index=True),
            df_of_addresses._append(dataframe_to_add_address, ignore_index=True)]


def save_to_file(id_name):
    if not os.path.exists(PATH + 'DATABASE'):
        os.makedirs(PATH + 'DATABASE')
    with open(PATH + 'DATABASE/' + id_name, 'w') as f:
        f.close()


def change_data(id_of_client, column, value, chosen_list):
    row_to_change = chosen_list.loc[chosen_list['ID'] == int(id_of_client)].index
    chosen_list.loc[row_to_change, column] = value
    return chosen_list
