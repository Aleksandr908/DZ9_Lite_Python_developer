# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цера: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."

# Для ДЗ Добавить новый тип продуктов (например, бытовая химия).

class HouseholdChemicals(Product):
    """
    Класс, представляющий бытовую химию, наследующий класс Product.
    """
    def __init__(self, name, price, concentration, hazard_class):
        super().__init__(name, price)
        self.concentration = concentration
        self.hazard_class = hazard_class

    def get_details(self):
        return (f"Бытовая химия: {self.name}, Концентрация: {self.concentration}, Класс опасности: {self.hazard_class}, Цена: {self.price} руб.")

