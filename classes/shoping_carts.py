# 3. Класс для управления корзиной покупок
# В классе ShoppingCart добавить функционал, чтобы при вызове get_details выводилась
# информация, например, ("покупатель такой-то приобрел то-то, "
# общая сумма, зарегистрировал покупки пользователь админ").


class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
#    def __init__(self): Первоначальное состояние

    def __init__(self, customer, admin):
        self.customer = customer
        self.admin = admin
        self.items = []

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total



    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f"{self.customer.get_details()}\n" #Добавлено
        details += "Корзина покупок:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общее: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки пользователь {self.admin.get_details()}" #Добавлено
        return details


