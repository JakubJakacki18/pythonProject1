import pandas as pd
from datetime import date


def add(**kwargs):
    # dataframe_to_add = {}
    # for author,title,pages,created in kwargs['AUTHOR'],kwargs['TITLE'],kwargs['PAGES'],kwargs['CREATED']:
    #     last_id = list_of_books.iloc[-1]['ID'] + 1
    #     # last_id if 'ID' in last_id else
    #     dataframe_to_add.update({'ID': last_id,
    #                         'AUTHOR': author,
    #                         'TITLE': title,
    #                         'PAGES': pages,
    #                         'CREATED': created,
    #                         'UPDATED': date.today()})
    # for key,val in kwargs.items():
    #     print(key,val)

    last_id = kwargs['ID'] if 'ID' in kwargs else list_of_books.iloc[-1]['ID'] + 1
    dataframe_to_add = {'ID': last_id,
                        'AUTHOR': kwargs['AUTHOR'],
                        'TITLE': kwargs['TITLE'],
                        'PAGES': kwargs['PAGES'],
                        'CREATED': kwargs['CREATED'],
                        'UPDATED': date.today()}
    return list_of_books._append(dataframe_to_add, ignore_index=True)


def addrembook(lower_order_function, **kwargs):
    global list_of_books
    list_of_books = pd.read_csv('book.csv')
    list_of_books = lower_order_function(**kwargs)
    list_of_books.to_csv('book.csv', index=False)


def remove(**kwargs):
    if 'ID' or 'TITLE' in kwargs:
        if 'ID' in kwargs:
            id_of_book = int(kwargs['ID'])
            row_to_drop = list_of_books.loc[list_of_books['ID'] == id_of_book].index
        else:
            row_to_drop = list_of_books.loc[list_of_books['TITLE'] == kwargs['TITLE']].index
        list_of_books.drop(row_to_drop, axis=0, inplace=True)
        return list_of_books



#     kwargs = {'lista_a': [1, 2, 3], 'lista_b': [4, 5, 6], 'lista_c': [7, 8, 9]}
#     funkcja(**kwargs)
# def funkcja(**kwargs):
#     for key, value in kwargs.items():
#         if isinstance(value, list):
#             for i, item in enumerate(value):
#                 # Tworzymy zmienne o nazwach złożonych z klucza i indeksu
#                 var_name = f"{key}_{i + 1}"
#                 locals()[var_name] = item
#                 print(f"{var_name}: {item}")