#scrivi una funzione a  cui passerai come parametro una stringa e ti restituirà
#una versione della stessa stringa al contrario (esempio "abcd" --> "dcba")


def reverse (stringa):
    stringaReverse = ""
    for i in range(len(stringa)-1,-1,-1):
        stringaReverse = stringaReverse + stringa[i]
    print(stringaReverse)


stringa = input("Inserisci una stringa: \n")
reverse(stringa)
