from colorama import init, Cursor, Back, Fore

init()


class ListCompleteProcess:
    def __init__(self):
        self.__list = []

    def addProcessComplete(self, processComplete):
        self.__list.append(processComplete)

    def printListCompleteOfProcess(self, x, y):
        print(Cursor.UP(y) + Cursor.FORWARD(x) + Fore.GREEN + "Procesos completados")
        for index in range(0, len(self.__list)):
            print(Cursor.FORWARD(x) + self.__list[index].toStringProcessComplete())

    def numberProcessComplete(self):
        print("Numero de procesos completados ", len(self.__list))