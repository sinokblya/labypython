# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
stol_quantity = store[goods['Стол']][0]['quantity']
stol_quantity_1 = store[goods['Стол']][1]['quantity']
stol_price = store[goods['Стол']][0]['price']
stol_price_1 = store[goods['Стол']][1]['price']
stol_cost = stol_quantity*stol_price + stol_quantity_1*stol_price_1
print('Стол -', stol_quantity+stol_quantity_1, 'шт, стоимость', stol_cost, 'руб') 
divan_quantity = store[goods['Диван']][0]['quantity']
divan_quantity_1 = store[goods['Диван']][1]['quantity']
divan_price = store[goods['Диван']][0]['price']
divan_price_1 = store[goods['Диван']][1]['price']
divan_cost = divan_quantity*divan_price + divan_quantity_1*divan_price_1
print('Диван -', divan_quantity+divan_quantity_1, 'шт, стоимость', divan_cost, 'руб')
styl_quantity = store[goods['Стул']][0]['quantity']
styl_quantity_1 = store[goods['Стул']][1]['quantity']
styl_quantity_2 = store[goods['Стул']][2]['quantity']
styl_price = store[goods['Стул']][0]['price']
styl_price_1 = store[goods['Стул']][1]['price']
styl_price_2 = store[goods['Стул']][2]['price']
styl_cost = styl_quantity*styl_price + styl_quantity_1*styl_price_1+styl_quantity_2*styl_price_2
print('Стул -', styl_quantity+styl_quantity_1+styl_quantity_2, 'шт, стоимость', styl_cost, 'руб')