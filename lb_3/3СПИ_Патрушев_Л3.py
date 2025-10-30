class Transport:
    def move(self):
        pass


class Car(Transport):
    def move(self):
        return "Машина едет."


class Bicycle(Transport):
    def move(self):
        return "Велосипед колесит."


class Plane(Transport):
    def move(self):
        return "Самолет летит."


class TransportFactory:
    def create_transport(choice):
        if choice == 1:
            return Car()
        elif choice == 2:
            return Bicycle()
        elif choice == 3:
            return Plane()
        else:
            return None


print("Выбери: 1-Машина, 2-Велосипед, 3-Самолет")
choice = int(input("Твой выбор: "))

transport = TransportFactory.create_transport(choice)
if transport:
    print(transport.move())
else:
    print("Неверный выбор")





