# Project 001 : Calculator


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# values = [328509,22667121]

def add():
    total = 0
    for i in values:
        total = total + i
    return total

def sub():
    total = 0
    for i in values:
        total = total - i
    return total


def mul():
    total = 1
    for i in values:
        total = i * total
    return total


def div():
    total = 1
    for i in values:
        total = i / total
    return total


def operation(operation):
    match operation:
        case "+":
            return add()
        case "-":
            return sub()
        case "*":
            return mul()
        case "/":
            return div()
        case default:
            print("try again schlum")
