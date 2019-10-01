#creare una lista contenente 3 liste con 1 tupla ciascuno

def numMax (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2>=num1 and num2>=num3:
        return num2
    if num3>=num1 and num3>=num2:
        return num3


tupla1 = (1,2,3)
tupla2 = (13,11,9)
tupla3 = (11,13,13)

lista1 = []
lista2 = []
lista3 = []
listone = []

for i in range(0,len(tupla1)):
    lista1.append(tupla1[i])
    lista2.append(tupla2[i])
    lista3.append(tupla3[i])

listone.append(lista1)
listone.append(lista2)
listone.append(lista3)

print(listone)

for i in range(0,len(listone)):
        print("Maggiore della lista n°",i,": ",numMax(listone[i][0],listone[i][1],listone[i][2]))




