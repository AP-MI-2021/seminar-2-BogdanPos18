def isPrime(x):
    '''
    determina daca un numar este prim
    :param x:
    :return:
    '''
    if x < 2:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True

def testIsPrime():
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def printMenu():
    print("1. Citire lista")
    print("2. Afisare numere prime")
    print("3. Iesire")

def citireLista():
    l = []
    n = int(input("Dati nr de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def numerePrimeDinLista(l):
    '''
    determina nr prime dintr-o lista
    :param l: lista de nr intregi
    :return: o sublista a lui l, continand nr prime din l
    '''
    rezultat = []
    for i in range(len(l)):
        if isPrime(l[i]):
            rezultat.append(l[i])
    return rezultat

def testNumerePrimeDinLista():
    assert numerePrimeDinLista([4, 9, 8]) == []
    assert numerePrimeDinLista([1, 2, 3, 4, 5]) == [2, 3, 5]

def main():
    testIsPrime()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == '1':
            l = citireLista()
        elif optiune == '2':
            print(numerePrimeDinLista(l))
        elif optiune == '3':
            break
        else:
            print("Optiune gresita! Reincearca")

main()
