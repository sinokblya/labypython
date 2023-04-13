# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 10

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


snowflakes = []

for _ in range(N):
    dict_of_snowflakes = {'length': sd.random_number(10, 100), 'x': sd.random_number(100, 1100), 'y': 600 + sd.randint(100, 150)}
    snowflakes.append(dict_of_snowflakes)
flag_of_stop = False

i = 1
sd.start_drawing()
while True:
    # sd.clear_screen()
    for snowflake in snowflakes:
        point_xy = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point_xy, color=sd.background_color, length=snowflake['length'])
        snowflake['x'] -= sd.random_number(-5, 15)
        snowflake['y'] -= sd.random_number(5, 30)
        point_xy = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point_xy, color=sd.COLOR_WHITE, length=snowflake['length'])
        if i % 40 == 0:
            new_snowflake = {'length': sd.random_number(10, 100), 'x': sd.random_number(100, 1100), 'y': 600 + sd.randint(100, 150)}
            snowflakes.append(new_snowflake)
        if snowflake['y'] < 50:
            snowflakes.remove(snowflake)
        i += 1
    
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

