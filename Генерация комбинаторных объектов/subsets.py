def subsets(a:list): #вывод всех подмножеств множества вне лексекографическом порядке
    b = []
    for i in range(len(a) + 1):
        b.append(0)

    print("1. (∅)")

    b[0] = 1
    k = 2
    last_element = 0 #для коректного вывода последднего элемента
    while b[-1] != 1:
        flag = 0
        i = 0
        print(str(k) + ". " + "(", end = "")
        while i != len(a):
            if b[i] == 1:
                if i == last_element: #если текущий элемент последний который нужно печатать
                    print(str(a[i]) + ")")
                    break
                else:
                    print(a[i], end = ", ")

            i += 1

        i = 0
        while b[i] == 1: #проходимся по всем двоичным наборам
            b[i] = 0
            i +=1

        b[i] = 1
        if i > last_element: #определяем с каким последним элементом работаем
            last_element = i

        k += 1    

def subsets_l_o(a:list): 
    b = []
    for i in range(len(a) + 1):
        b.append(0)

    print("1. (∅)")
    k = 2
    for i in range(len(a)): #выводим подмножетсва из 1 элемента
        print(str(k) + ". " + "(" + str(a[i]) + ")")
        k += 1
    
    last_element_index = 1 #для коректного вывода последнего элемента
    b[last_element_index] = 1
    while b[-1] != 1:
        i = 0
        while b[i] == 1 and i != last_element_index:
            b[i] = 0
            i += 1

        if i == last_element_index:
            b[i] = 0
            last_element_index += 1
            b[last_element_index] = 1
        else:
            b[i] = 1

            print(str(k) + ". " + "(", end = "")
            i = 0
            while i != last_element_index:
                if b[i] == 1:
                        print(a[i], end = ", ")

                i += 1

            print(str(a[i]) + ")")    

        k += 1        

subsets([1, 2, 3, 4, 5])
print()
subsets([])
print()
subsets_l_o([1, 2, 3])
print()
subsets_l_o(["a", "b", "c", "d"])              
