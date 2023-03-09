# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
x = sites['Moscow']
y = sites['London']
z = sites['Paris']
distances = {'Moscow': {'London':round(((x[0]-y[0])**2+(x[1]-y[1])**2)**.5),
                        'Paris':round(((x[0]-z[0])**2+(x[1]-z[1])**2)**.5)},
             'London': {'Moscow':round(((y[0]-x[0])**2+(y[1]-x[1])**2)**.5),
                         'Paris':round(((y[0]-z[0])**2+(y[1]-z[1])**2)**.5)},
              'Paris':{'London': round(((z[0]-y[0])**2+(z[1]-y[1])**2)**.5),
                         'Moscow':round(((z[0]-x[0])**2+(z[1]-x[1])**2)**.5)},
              }

# TODO здесь заполнение словаря

print(distances)
