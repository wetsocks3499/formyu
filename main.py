# by c. yerger, runs on Python 3
## splash
print('''
~-~-~-~-~-~-~-~-~-

welcome to formyu

~-~-~-~-~-~-~-~-~-
''')
# imports
version = 0.4
import sys
## globals
formula = ''
cubeVolumeVar = 'v -c'
recPrisVolumeVar = 'v -r'
squarePyramidVolumeVar = 'v -sp'
HELP = 'help'
EXIT = 'exit'
VERSION = '--version'
## fallback def
def exit():
    sys.exit()
## function def
def squarePyramidVolumeFunction():
    s = float(input('Edge length of the pyramid: '))
    h = float(input('Height of the pyramid: '))
    outprint = (s ** 2) * (h / 3)
    print(round(outprint, 2), 'units cubed.')
def cubeVolumeFunction():
    s = float(input('Side length of cube: '))
    outprint = s ** 3
    print('\nVolume = ')
    print(round(outprint, 2), 'units cubed.')
def recPrisVolumeFunc():
    w = float(input('Width: '))
    l = float(input('Length: '))
    h = float(input('Height: '))
    outprint = w * l * h
    print('\nVolume = ')
    print(round(outprint, 2), 'units cubed.')
def helpFunc():
    f = open("man.txt", 'r')
    print(f.read())
def showVersion():
    print('You are running version ', version)
## run def
def script():
    running = True
    while running == True:
        formula = input()
## redirect
        if formula == cubeVolumeVar:
            cubeVolumeFunction()
        if formula == recPrisVolumeVar:
            recPrisVolumeFunc()
        if formula == squarePyramidVolumeVar:
            squarePyramidVolumeFunction()
        if formula == HELP:
            helpFunc()
        if formula == VERSION:
            showVersion()
        if formula == EXIT:
            running = False
            exit()
## run call
script()