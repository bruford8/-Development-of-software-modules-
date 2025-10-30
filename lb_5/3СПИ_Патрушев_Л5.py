class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата картой: {amount} руб"


class EWalletPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата электронными деньгами: {amount} руб"


class QRCodePayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата по QR-коду: {amount} руб"


class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        return f"Перевод на номер: {amount} руб"


class Platform:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        pass


class MobileAppPlatform(Platform):
    def make_payment(self, amount):
        result = self.payment_method.pay(amount)
        return f"Мобильное приложение: {result}"


class WebPlatform(Platform):
    def make_payment(self, amount):
        result = self.payment_method.pay(amount)
        return f"Веб-сайт: {result}"


print("Выбери способ оплаты:")
print("1 - Кредитная карта")
print("2 - Электронные деньги")
print("3 - QR-код")
print("4 - Перевод на номер")

payment_choice = int(input("Твой выбор (1-4): "))

print("\nВыбери платформу:")
print("1 - Мобильное приложение")
print("2 - Веб-сайт")

platform_choice = int(input("Твой выбор (1-2): "))

amount = float(input("Сумма оплаты: "))

if payment_choice == 1:
    payment = CreditCardPayment()
elif payment_choice == 2:
    payment = EWalletPayment()
elif payment_choice == 3:
    payment = QRCodePayment()
else:
    payment = BankTransferPayment()

if platform_choice == 1:
    platform = MobileAppPlatform(payment)
else:
    platform = WebPlatform(payment)

result = platform.make_payment(amount)
print(f"\n{result}")
