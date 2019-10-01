#scrivere ciao n volte con ricorsione, senza for

def ciaoRic (n):
    if(n==0):
        print("---------ciao finiti---------\n")
    else:
        print("ciao n° ",n)
        ciaoRic(n-1)


n = int(input("Inserisci quante volte vuoi vedere ciao: \n"))
ciaoRic(n)