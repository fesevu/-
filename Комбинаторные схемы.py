from collections import Counter 

def factorial(beg, end): #нахождение факториала с помощью бин поиска
    if end < 0:
        print("Невозможно найти факториал меньше нуля")
        return -1
    elif end == 0 or end == 1 or beg > end:
        return 1
    elif (beg == end):
        return beg
    elif (end - beg == 1):
        return end * beg
    else:
        m = int((beg + end) / 2)
        return factorial(beg, m) * factorial(m + 1, end)

def perm_without_repeat(n): #перестановка без повторений
    return int(factorial (2, n))

def perm_without_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество перестановок без повторений
        (2) Пример задачи на перестановки без повторений
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            perm_without_repeat_opt(0)
            flag = 1
    
    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            n = int(input("Введите n для подсчёта по формуле перестановок без повторений P\u2099 = n!: "))
        except:
            print("Не правильный формат ввода")
            res = perm_without_repeat_opt(mode_in)
            flag = 1

        if flag == 0:    
            print("P\u2099 = " + str(perm_without_repeat(n)))

        if mode_in == 4:
            if res == 0:
                return perm_without_repeat(n)
            else:
                return res
    elif mode_in == 2:
        print("""
            Сколько n-значных чисел можно составить из n карточек с цифрами?
        """)

        try:
            n = int(input("Введите n: "))
        except BaseException:
            print("Не правильный формат ввода")
            perm_without_repeat_opt(2)
            flag = 1

        l = list(map(int, input("Введите через пробел " + str(n) + " цифр: ").split()))

        if n > len(l):
            print("Введено меньше " + str(n) + " цифр")
        elif n < len(l):
            print("Введено больше " + str(n) + " цифр")
        else:
            if 0 in l:
                print("Ответ: " + str(perm_without_repeat(n) - perm_without_repeat(n - 1)) + " чисел")
            else:
                print("Ответ: " + str(perm_without_repeat(n)) + " число(ел)")   
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет") 

    if flag == 0:
        perm_without_repeat_opt(0) 
    

def comb_without_repeat(n, r): #сочетаний без повторений
    return int(factorial(2, n) / (factorial(2, r) * factorial(2, n - r)))

def comb_without_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество сочетаний без повторений
        (2) Пример задачи на сочетания без повторений
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            comb_without_repeat_opt(0)
            flag = 1
    
    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            n, i = map(int, input("Введите n и i через пробел для подсчёта по формуле сочетаний без повторений C\u2099\u2071 = n!/(i! * (n - i)!): ").split())
        except BaseException:
            print("Не правильный формат ввода")
            res = comb_without_repeat_opt(mode_in)
            flag = 1

        if n < i:
            print("Введенное n меьше i")
            res = comb_without_repeat_opt(mode_in)
            flag = 1
        else:
            print("C\u2099\u2071 = " + str(comb_without_repeat(n, i)))
            
        if mode_in == 4:
                if res == 0:
                    return comb_without_repeat(n, i)
                else:
                    return res    
    elif mode_in == 2:
        print("""
        В шахматном турнире участвует n человек и каждый с каждым играет по одной партии. Сколько всего партий сыграно в турнире?
    """
        )

        try:
            n = int(input("Введите n: "))
        except BaseException:
            print("Не правильный формат ввода")
            comb_without_repeat_opt(2)
            flag = 1

        print("Ответ: " + str(comb_without_repeat(n, 2)) + " партия(й)")
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        comb_without_repeat_opt(0)
    
def plac_without_repeat(n, r): #размещение без повторений
    return int(factorial(2, n) / factorial(2, n - r))

def plac_without_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество размещений без повторений
        (2) Пример задачи на размещения без повторений
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            plac_without_repeat_opt(0)
            flag = 1

    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            n, i = map(int, input("Введите n и i через пробел для подсчёта по формуле размещений без повторений A\u2099\u2071 = n!/(n - i)!: ").split())
        except BaseException:
            print("Не правильный формат ввода")
            res = plac_without_repeat_opt(mode_in)
            flag = 1

        if n < i:
            print("Введенное n меьше i")
            res = plac_without_repeat_opt(mode_in)
            flag = 1
        else:
            print("A\u2099\u2071 = " + str(plac_without_repeat(n, i)))
            
        if mode_in == 4:
                if res == 0:
                    return plac_without_repeat(n, i)
                else:
                    return res    
    elif mode_in == 2:
        print("""
        В студенческой группе n человека. Сколькими способами можно выбрать старосту и его заместителя?
    """
        )

        try:
            n = int(input(print("Введите n: ")))
        except BaseException:
            print("Не правильный формат ввода")
            plac_without_repeat_opt(2)
            flag = 1

        print("Ответ: " + str(plac_without_repeat(n, 2)) + " способ(ов)")    
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        plac_without_repeat_opt(0)
    

