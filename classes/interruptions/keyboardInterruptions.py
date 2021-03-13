import msvcrt
class KeyboardInteruptions:
    def __init__(self):
        self.__statusInterrpution = 0


    def listenInterruption(self):
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == "I":
                self.__statusInterrpution = 1
            elif char == "E":
                self.__statusInterrpution = 2
            elif char == "P":
                self.__statusInterrpution = 3
            elif char == "C" and self.__statusInterrpution == 3:
                self.__statusInterrpution = 4

    def getStatusInterruption(self):
        return self.__statusInterrpution


    def setStatusInterruption(self, status):
        self.__statusInterrpution = status