#Esercizio1
#creare due tuple che rappresentino i due
#elenchi di nomi e cognomi descritti sotto:
#Nomi: Numa, Tullo, Anco
#Cognomi: Pompilio, Ostilio, Marzio

tupla1 = ('Numa','Tullo','Anco')
tupla2 = ('Pompilio','Ostilio','Marzio')
#print(tupla1,tupla2)


#Esercizio2
#Ottenere una lista in cui ogni elemento è un
#dizionario {'nome':'nome', 'cognome':'cognome'}, 
#che accoppia nomi e cognomi in base all'ordine
lista = []


for x in range(0,len(tupla1),1):
    lista.append({'nome':tupla1[x],'cognome':tupla2[x]})
print(lista)
print(type(lista[2]))
ciao = lista[0]
print(ciao["cognome"])