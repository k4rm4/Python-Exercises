output = ''
tastiera = input("Inserisci un nucleotide tra i seguenti: (A-C-G-T)\n")
tastiera = tastiera.upper()
if (tastiera == 'A'):
    output = 'T'
    print(output)
elif (tastiera == 'T'):
    output = 'A'
    print(output)
elif (tastiera == 'C'):
    output = 'G'
    print(output)
elif (tastiera == 'G'):
    output = 'C'
    print(output)
else:
    print("Non hai inserito un nucleotide tra questi: (A-C-G-T)")