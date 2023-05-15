def __generateCompositions(n): #рекурсивная функция генерации композиция числа
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    
    compositions = [] #создаём пустую композиуию в которую будем записывать композицию текущего числа
    for i in range(1, n): #на текущее место в копмозиции перебирааем все значения
        for c in __generateCompositions(n - i): #последующие места в композиции состоят из композиций оставшейся суммы, композиция нуля вернет пустой массив
            compositions.append([i] + c)
    compositions.append([n]) #добавляем число для которого ищем как композицию
    return compositions

def generateCompositions(n):
    compositions = __generateCompositions(n)
    for i in range(len(compositions)):
        print("(", end="")
        for j in range(len(compositions[i]) - 1):
            print(str(compositions[i][j]), end=", ")

        print(str(compositions[i][-1]) + ")")    


generateCompositions(3)
print()
generateCompositions(7)