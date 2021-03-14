from classes.listProcess import ListProcess
from classes.listCompleteProcess import ListCompleteProcess
from operationsMathematics.operations import executeOperation
from classes.interruptions.keyboardInterruptions import KeyboardInteruptions
from colorama import init, Cursor, Back, Fore
from time import sleep
import os
init()


class VistProcess:
    def __init__(self, listLots):
        self.__listBatch = listLots
        self.__countProgram = 0
        self.__numberBatchActual = 1
        self.__cursorY = 5
        self.__listProcessFinish = ListCompleteProcess()
        self.__interruption = KeyboardInteruptions()
        self.__flagToContinuePrintProcess = True

    def __statusOfInterruptionInside(self):
        status = self.__interruption.getStatusInterruption()
        if status == 3:
            while True:
                self.__interruption.listenInterruption()
                status = self.__interruption.getStatusInterruption()
                if status == 4:
                    break
        if status == 1 or status == 2:
            self.__flagToContinuePrintProcess = False


    def __statusOfInterruptionOutside(self, listProcess, process):
        statusInterruption = self.__interruption.getStatusInterruption()
        if statusInterruption == 1:
            listProcess.addProcess(process)
            listProcess.deleteLastProcess()
            self.__cursorY -= 1
        elif statusInterruption == 2:
            process.setNumberLot(self.__numberBatchActual)
            self.__listProcessFinish.addProcessComplete(process)
            listProcess.deleteLastProcess()
        elif statusInterruption == 0 or statusInterruption == 4:
            self.__realizeOperation(process)
            self.__listProcessFinish.addProcessComplete(process)
            listProcess.deleteLastProcess()
        self.__interruption.setStatusInterruption(0)


    def __printProcessActual(self, process):
        maximunTime = 1
        idProgram = " "
        operation = " "
        timeRest = " "
        time = " "
        index = 1
        if process is not None:
            maximunTime = process.getMaximumTime()
            idProgram = process.getNumberProgram()
            operation = str(process.getFirstNumber()) + " " +\
                        process.getOperation() + " "+str(process.getSecondNumber())
            if process.getTimeTranscurred() > 0:
                index = process.getTimeTranscurred()
        print("\r" + Cursor.FORWARD(46) + "Operacion: " + operation, end="\n")
        print("\r" + Cursor.FORWARD(46) + "ID: " + str(idProgram), end="\n")
        while self.__flagToContinuePrintProcess:
            self.__interruption.listenInterruption()
            if index < maximunTime + 1:
                if process is not None:
                    timeRest = maximunTime - index
                    time = index
                print("\r" + Cursor.FORWARD(46) +
                      "Tiempo transcurrido: " + str(time) + "\n" + Cursor.FORWARD(46) +
                      "Tiempo restante: " + str(timeRest) + " ", end="")
                if process is not None:
                    process.setTimeTranscurred(time)
                print(Cursor.DOWN(4))
                self.__countProgram += 1
                print("\r" + Fore.LIGHTYELLOW_EX + "Contador del programa: ",
                      str(self.__countProgram), end="")
                print(Fore.RESET)
                print(Cursor.UP(8))
                self.__statusOfInterruptionInside()
                if idProgram is not 0:
                    sleep(1)
                else:
                    break
            else:
                break
            index = index + 1

    def __realizeOperation(self, process):
        number_1 = process.getFirstNumber()
        number_2 = process.getSecondNumber()
        result = executeOperation(number_1, number_2, process.getOperation())
        if type(result) is float:
            result = round(result, 2)
        operation = str(number_1) + " " + \
            process.getOperation() + " " + str(number_2)
        process.setOperation(operation)
        process.setResult(result)
        process.setNumberLot(self.__numberBatchActual)

    def __printInfo(self, flag, listProcess):
        os.system("cls")
        process = None
        if listProcess.numberProcess() > 0:
            process = listProcess.getAcualProcess()
        numberBatch = self.__listBatch.numberBatch()
        if numberBatch == 0:
            numberBatch = 1
        listProcess.printListProcessToExecute(1, 2, numberBatch - 1)
        print("\n")
        self.__listProcessFinish.printListCompleteOfProcess(80, 9)
        print("\n")
        print(Fore.RESET)
        print(Fore.LIGHTCYAN_EX + Cursor.FORWARD(46) +
              Cursor.UP(self.__cursorY) + "proceso en ejecucion",end="\n")
        print(Fore.RESET)
        if flag:
            self.__printProcessActual(process)
            self.__flagToContinuePrintProcess = True
            self.__statusOfInterruptionOutside(listProcess, process)
        else:
            self.__printProcessActual(process)
        print("\n\n\n\n")
        if not flag:
            self.__listProcessFinish.numberProcessComplete()

    def __isNotEmptyList(self, listProcess):
        if listProcess.numberProcess() > 0:
            return True
        else:
            return False

    def __imprimirDate(self, listProcess, flagState):
        continueToPrintActualList = self.__isNotEmptyList(listProcess)
        while continueToPrintActualList:
            if flagState:
                self.__printInfo(True, listProcess)
            self.__cursorY += 1
            continueToPrintActualList = self.__isNotEmptyList(listProcess)
        if not flagState:
            self.__printInfo(False, listProcess)
        else:
            self.__numberBatchActual += 1

    def __completeVistAllProcess(self):
        numberBatch = self.__listBatch.numberBatch()
        for index in range(0, numberBatch):
            listActualProcess = self.__listBatch.getActualListLots()
            self.__imprimirDate(listActualProcess , True)
            self.__listBatch.deleteActualProcess()
        listProcess = ListProcess()
        self.__imprimirDate(listProcess, False)

    def printScreen(self):
        self.__completeVistAllProcess()
