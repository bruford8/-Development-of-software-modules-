from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def update(self, product):
        pass


class TechLover(Customer):
    def update(self, product):
        print(f"TechLover: О, новый товар в магазине — {product}!")


class BookLover(Customer):
    def update(self, product):
        print(f"BookLover: Хм, добавили {product}, интересно!")


class Store:
    def __init__(self):
        self.products = []
        self.subscribers = []

    def add_subscriber(self, customer):
        self.subscribers.append(customer)

    def remove_subscriber(self, customer):
        self.subscribers.remove(customer)

    def add_product(self, product):
        self.products.append(product)
        print(f"\nМагазин: Добавлен товар '{product}'")
        self.notify_subscribers(product)

    def notify_subscribers(self, product):
        for customer in self.subscribers:
            customer.update(product)


if __name__ == "__main__":
    store = Store()

    tech = TechLover()
    book = BookLover()

    store.add_subscriber(tech)
    store.add_subscriber(book)

    store.add_product("Макар")
    store.add_product("Никита")
