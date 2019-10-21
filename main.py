# formyu 0.1 by c. yerger 
import sys
print('''
~-~-~-~-~-~-~-~-~-

welcome to formyu 

~-~-~-~-~-~-~-~-~-''')
## fallback def
def exit():
    sys.exit()
def script():
    print('\n')
## declare
    formula = input()
    cubeVolumeVar = 'v -c'
    recPrisVolumeVar = 'v -r'
    HELP = 'help'
    EXIT = 'exit'
## useful def
    def cubeVolumeFunction(): 
        s = float(input('Side length of cube: '))
        outprint = s ** 3
        print('\nVolume = ')
        print(round(outprint, 2), 'units cubed.')
        script()
    def recPrisVolumeFunc():
        w = float(input('Width: '))
        l = float(input('Length: '))
        h = float(input('Height: '))
        outprint = w * l * h
        print('\nVolume = ')
        print(round(outprint, 2), 'units cubed.')
        script()
    def helpFunc():
        f = open("man.txt", 'r')
        print(f.read())
        script()
## redirect
    if formula == cubeVolumeVar:
	    cubeVolumeFunction()
    if formula == recPrisVolumeVar:
        recPrisVolumeFunc()
    if formula == HELP:
	    helpFunc()
    if formula == EXIT:
	    exit()
## run
script()