def perm_with_repeat(arr): #перестановка с повторениями
    rep = list(Counter(arr).values())

    denominator = 1
    for i in range(len(rep)):
        denominator *= factorial(2, rep[i])

    return int(factorial(2, len(arr)) / denominator) 

def perm_with_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество перестановок с повторениями
        (2) Пример задачи на перестановки с повторений
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            perm_with_repeat_opt(0)
            flag = 1
    
    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            l = list(map(int, input("Введите через пробел элементы множества для подсчёта по формуле перестановок с повторениями по формуле P\u2099 = n! / (n\u2081!...n\u2096!): ").split()))
        except:
            print("Не правильный формат ввода")
            res = perm_with_repeat_opt(mode_in)
            flag = 1

        if flag == 0:    
            print("P\u2099 = " + str(perm_with_repeat(l)))

        if mode_in == 4:
            if res == 0:
                return perm_with_repeat(l)
            else:
                return res
    elif mode_in == 2:
        print("""
            Сколько различных буквосочетаний можно получить перестановкой карточек со следующими буквами: К, О, Л, О, К, О, Л, Ь, Ч, И, К?
        """)

        l = ["К", "О", "Л", "О", "К", "О", "Л", "Ь", "Ч", "И", "К"]

        print("Ответ: " + str(perm_with_repeat(l)) + " словосочетаний")
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет") 

    if flag == 0:
        perm_with_repeat_opt(0)
    

def comb_with_repeat(n, r): #сочетаний с повторениями
    return comb_without_repeat(n + r - 1, r)

def comb_with_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество сочетаний с повторениями
        (2) Пример задачи на сочетания с повторениями
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            comb_with_repeat_opt(0)
            flag = 1

    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            n, i = map(int, input("Введите n и i через пробел для подсчёта по формуле сочетаний с повторениями C\u2099\u2071 = (n + i - 1)!/(i! * (n - 1)!): ").split())
        except BaseException:
            print("Не правильный формат ввода")
            res = comb_with_repeat_opt(mode_in)
            flag = 1

        if flag == 0:
            print("C\u2099\u2071 = " + str(comb_with_repeat(n, i)))

        if mode_in == 4:
            if res == 0:
                return comb_with_repeat(n, i)
            else:
                return res
    elif mode_in == 2:
        print("""
        В кошельке находится большое количество n монет разного номинала. Сколькими способами можно извлечь k монеты из кошелька?
    """
        )

        try:
            n, k = map(int, input("Введите n и k через пробел: ").split())
        except BaseException:
            print("Не правильный формат ввода")
            comb_with_repeat_opt(2)
            flag = 1

        return print("Ответ: " + str(comb_with_repeat(n, k)) + " способ(ами)")
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        comb_with_repeat_opt(0)
    

def plac_with_repeat(n, r): #размещение c повторениями
    return int(n ** r)

def plac_with_repeat_opt(mode_in):
    flag = 0
    res = 0
    flag_in = 0
    if mode_in == 0 and mode_in != 4:
        print("""
        (1) Посчитать по формуле количество размещений с повторениями
        (2) Пример задачи на размещения с повторениями
        (3) Выход в главное меню
    """
        )

        flag_in = 1
        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            plac_with_repeat_opt(0)
            flag = 1

    if mode_in == 1 or (mode_in == 4 and flag_in == 0):
        try:
            n, i = map(int, input("Введите n и i через пробел для подсчёта по формуле размещений с повторениями A\u2099\u2071 = n\u2071: ").split())
        except BaseException:
            print("Не правильный формат ввода")
            res = plac_with_repeat_opt(mode_in)
            flag = 1

        if flag == 0:    
            print("A\u2099\u2071 = " + str(plac_with_repeat(n, i)))

        if mode_in == 4:
            if res == 0:
                return plac_with_repeat(n, i)
            else:
                return res
    elif mode_in == 2:
        print("""
        У Васи дома живут 4 кота. После завтрака любой кот может уйти гулять или остаться дома.
        Сколькими способам могут уйти гулять коты, если каждый из них может выйти на улицу, как через дверь, так и через окно?
    """
        )

        print("Ответ: " + str(plac_with_repeat(3, 4) - 1) + " способ(ов)")    
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        plac_with_repeat_opt(0)
    

