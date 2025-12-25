from client import Client
from product import Product
from order import Order


# Главный класс Магазин - управляет всей системой
class Store:
    def __init__(self):
        self.clients = []
        self.products = []
        self.orders = []
        self.next_id = 1

    # Метод для добавления нового клиента
    def add_client(self, name, distance):
        client = Client(self.next_id, name)
        client.distance = distance
        self.clients.append(client)
        self.next_id += 1
        return client

    # Метод для добавления нового товара
    def add_product(self, name):
        product = Product(self.next_id, name)
        self.products.append(product)
        self.next_id += 1
        return product

    # Метод для создания нового заказа
    def add_order(self, client_id, product_id):
        order = Order(self.next_id, client_id, product_id)
        self.orders.append(order)
        self.next_id += 1
        return order

    # Метод для получения заказов в определенном радиусе от склада
    def get_orders_in_radius(self, radius):
        result = []

        for order in self.orders:
            for client in self.clients:
                if client.id == order.client_id and client.distance <= radius:
                    result.append(order)

        # Возвращаем список заказов
        return result