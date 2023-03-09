# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Mama' , 'Sistra' , 'Papa' , 'I' , 'Dedywka']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Tatyana' , 170],
    ['Lubov', 172],
    ['Aleksey', 184],
    ['Ivan', 196],
    ['Anatoliy',180]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост:'+my_family[2]+' -', my_family_height[2][1],'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = 0
sum +=my_family_height[0][1]
sum +=my_family_height[1][1] 
sum +=my_family_height[2][1] 
sum +=my_family_height[3][1]  
sum +=my_family_height[4][1]
print('Общий рост моей семьи - ', sum ,'см') 