def summ(mode_in):
    flag = 0
    res = 0
    if mode_in == 0:
        print("""
        (1) Посчитать по формуле сумму разных комбинаторных схем
        (2) Пример задачи на комбинаторную сумму
        (3) Выход в главное меню
    """
        )

        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            summ(0)
            flag = 1

    if mode_in == 1:

        action = {
            1: perm_without_repeat_opt,
            2: comb_without_repeat_opt,
            3: plac_without_repeat_opt,
            4: perm_with_repeat_opt,
            5: comb_with_repeat_opt,
            6: plac_with_repeat_opt,
        }

        print("""
        Выберите первое слагаемое
        (1) Перестановка без повторений
        (2) Сочетание без повторений
        (3) Размещение без повторений
        (4) Перестановка с повторениями
        (5) Сочетание с повторениями
        (6) Размещение с повторениями
    """
        )

        try:
            summand1 = int(input("Введите цифру соответсвующего выбора без скобок: "))
        except BaseException:
            print("Такого варианта нет")
            summ(1)
            flag = 1

        print("""
        Выберите второе слагаемое
        (1) Перестановка без повторений
        (2) Сочетание без повторений
        (3) Размещение без повторений
        (4) Перестановка с повторениями
        (5) Сочетание с повторениями
        (6) Размещение с повторениями
    """
        )

        try:
            summand2 = int(input("Введите цифру соответсвующего выбора без скобок: "))
        except BaseException:
            print("Такого варианта нет")
            summ(1)
            flag = 1

        try:
            summand1 = action[summand1](4)
            summand2 = action[summand2](4)

            print("Сумма равна " + str(summand1 + summand2))
        except BaseException:
            print()
    elif mode_in == 2:
        print("""
        Студенческая группа состоит из 23 человек, среди которых 10 юношей и 13 девушек. Сколькими способами можно выбрать 2 человек одного пола?
    """
        )

        print("Ответ: " + str(comb_without_repeat(10, 2) + comb_without_repeat(13, 2)))
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        summ(0)
        
def multi(mode_in):
    flag = 0
    res = 0
    if mode_in == 0:
        print("""
        (1) Посчитать по формуле произведение разных комбинаторных схем
        (2) Пример задачи на комбинаторное произведение
        (3) Выход в главное меню
    """
        )

        try:
            mode_in = int(input("Введите цифру соответсвующего действия без скобок: "))
        except BaseException:
            print("Такого действия нет")
            multi(0)
            flag = 1

    if mode_in == 1:

        action = {
            1: perm_without_repeat_opt,
            2: comb_without_repeat_opt,
            3: plac_without_repeat_opt,
            4: perm_with_repeat_opt,
            5: comb_with_repeat_opt,
            6: plac_with_repeat_opt,
        }

        print("""
        Выберите первый множитель
        (1) Перестановка без повторений
        (2) Сочетание без повторений
        (3) Размещение без повторений
        (4) Перестановка с повторениями
        (5) Сочетание с повторениями
        (6) Размещение с повторениями
    """
        )

        try:
            multiplier1 = int(input("Введите цифру соответсвующего выбора без скобок: "))
        except BaseException:
            print("Такого варианта нет")
            multi(1)
            flag = 1

        print("""
        Выберите второй множитель
        (1) Перестановка без повторений
        (2) Сочетание без повторений
        (3) Размещение без повторений
        (4) Перестановка с повторениями
        (5) Сочетание с повторениями
        (6) Размещение с повторениями
    """
        )

        try:
            multiplier2 = int(input("Введите цифру соответсвующего выбора без скобок: "))
        except BaseException:
            print("Такого варианта нет")
            multi(1)
            flag = 1

        multiplier1 = action[multiplier1](4)
        multiplier2 = action[multiplier2](4)

        print("Сумма равна " + str(multiplier1 * multiplier2))
    elif mode_in == 2:
        print("""
        Сколько существует n-значных чисел, которые делятся на 5?
    """
        )

        try:
            n = int(input("Введите n: "))
        except:
            print("Не правильный формат ввода")
            multi(2)
            flag = 1

        res = comb_without_repeat(9, 1)
        for i in range(1, n - 1):
            res *= comb_without_repeat(10, 1)

        res *= 2

        print("Ответ: " + str(res))
    elif mode_in == 3:
        flag = 1
    else:
        print("Такого действия нет")

    if flag == 0:
        multi(0)        

action = {
        1: perm_without_repeat_opt,
        2: comb_without_repeat_opt,
        3: plac_without_repeat_opt,
        4: perm_with_repeat_opt,
        5: comb_with_repeat_opt,
        6: plac_with_repeat_opt,
        7: summ,
        8: multi,
        9: lambda x: print("Выход из программы")
}

mode = 0
while mode != 9:
    print("""Выберите действие
      (1) Вычислить число перестановок без повторений
      (2) Вычислить число сочетаний без повторений
      (3) Вычислить число размещений без повторений
      (4) Вычислить число перестановок с повторениями
      (5) Вычислить число сочетаний с повторениями
      (6) Вычислить число размещений с повторениями
      (7) Посчитать сумму
      (8) Посчитать произведение 
      (9) Выход из программы
    """)

    try:
        mode = int(input("Введите цифру соответсвующего действия без скобок: "))
    except BaseException:
        print("Не правильный формат вводаа \n")

    #try:
    action[mode](0)
    #except BaseException:
       #print("Такого действия нет \n")
       #mode = 0