LAB_SOURCE_FILE=__file__


def num_eights(x):
    """Возвращает количество восьмёрок в записи числа x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # в этом задании запрещено использовать оператор связывания
    >>> # используйте только рекурсию
    >>> check(LAB_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """

    "*** YOUR CODE HERE ***"
    if x % 10 == 8:
        return 1 + num_eights(x // 10)
    elif x < 10:
        return 0
    else:
        return num_eights(x // 10)
print(num_eights(888))


def pingpong(n):
    """Возвращает n-ый элемент пинг-понг последовательности.

    Пинг-понг последовательность начинается с 1.
    Следующий элемент получается прибавлением приращения к предыдущему.
    Начальное приращение: +1.
    Если номер элемента кратен 8 или содержит цифру 8 - знак приращения меняется (обозначено *):

    Номер   1	2	3	4	5	6	7	8*	9	10	11	12	13	14	15	16*	17	18*	19	20	21 ...

    Элемент 1	2	3	4	5	6	7	8*	7	 6	 5	 4	 3	 2	 1	 0*	 1	 2*	 1	 0	-1 ...

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # в этом задании запрещено использовать оператор связывания
    >>> # используйте только рекурсию
    >>> check(LAB_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def next_number(current, direction, i):
        if i == n:
            return current
        if i % 8 == 0 or has_eight(i):
            return next_number(current - direction, -direction, i+1)
        else:
            return next_number(current + direction, direction, i+1)

    def has_eight(k):
        if k % 10 == 8:
            return True
        elif k < 10:
            return False
        else:
            return has_eight(k // 10)

    return next_number(1, 1, 1)


def missing_digits(n):
    """Функция принимает число n, цифры которого стоят в порядке возрастания
    и возвращает количество пропущенных цифр в этом числе.
    >>> missing_digits(1248) # пропущены 3, 5, 6, 7
    4
    >>> missing_digits(1122) # нет пропущенных
    0
    >>> missing_digits(123456) # нет пропущенных
    0
    >>> missing_digits(3558) # пропущены 4, 6, 7
    3
    >>> missing_digits(35578) # пропущены 4, 6
    2
    >>> missing_digits(12456) # пропущена 3
    1
    >>> missing_digits(16789) # пропущены 2, 3, 4, 5
    4
    >>> missing_digits(19) # пропущены 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # между 4 и 4 нет пропущенных
    0
    >>> from construct_check import check
    >>> # нельзя использовать циклы
    >>> check(LAB_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_missing_digits(s, i):
        if i == len(s) - 1:
            return 0
        if s[i] == s[i + 1]:
            return count_missing_digits(s, i + 1)
        else:
            diff = int(s[i + 1]) - int(s[i])
            return diff - 1 + count_missing_digits(s, i + 1)

    s = str(n)
    return count_missing_digits(s, 0)


def next_largest_coin(coin):
    """Возвращает следующую монету.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # остальные возвращают None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Возвращает кол-во вариантов размена total используя монеты по 1, 5, 10, 25 коп.

    Например 15 коп. можно разменять так:
    - 15 монет по 1 коп.
    - 10 монет по 1 коп. + 1 монета 5 коп.
    - 5 монет по 1 коп. + 2 по 5 коп.
    - 5 монет по 1 коп. + 1 по 10 коп.
    - 3 монеты по 5 коп.
    - 1 монета 5 коп. + 1 монета 10 коп.
    Итого 6 вариантов.

    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # как можно разменять рубль (100 копеек)?
    242
    >>> from construct_check import check
    >>> # нельзя использовать циклы
    >>> check(LAB_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def count_helper(total, coins):
        if total == 0:
            return 1
        elif total < 0 or not coins:
            return 0
        else:
            return count_helper(total, coins[1:]) + count_helper(total - coins[0], coins)
    return count_helper(total, [1, 5, 10, 25])


from operator import sub, mul

def make_anonymous_factorial():
    """Возвращает выражение, которое вычисляет факториал.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # нельзя использовать связывание, рекурсивные вызовы, создавать свои функции
    >>> check(LAB_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
