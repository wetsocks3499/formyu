# by c. yerger
# imports
version = 0.4
import mplot
from mpl_toolkits import mplot3
import numpy as np
import sys
## globals
formula = input()
cubeVolumeVar = 'v -c'
recPrisVolumeVar = 'v -r'
squarePyramidVolumeVar = 'v -sp'
HELP = 'help'
EXIT = 'exit'
VERSION = '--version'
## splash
print('''
~-~-~-~-~-~-~-~-~-

welcome to formyu

~-~-~-~-~-~-~-~-~-''')
## fallback def
def exit():
    sys.exit()
def script():
    print('\n')
## useful def
    def squarePyramidVolumeFunction():
        s = float(input('Edge length of the pyramid: '))
        h = float(input('Height of the pyramid: '))
        outprint = (s ** 2) * (h / 3)
        print(round(outprint, 2), 'units cubed.')
        script()
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
    def showVersion():
        print('You are running version ',string(version))
        script()
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
	    exit()
## run
script()