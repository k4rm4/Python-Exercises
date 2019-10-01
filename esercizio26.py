#viene passato carattere come parametro e ci dice se è una vocale

def checkVocale(lettera):
    controllo = "aeiou"
    flag = 0
    for i in range (0,len(controllo)):
        if controllo[i] == lettera:
            print("La lettera",lettera," è una vocale!")
            flag = 1
    if flag == 0: 
        print("La lettera",lettera," non è una vocale!")    



lettera = input("Inserisci una lettera: \n")
lettera = lettera.lower()
checkVocale(lettera)