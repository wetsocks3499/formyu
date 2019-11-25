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
formula = input("Please select an option:\nCube [1]\nRectangular Prism\nSquare-based Pyramid\nTrapezium\nTriangular Pyramid\nCone\nExit")
cubeVolumeVar = '1'
recPrisVolumeVar = '2'
squarePyramidVolumeVar = '3'
trapeziumVolumeVar = '4'
trianglePyramidVolumeVar = '5'
coneVar = '6'
HELP = '7'
EXIT = '8'
VERSION = '9'
## fallback def
def exit():
    sys.exit()
## function def
def trianglePyramidVolumeFunction():
    lb = float(input('Length of the base: '))
    hb = float(input('Height of the base: '))
    hp = float(input('Height of the pyramid: '))
    outprint = ((lb*hb)*hp)/3
    print(round(outprint, 2), 'units cubed.')
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

def trapeziumVolumeFunc():
    wOne = float(input('Width 1: '))
    wTwo = float(input('Width 2: '))
    l = float(input('Length: '))
    h = float(input('Height: '))
    outprint = (0.5 * (wOne + wTwo) * h) * l
    print('Volume = ', round(outprint, 2), 'units cubed.')

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
        if formula == cubeVolumeVar:  # Ugh. The ONLY reason I did this is because
            cubeVolumeFunction()      # Python doesn't have a switch case.
        if formula == recPrisVolumeVar:
            recPrisVolumeFunc()
        if formula == squarePyramidVolumeVar:
            squarePyramidVolumeFunction()
        if formula == trapeziumVolumeVar:
            trapeziumVolumeFunc()
        if formula == HELP:
            helpFunc()
        if formula == VERSION:
            showVersion()
        if formula == EXIT:
            running = False
            exit()
## run call
script()