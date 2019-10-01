def palindroma (parola):
    inizio,fine = 0,len(parola)-1
    if(len(parola)==0 or len(parola)==1):
        print("La parola è palindroma! \n")
    elif (parola[inizio]==parola[fine]):
        return palindroma(parola[1:len(parola)-1])
    else:
        print("La parola non è palindroma! \n")


parola = input("Inserisci la parola: \n")
palindroma(parola)
