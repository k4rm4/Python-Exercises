def countDown (contatore):
    if (contatore==0):
        print("o",contatore)
        print("\n Finito!\n")
        
    elif (contatore<0):
        print("Countdown minore di zero!")
    else: 
        print("o",contatore)
        contatore-=1
        countDown(contatore)
    
        

contatore = int(input("Inserisci il numero per il countdown: \n"))
countDown(contatore)

