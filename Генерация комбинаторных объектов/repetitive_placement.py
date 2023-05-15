def repetitivePlacement(a:list, k:int): #генерация размещений с повторениями в лексекографическом порядке в отсортированном списке
    plac = [] #генерации множества k-разрядных чисел в системе счисления с основанием len(a)
    for i in range(k):
        plac.append(0)
      
    j = k - 1
    count = 1
    while j != -1:
        print(str(count) + ". (", end="") #печать размещения
        for i in range(k - 1):
            print(str(a[plac[i]]), end=", ")

        print(str(a[plac[-1]]) + ")")

        j = k - 1
        while plac[j] == len(a) - 1:
            plac[j] = 0
            j -= 1

        plac[j] += 1
        count += 1

repetitivePlacement([1, 2, 3, 4, 5], 2)
print()
repetitivePlacement(["a", "b", "c", "gh", "sz"], 3) 

               
    