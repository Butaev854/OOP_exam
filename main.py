# Файл: main.py

from store import Store
def main():
    my_store = Store()

    # Добавляем клиентов
    my_store.add_client("Иван", 5)
    my_store.add_client("Мария", 10)
    my_store.add_client("Петр", 3)

    # Добавляем товары в магазин
    my_store.add_product("Обои")
    my_store.add_product("Штукатурка")

    # Создаём заказы:
    my_store.add_order(1, 1)
    my_store.add_order(2, 2)
    my_store.add_order(3, 1)

    # Получаем все заказы в радиусе 6 км от склада
    orders = my_store.get_orders_in_radius(6)

    # Открываем файл для записи
    with open("orders.txt", "w", encoding="utf-8") as f:
        f.write("Заказы в работе (радиус 6 км):\n")
        for order in orders:
            f.write(f"Заказ {order.id}: клиент {order.client_id}, товар {order.product_id}\n")
    print("Запись в файле orders.txt")

if __name__ == "__main__":
    main()