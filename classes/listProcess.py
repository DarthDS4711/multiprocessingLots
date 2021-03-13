from colorama import init, Cursor, Fore
from operator import attrgetter

init()


class ListProcess:
    def __init__(self):
        self.__list = []

    def addProcess(self, process):
        self.__list.append(process)

    def numberProcess(self):
        return len(self.__list)

    def getAcualProcess(self):
        if len(self.__list) > 0:
            return self.__list[0]

    def deleteLastProcess(self):
        if len(self.__list) > 0:
            self.__list.pop(0)

    def printListProcessToExecute(self, x, y, lotsPending):
        print(Fore.LIGHTRED_EX +  Cursor.UP(y) + Cursor.FORWARD(x) +
              "Numero de lotes pendientes: ", lotsPending)
        print(Fore.RESET)
        for index in range(1, 6):
            if index >= len(self.__list):
                print(" ", end="\n")
            elif index < len(self.__list):
                print(Cursor.FORWARD(x) + "process: ", self.__list[index], end="\n")

    def clearList(self):
        self.__list.clear()


