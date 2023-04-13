# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
sd.resolution = (1200, 600)

starting_point = sd.Point(600, 0)

def draw_branches(cur_point, cur_angle, cur_length):
    if cur_length < 10:
        return None

    first_vector = sd.get_vector(cur_point, cur_angle, cur_length)
    second_vector = sd.get_vector(cur_point, cur_angle, cur_length)
    first_vector.draw()
    second_vector.draw()
    
    exit_point_1 = first_vector.end_point

    next_vector = cur_length * (sd.random_number(60, 90) / 100)

    draw_branches(exit_point_1, cur_angle + sd.random_number(18, 42), next_vector)
    draw_branches(exit_point_1, cur_angle - sd.random_number(18, 42), next_vector)

start_vector = sd.get_vector(starting_point, 90, 100)
start_vector.draw()

draw_branches(start_vector.end_point, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
