# Класс Клиент - представляет покупателя магазина
class Client:
    def __init__(self, id, name):
        # id клиента
        self.id = id
        # имя клиента
        self.name = name
        # расстояние от клиента до склада в километрах
        self.distance = 0