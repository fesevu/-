def generatePartitions(n): #генерация разбиения числа n в лексикографическом порядке
    if n == 0:
        print("()")
        return
    
    patr = [1 for i in range(n)] #первое разбиение из 1

    while len(patr) != 1:
        #выводим разбиение
        print("(", end="")
        for i in range(len(patr) - 1):
            print(patr[i], end=", ")

        print(str(patr[-1]) + ")")

        #находим первый минимальный элемент и увеличиваем на 1 а последний элемент уменьшаем на 1  
        min_index = 0
        for i in range(1, len(patr) - 1):
            if patr[i] < patr[min_index]:
                min_index = i

        patr[min_index] += 1
        patr[-1] -= 1

        s = sum(patr[min_index + 1:]) #сумма элементов
        temp = patr[:min_index + 1] + [1 for i in range(s)]
        patr = temp
                
    print("("  + str(patr[0]) + ")")

generatePartitions(5)
print()
generatePartitions(7)        