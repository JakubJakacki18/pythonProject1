import os
from functools import partial
import pandas as pd
from datetime import date
from globals import PATH

df_of_books = pd.DataFrame()


def return_more_than_one_book(function):
    def wrapper(*args):
        for i in args:
            function(i)
    return wrapper


def is_book_rented(id_of_rentbook, dict_item):
    for i in dict_item[-1]:
        if i == id_of_rentbook:
            return True
    return False


def who_rented_book(dictionary, id_of_rentbook):
    is_book_rented_with_arg = partial(is_book_rented, id_of_rentbook)
    people_with_rented_book = filter(is_book_rented_with_arg, dictionary.items())
    return dict(people_with_rented_book)


def check_files():
    dict_with_files = {key: None for key in os.listdir(PATH + 'DATABASE')}
    for file_name in dict_with_files:
        with open(PATH + 'DATABASE/' + file_name, 'r') as f:
            list_of_rented_books = f.read().split(',')
            dict_with_files[file_name] = list_of_rented_books
    return dict_with_files


def save_rented_books_to_file(id_client, list_of_books_to_rent):
    global df_of_books
    df_of_client = pd.read_csv(PATH + 'customer.csv')
    if (df_of_client['ID'] == int(id_client)).any():
        f = open(PATH + 'DATABASE/' + id_client, 'a')
        for id_of_rented_book in list_of_books_to_rent:
            f.write(',' + id_of_rented_book)
            df_of_books.loc[df_of_books['ID'] == int(id_of_rented_book), 'UPDATE'] = 'Rented by: ' + id_client
        f.close()


def rentbooks(id_client, *args):
    global df_of_books
    list_of_books_to_rent = []
    dict_with_files = check_files()
    df_of_books = pd.read_csv(PATH + 'book.csv')
    for id_of_rentbook in args:
        if who_rented_book(dict_with_files, id_of_rentbook) == dict() and (
                df_of_books['ID'] == int(id_of_rentbook)).any():
            list_of_books_to_rent.append(id_of_rentbook)
    if list_of_books_to_rent != list():
        save_rented_books_to_file(id_client, list_of_books_to_rent)
    df_of_books.to_csv(PATH + 'book.csv', index=False)


@return_more_than_one_book
def returnbook(id_of_book):
    global df_of_books
    try:
        df_of_books = pd.read_csv(PATH + 'book.csv')
    except FileNotFoundError as e:
        print('Nie znaleziono pliku: '+e.filename)
    else:
        person_which_rented_book = who_rented_book(check_files(), id_of_book)
        delete_book_from_file(person_which_rented_book.keys(), id_of_book)
        df_of_books.to_csv(PATH + 'book.csv', index=False)


def delete_book_from_file(key_client, id_of_book):
    global df_of_books
    try:
        id_client = list(key_client)[0]
    except IndexError:
        print(f'Słownik z użytkownikami jest pusty, książki z ID: {id_of_book} nikt nie wypożyczył')
    else:
        with open(PATH + 'DATABASE/' + id_client, 'r+') as f:
            list_of_rented_books = f.read().split(',')
            list_of_rented_books.remove(id_of_book)
            f.seek(0)
            f.write(','.join(list_of_rented_books))
            f.truncate()
        df_of_books.loc[df_of_books['ID'] == int(id_of_book), 'UPDATE'] = date.today()
