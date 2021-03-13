from classes.process import Process
from classes.listProcess import ListProcess
from classes.listLots import ListLots
from classes.container.tableIndex import TableIndex
import random
import os


class AutomaticGenerateProcess:
    def __init__(self):
        self.__listBatch = ListLots()
        self.__tableId = TableIndex()
        self.__numberProgram = 1

    def addingProcess(self):
        listProcess = ListProcess()
        numberMaximumProcess = int(input("Ingresa el numero de procesos a ejecutar: "))
        if numberMaximumProcess == 0:
            numberMaximumProcess = 1
        for index in range(0, numberMaximumProcess):
            process = self.__createProcess()
            listProcess.addProcess(process)
            if listProcess.numberProcess() % 5 == 0:
                self.__listBatch.addBatch(listProcess)
                listProcess = ListProcess()
        if listProcess.numberProcess() > 0:
            self.__listBatch.addBatch(listProcess)

    def __optionsOperations(self):
        operation = random.randint(1, 5)
        if operation == 1:
            return "sum"
        elif operation == 2:
            return "rest"
        elif operation == 3:
            return "mult"
        elif operation == 4:
            return "div"
        elif operation == 5:
            return "mod"


    def __createProcess(self):
        os.system("cls")
        operation = self.__optionsOperations()
        number1 = random.randint(0, 200)
        number2 = random.randint(1, 200)
        timeMaximumProcess = random.randint(5, 15)
        idProgram = self.__numberProgram
        process = Process(operation, timeMaximumProcess, idProgram, number1, number2)
        self.__numberProgram += 1
        return process

    def getLots(self):
        return self.__listBatch
