def effectivePermutation(l:list, n:int):
    perm = [i for i in range(n + 1)] #perm - сама перестановка, содержащая индексы исходного множетсва
    reverse = [i for i in range(n + 1)] # reverse - обратная перестановка, которая содердит индекс на каком месте находится соответсвующий элемент в перестановке (reverse[1] - индекс первого элемента в perm)
    m = n + 1 #для алгоритма необходимы граница которые больше наибольшего индекса элемента
    perm[0] = n + 1
    perm.append(m) #reverse[n + 1] = n + 1
    reverse[0] = None

    shift = [-1 for i in range(n + 1)] #список хранящий следующий сдвиг для каждого элемента, индекс равен индексу исходного списка
    shift[0] = None
    shift[1] = 0 #первый элемент сдвигать не будем когда дойдем до него, так как переберём все возможные перестановки

    k = 0  
    while m != 1:
        k += 1 #индекс перестановки
        print(str(k), end=") [")
        for i in range(1, n):
            print(l[perm[i] - 1], end = ", ")
        print(str(l[perm[n] - 1]) + "]")     
        m = n
        while perm[reverse[m] + shift[m]] > m: #если следующий или предыдущий элемент мень больше чем m, то дальше сдвигать не надо надо менять направление сдвига и работать с предыдущим элементом
            shift[m] = -shift[m]
            m -= 1

        location = reverse[m] #где находится текущий элемент
        where_to_shift = location + shift[m] #куда смещаем текущий элемент
        perm[location], perm[where_to_shift] = perm[where_to_shift], perm[location] #меняем местами

        index_item_where_shift = perm[location] #индекс элемента который был перемещён
        reverse[m], reverse[index_item_where_shift] = reverse[index_item_where_shift], location #запоминаем новые положения элементов в перестановке

a = [1, 2, 3, 4, 5]
effectivePermutation(a, len(a))

b = ["a", "b", "c"]
effectivePermutation(b, len(b))


        