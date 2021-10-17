from copy import copy, deepcopy


def print_menu():
    print("1. Citire lista ")
    print("2. Afisare numere prime ")
    print("3. Determinare cea mai lunga subsecventa de numere divizibile cu 10")
    print("4. Testati metode de reprezentare a listelor in memorie")
    print("x. Iesire")


def read_list():
    l = []
    string_citit = input("Dati lista de nr separate prin virgula: ")
    numere = string_citit.split(",")
    for x in numere:
        l.append(int(x))
    return l


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True


def get_primes(list):
    primes = []
    for x in list:
        if is_prime(x):
            primes.append(x)
    return primes


def test_get_primes():
    assert (get_primes([1, 2, 3, 5, 7, 10, 100]) == [2, 3, 5, 7]) is True
    assert (get_primes([10, 20, 15, 6]) == []) is True
    assert (get_primes([3, 11, 8, 17, 4]) == [3, 11]) is False


def all_div_10(list):
    for x in list:
        if x % 10 != 0:
            return False
    return True


def get_longest_all_div_10(list):
    rez = ()
    for i in range(len(list)):
        for j in range(i, len(list)):
            if all_div_10(list[i:j+1]) and len(list[i:j+1]) > len(rez):
                rez =  list[i:j+1]
    return rez


def test_get_longest_all_div_10():
    assert (get_longest_all_div_10([10, 20, 30, 5]) == [10, 20, 30]) is True
    assert (get_longest_all_div_10([1, 2, 19, 21]) == []) is False
    assert (get_longest_all_div_10([2, 10, 100, 4, 5, 20]) == [20]) is False


def test_copy_methods():
    l1 = [1, 2, 3]
    l2 = l1
    l2[0] = 100
    print(l1)

    print("liste de elemente de tip valoare")
    print("shallow copy")
    # shallow copy
    l1 = [1, 2, 3]
    l2 = l1[:]
    l2[0] = 100
    print(l1)

    # echivalent (shallow copy)
    l1 = [1, 2, 3]
    l2 = l1.copy()
    l2[0] = 100
    print(l1)

    # echivalent (shallow copy)
    l1 = [1, 2, 3]
    l2 = copy(l1)
    l2[0] = 100
    print(l1)

    print("deep copy")
    # deep copy
    l1 = [1, 2, 3]
    l2 = deepcopy(l1)
    l2[0] = 100
    print(l1)

    print("--------------------")
    print("liste de elemente de tip referinta")
    print("shallow copy")
    # shallow copy
    l1 = [[1], [2, 3], [4]]
    l2 = l1[:]
    l2[0][0] = 100
    print(l1)
    for i in range(len(l1)):
        print(id(l1[i]))
        print(id(l2[i]))

    print("deep copy")
    # deep copy
    l1 = [[1], [2, 3], [4]]
    l2 = deepcopy(l1)
    l2[0][0] = 100
    print(l1)
    for i in range(len(l1)):
        print(id(l1[i]))
        print(id(l2[i]))


def main():
    test_get_primes()
    test_get_longest_all_div_10()
    l = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = read_list()
        elif optiune == "2":
            print(get_primes(l))
        elif optiune == "3":
            print(get_longest_all_div_10(l))
        elif optiune == "4":
            test_copy_methods()
        else:
            break


main()
