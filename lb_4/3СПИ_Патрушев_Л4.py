class DeliveryStrategy:
    def calculate_cost(self, weight):
        pass


class CourierDelivery(DeliveryStrategy):
    def calculate_cost(self, weight):
        return 200 + weight * 50


class PostalDelivery(DeliveryStrategy):
    def calculate_cost(self, weight):
        return 100 + weight * 25


class DroneDelivery(DeliveryStrategy):
    def calculate_cost(self, weight):
        return 300 + weight * 10


class DeliveryContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_cost(self, weight):
        return self.strategy.calculate_cost(weight)


print("Выбери способ доставки:")
print("1 - Курьер (200 + 10 за кг)")
print("2 - Почта (100 + 5 за кг)")
print("3 - Дрон (300 + 15 за кг)")

choice = int(input("Твой выбор (1-3): "))
weight = float(input("Вес посылки (кг): "))

if choice == 1:
    strategy = CourierDelivery()
elif choice == 2:
    strategy = PostalDelivery()
elif choice == 3:
    strategy = DroneDelivery()
else:
    print("Неверный выбор!")
    exit()

delivery = DeliveryContext(strategy)
cost = delivery.calculate_cost(weight)

print(f"Стоимость доставки: {cost} руб")