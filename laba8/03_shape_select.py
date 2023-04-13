# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
sd.resolution = (600, 600)

all_colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 5: sd.COLOR_CYAN, 6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}
name_of_colors = {1: 'красный', 2: 'оранжевый', 3: 'жёлтый', 4: 'зёленый', 5: 'сине-зеленый', 6: 'голубой', 7: 'фиолетовый'}
print("Список цветов:")
for color in name_of_colors.values():
    print(color)

name_of_figures = {1: 'треугольник', 2: 'квадрат', 3: 'пятиугольник', 4: 'шестиугольник'}
all_angles = {1: 120, 2: 90, 3: 72, 4: 60}
print("\nСписок цветов:")
for figure in name_of_figures.values():
    print(figure)

current_color = int(input('\nВведите номер цвета: '))

current_figure = int(input('Введите номер фигуры: '))

if current_color in all_colors:
    if current_figure in all_angles:
        point1 = sd.Point(250, 250)
        for i in range(0, 361, all_angles[current_figure]):
            v1 = sd.get_vector(start_point=point1, angle=i, length=100, width=3)
            v1.draw(all_colors[current_color])
            point1 = v1.end_point

sd.pause()
