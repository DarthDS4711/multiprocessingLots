def __sum(number1, number2):
    return number1 + number2


def __rest(number1, number2):
    return number1 - number2


def __mult(number1, number2):
    return number1 * number2


def __div(number1, number2):
    return number1 / number2


def __modul(number1, number2):
    return number1 % number2


def executeOperation(number1, number2, operation):
    if (operation == "sum"):
        return __sum(number1, number2)
    elif (operation == "rest"):
        return __rest(number1, number2)
    elif (operation == "mult"):
        return __mult(number1, number2)
    elif (operation == "div"):
        return __div(number1, number2)
    elif (operation == "mod"):
        return __modul(number1, number2)

