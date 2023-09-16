import tkinter.messagebox
from tkinter.ttk import Combobox

from library import *
from tkinter import *
def main_fun():
    # addrembook(add,AUTHOR='Michał Wawrzyniak', TITLE = 'Na naszej wsi', PAGES = '240',CREATED = '2012-04-10')
    # addrembook(remove,TITLE='Podróże po Ameryce')
    # addrembook(remove,ID='102')
    # operation_on_client(new_client_sign_up,NAME='Tom1asz Mikucki',EMAIL='t.mikucki@o2.pl',PHONE='764359103',STREET='Kawaleryjska',CITY='Białystok',COUNTRY='Poland')
    # operation_on_client(client_delete,NAME='Natalia Nowicka')
    # operation_on_client(client_delete,ID='812')
    # rentbooks('821','103','102','122','200','211','232')
    # returnbook('101','102')
    # operation_on_client(change_existing_data,ID='226', PHONE='984985443')
    # open_window_to_remove_book()
    pass

chosen_option = 'ID'
def open_window_to_remove_book():
    window = Tk()
    window.title('Usuń książkę')
    window.geometry('480x270')

    Label(window, text='Wybierz dostępne opcje:', justify='center').grid(row=0, column=0, columnspan=2, pady=3)
    window.grid_columnconfigure(0,minsize=240)
    window.grid_columnconfigure(1,minsize=240)
    Label(window, text='Wprowadź wartość:').grid(row=2, column=0, sticky=E, padx=2)
    cb_choose = (Combobox(window,width=30,values=['ID','TITLE']))
    # cb_choose['values'] = 'ID','Tytuł'
    cb_choose.grid(row=1,column=0,columnspan=2)
    cb_choose.current(0)
    def combo_function(event):
        global chosen_option
        chosen_option=cb_choose.get()


    cb_choose.bind('<<ComboboxSelected>>',combo_function)
    cb_choose['state']='readonly'
    entry_value=Entry(window)
    entry_value.grid(row=2,column=1,pady=40,sticky=W,padx=2)
    def call_remove():
        string_input = f"addrembook(remove,{chosen_option}='{entry_value.get()}')"
        compiled_code = compile(string_input, '<string>', 'exec')
        exec(compiled_code)
        tkinter.messagebox.showinfo(title='Informacja',message='Funkcja została uruchomiona pomyślnie!')
    btn_delete_book = Button(window, text='Usuń książkę', width=20, command=call_remove)
    btn_delete_book.grid(row=3,columnspan=2)
    window.mainloop()


if __name__ == '__main__':
    main_fun()