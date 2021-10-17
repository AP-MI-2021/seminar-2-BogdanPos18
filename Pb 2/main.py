def printMenu():
    print("1. Citire lista")
    print("2. Afisare subsecventa")
    print("3. Iesire")

def citireLista():
    l = []
    stringCitit = input("Dati lista: ")
    numere = stringCitit.split(",")
    for x in numere:
        l.append(int(x))
    return l

def toateDivizibileCu10(l):
    '''
    determina daca toate elementele dintr-o lista sunt divizibile cu 10
    :param l: lista de nr intregi
    :return: True, daca toate elementele din lista sunt divizibile cu 10, False in caz contrar
    '''
    for x in l:
        if x % 10 != 0:
            return False
    return True

def testToateDivizibileCu10():
    assert toateDivizibileCu10([4, 10, 2]) is False
    assert toateDivizibileCu10([10]) is True

def subsecventaDivizibileCu10(l):
    '''
    determina una din cele mai lungi subsecvente de nr divizibile cu 10
    :param l: lista de nr intregi
    :return: una din cele mai lungi subsecvente de nr divizibile cu 10
    '''''
    subsecventaMax = []
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            if toateDivizibileCu10(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def testSubsecventaDivizibileCu10():
    assert (subsecventaDivizibileCu10([4, 5, 6]) == []) is True
    assert (subsecventaDivizibileCu10([10, 20, 3, 14]) == [10, 20]) is True

def main():
    testToateDivizibileCu10()
    testSubsecventaDivizibileCu10()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiune")
        if optiune == '1':
            l = citireLista()
        elif optiune == '2':
            print(subsecventaDivizibileCu10(l))
        else:
            break

main()