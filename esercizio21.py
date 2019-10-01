def printList(L):
    if L:
        print(L[0])
        printList(L[1:])


L = [1,2,3,4,5,6,7,8,9,10]
printList(L)