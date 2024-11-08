import json

def load_menu(file):
    with open(file,'r') as f:
        menu_list : dict = json.loads(f.read())
        f.close()
        return menu_list

class Restaurant:
    def __init__(self):                         # Початок роботи ресторану. Завантажити меню, створити пусті списки столиків і замовлень.
        pass

    def add_item_to_menu(self,name,price):      # Додати страву до меню, якщо її ще немає.
        pass

    def del_item_from_menu(self,name,price):    # Видалити страву з меню, якщо така є.
        pass

    def book(self,table,time):                  # Резервувати столик на певний час.
        pass

    def cancel_booking(self,table,time):        # Зняти резерв столика.
        pass

    def order_items(self,table,order_list):     # Створити нове замовлення.
        pass

    def fulfilled_order(self,table):            # Виконати перше замовлення для столика.
        pass

    def cancelled_order(self,table):            # Відмінити перше замовлення для столика.
        pass

    def __del__(self):                          # Зберегти меню для подальших запусків програми.
        pass
