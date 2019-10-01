#presi 3 numeri vede il maggiore 

def numMax (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print("Numero: ",num1)
    if num2>=num1 and num2>=num3:
        print("Numero: ",num2)
    if num3>=num1 and num3>=num2:
        print("Numero: ",num3)
        



a =  int(input("Inserisci 1° numero: \n"))
b =  int(input("Inserisci 2° numero: \n"))
c =  int(input("Inserisci 3° numero: \n"))

numMax (a,b,c)
