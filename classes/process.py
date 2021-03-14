class Process:
    def __init__(self, operation, maximumTime, numberProgram, number1, number2):
        self.__operation = operation
        self.__maximumTime = maximumTime
        self.__numberProgram = numberProgram
        self.__number1 = number1
        self.__number2 = number2
        self.__result = "Error"
        self.__numberBatch = 0
        self.__timeTranscurred = 0

    def setTimeTranscurred(self, time):
        self.__timeTranscurred = time

    def getTimeTranscurred(self):
        return self.__timeTranscurred

    def getOperation(self):
        return self.__operation

    def getMaximumTime(self):
        return self.__maximumTime

    def getNumberProgram(self):
        return self.__numberProgram

    def getFirstNumber(self):
        return self.__number1

    def getSecondNumber(self):
        return self.__number2

    def __str__(self):
        chain = "ID: " + str(self.__numberProgram) + " " + \
                "TME: " + str(self.__maximumTime) + " " + \
                "TT: " + str(self.__timeTranscurred)
        return chain

    def getResult(self):
        return self.__result

    def setResult(self, result):
        self.__result = result

    def toStringProcessComplete(self):
        chain = "ID: " + str(self.__numberProgram) + "  ope: " + \
            self.__operation + " result: " + str(self.__result) + " lot: " + str(self.__numberBatch)
        return chain

    def setOperation(self, operation):
        self.__operation = operation

    def setNumberLot(self, number):
        self.__numberBatch = number

    def getNumberBatch(self):
        return self.__numberBatch
