# Товары в магазине
product = {
    1: {'Продукт': 'Ноутбук', 'Цена': 500},
    2: {'Продукт': 'АЙФОН', 'Цена': 1500},
    3: {'Продукт': 'Видео карта', 'Цена': 1200}
}

# Корзина
cart = {}

#  отображения товаров
def display_product():
    print('Приветствую в магазине')
    print('Список товаров:')
    for product_id, product_info in product.items():
        print(f"{product_id}. {product_info['Продукт']} - ${product_info['Цена']}")

#  товары в корзине
def add_to_cart(product_id, quantity):
    if product_id in product:
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        print(f"Добавлено {quantity} шт. {product[product_id]['Продукт']} в корзину.")
    else:
        print('Нет данного товара')

#отображения корзины
def display_cart():
    if not cart:
        print('Корзина пуста.')
    else:
        print('Корзина:')
        total = 0
        for product_id, quantity in cart.items():
            product_info = product[product_id]
            cost = product_info['Цена'] * quantity
            total += cost
            print(f"{product_info['Продукт']} - {quantity} шт. x ${product_info['Цена']} = ${cost}")
        print(f"Итого: ${total}")

# цикл программы
def shop():
    while True:
        display_product()
        choice = input("Введите номер товара для добавления в корзину (или 'q' для выхода): ")

        if choice == 'q':
            break

        if choice.isdigit():
            product_id = int(choice)
            if product_id in product:
                quantity = input("Введите количество: ")
                if quantity.isdigit():
                    quantity = int(quantity)
                    if quantity > 0:
                        add_to_cart(product_id, quantity)
                    else:
                        print("Количество должно быть больше нуля.")
                else:
                    print("Пожалуйста, введите корректное количество.")
            else:
                print("Такого товара нет в магазине.")
        else:
            print("Пожалуйста, введите корректный номер товара.")

        display_cart()

# Запуск программы
if __name__ == '__main__':
    shop()


