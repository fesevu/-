def heapPermutation(list, l, count): #алгоритм хипа порождения перестановок + подсчёт перестановок, при котром как бы фиксируется последний элемент
    count = 0
    if l == 1: #печатаем текущую перестановку, так как работаем с подмножетсвом из 1 элемента
        print(list)
        count = 1 #1 перестановка
        return count
    else:
        for i in range(l): #проходимся по каждому элементу
            count += heapPermutation(list, l - 1, count) #вызываем для подмножеств, и суммируем количтсво перестановок для каждого элемента
            if l % 2 == 0: #если четное меняем послежний элемент с текущим
                list[l - 1], list[i] = list[i], list[l - 1] 
            else:
                list[0], list[l - 1] = list[l - 1], list[0]

    return count            

a = [1, 2, 3]
b = ["a", "b", "c", "d", "e"]

count = heapPermutation(a, len(a), 0)
print(count)
count = heapPermutation(b, len(b), 0)
print(count)
            