from vist.vistProcess import VistProcess
from classes.automaticGenererateProcess import AutomaticGenerateProcess


def main():
    addProcess = AutomaticGenerateProcess()
    addProcess.addingProcess()
    vist = VistProcess(addProcess.getLots())
    vist.printScreen()
    input()


if __name__ == '__main__':
    main()
