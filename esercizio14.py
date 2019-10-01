#nome vostri due amici di banco e età

diz = {"Nome" : ["Marco","Andrea"], "Cognome" : ["Marin","Conti"], "Età" : ["19","21"]}
len_a,len_b,len_c  = len(diz["Nome"]),len(diz["Cognome"]),len(diz["Età"])
k1,k2,k3 = diz["Nome"],diz["Cognome"],diz["Età"]
flag = 0
keys = diz.keys()#contiene le chiavi
conta = len(keys)#contiene il numero delle chiavi
lunghezze = []

for elem in range(0,conta,1):
    lunghezze.append((len(diz[x]))
    print(lunghezze[elem])


'''if(len_a < len_b or len_a < len_c):
    flag = len_a
elif(len_b < len_a or len_b < len_c):
    flag = len_b
else: flag = len_c

for x in range(0,flag,1):
    print(k1[x],k2[x],k3[x])'''