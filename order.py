# Класс Заказ - представляет заказ в магазине
class Order:
    def __init__(self, id, client_id, product_id):
        # id заказа
        self.id = id
        # id клиента, который сделал заказ
        self.client_id = client_id
        # id товара, который заказали
        self.product_id = product_id
        # статус заказа: "в работе" или "выполнен"
        self.status = "в работе"