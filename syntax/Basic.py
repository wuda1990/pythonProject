def decision(x):
    if x > 90:
        return 'A'
    elif x > 80:
        return 'B'
    elif x > 70:
        return 'C'
    elif x > 60:
        return 'D'
    else:
        return 'F'


def stringOperation():
    var1 = 'Hello World!'
    print("Updated String :- ", var1[:6] + 'Python')
    print("It has been %d years since I started learning Python and "
          "It has been %d months since I started reviewing it" % (3, 6))


def listOperation():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    print(list1.reverse())

    list3 = list1 + list2
    print(list3)


def setOperation():
    x = {"apple", "banana", "cherry", True}
    y = {"google", 1, "apple", 2}

    z = x.symmetric_difference(y)
    print(z)


if __name__ == '__main__':
    print(decision(100))  # 'A'
    print(decision(85))  # 'B'
    print(decision(75))  # 'C'
    print(decision(65))  # 'D'
    print(decision(55))  # 'F
    stringOperation()
    listOperation()
    setOperation()
