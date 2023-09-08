from books import *
from client import *
from rentbook import *
import os

#najpierw książki, klient, reszta

def main_fun():
    os.chdir("library")
    print(' ')
    # addrembook(add,AUTHOR=Maciek Kowalski', TITLE = ['Podróże po Ameryce','jakis','jakis','jakis'], PAGES = ['350','324','jakis','jakis'],CREATED = ['2019-02-02','2019-01-04','jakis','jakis'] )
    # addrembook(remove,TITLE='Podróże po Ameryce')
    operation_on_client(client_delete('12'))
    operation_on_client(new_client_sign_up(kw1='sas'))




if __name__ == '__main__':
    main_fun()

## Example 1 - modules in python
## See example in calculator folder
## Example 2 - datatime module
# from datetime import date
# print(date.today())
###########################################
## Zapis/odczyt danych typ słownik do pliku
## Example 3 - load .csv file as dictionary
# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     for row in csv_reader:
#         print(row)

## more option, see info: https://docs.python.org/3/library/csv.html
################# Task
## Twoim zadaniem jest utworzenie pakietu obsługi
## nowych i aktualnych klientów w wypożyczalni książek
## oraz dostępnych zasobów. Administratorem w/w wypożyczlni
## jest biliotekarka, która świetnie zna pythona.
###############################################
############    Zasoby:
## Folder Library zawiera 3 pliki zawierające następujące dane:
## book.csv - dane książek
## address.csv - adres klientów
## customer.csv - dane osobowe klientów
################################################
############  Specyfikacja oprogramowania:
## Utwórz następujące moduły:
## 1. Moduł main - główny moduł, który administruje zasobami wypożyczalni
## musi zawierać:  def __main__()
## 2. Moduł obsługi książek zawierający 2 funkcje:
## funkcja 1: dodanie nowej książki do bazy (book.csv)
## funkcja 2: usuwanie książki do bazy opcje: wględem ID lub tytułu (book.csv)
##
## 3. Moduł obsługi klienta zawierający 4 funkcje
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Klient podaje swoje dane, nadawany jest klientowi losowy numer ID (3 cyfry))
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej przez klienta książki oraz
## data wypożyczenia a potem zwrotu książki
## funkcja 3: usuwanie danych klienta opcje: względem ID lub NAME
##
## 4. moduł wypożyczania książki przez użytkownika 2 funkcje
## funkcja 1: wypożyczenie książki lub kilku książek przez klienta
## funkcja 2: zwrot 1 książki przez klienta
##
## Jeśli skończyłeś zadanie, przyjmij rolę kolejnego programisty
## który dostał zadanie aktualizacji Twojego oprogramowania
## Nie modyfikując i nie zmieniając nazwy funkcji w module 4
# "funkcja 2: zwrot 1 książki przez klienta" napisz jej zawartość
## tak aby klient miał możliwość zwrotu dowolnej liczby książek

## WYMAGANIA:
## - możesz programować wyłącznie w paradygmacie funkcyjnym
## - utwórz funkcję wyższego rzędu
## - utwórz funkcję wielu zmiennych wejściowych
## - utwórz funkcję zagnieżdzoną
## - użyj dekoratora
## - wykonaj dokumentację dla conajmniej 1 funkcji, 1 modułu, pakietu
## - conajmniej dla 1 funkcji wykonaj obsługę wyjątku  (dotyczy modułów 2-4)

## WSKAZANIA:
## - możesz zwiększyć liczbę modułów
## - dla zapisu/odczytu daty oraz danych do bazy wykorzystaj odpowiednie pakiety


# 4. moduł wypożyczania książki przez użytkownika 2 funkcje
# funkcja 1: wypożyczenie książki lub kilku książek przez klienta
# funkcja 2: zwrot 1 książki przez klienta
