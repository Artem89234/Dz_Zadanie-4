a = input('Впшите небольшой текст: ')
b = []
b = a.split(' ')
t = len(b)
c = []
for i in range(t): #Определяем длину каждого слова в строке
    p = len(b[i])
    c.append(p)
    
P = max(c) #Находим максимальное количество букв
for i in range(t): #Находим индекс в списке с количеством бук, индекс максимального количества букв
    if c[i] == P:
        print('Слово с максимальным количеством букв: ',b[i])
        break

w = 0
y = []
for i in range(t):
    w = 0
    for j in range(t):
        if b[i] == b[j]:
            w = w + 1
    y.append(w)

P = max(y)
for i in range(t):
    if y[i] == P:
        print('Максимальное повторяющееся слово в строке: ', b[i])
        break


