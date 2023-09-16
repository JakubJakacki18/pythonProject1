import pandas as pd
from datetime import date
from globals import PATH

df_of_books = pd.DataFrame()


def add(**kwargs):
    id_of_client = kwargs['ID'] if 'ID' in kwargs else df_of_books.iloc[-1]['ID'] + 1
    dataframe_to_add = {'ID': id_of_client,
                        'AUTHOR': kwargs['AUTHOR'],
                        'TITLE': kwargs['TITLE'],
                        'PAGES': kwargs['PAGES'],
                        'CREATED': date.today(),
                        'UPDATED': date.today()}
    return df_of_books._append(dataframe_to_add, ignore_index=True)


def addrembook(lower_order_function, **kwargs):
    global df_of_books
    try:
        df_of_books = pd.read_csv(PATH+'book.csv')
    except FileNotFoundError as e:
        print('Nie znaleziono pliku: '+e.filename)
    else:
        df_of_books = lower_order_function(**kwargs)
        df_of_books.to_csv(PATH+'book.csv', index=False)


def remove(**kwargs):
    if 'ID' or 'TITLE' in kwargs:
        if 'ID' in kwargs:
            id_of_book = int(kwargs['ID'])
            row_to_drop = df_of_books.loc[df_of_books['ID'] == id_of_book].index
        else:
            row_to_drop = df_of_books.loc[df_of_books['TITLE'] == kwargs['TITLE']].index
        df_of_books.drop(row_to_drop, axis=0, inplace=True)
        return df_of_books
