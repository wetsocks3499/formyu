# formyu 0.1 by c. yerger 
import sys
print('''
~-~-~-~-~-~-~-~-~-

welcome to formyu 

~-~-~-~-~-~-~-~-~-
''')
## fallback def
def exit():
	sys.exit()
def script():
	print('''
	''')
## declare
	formula = input()
	cubeVolumeVar = 'v -c'
	HELP = 'help'
	EXIT = 'exit'
## useful def
	def cubeVolumeFunction(): 
		s = float(input('Side length of cube: '))
		outprint = s ** 3
		print('Volume = ', end='')
		print(round(outprint, 2), 'units cubed.')
		script()
	def helpFunc():
		f = open("man.txt", 'r')
		print(f.read())
		script()
## redirect
	if formula == cubeVolumeVar:
		cubeVolumeFunction()
	if formula == HELP:
		helpFunc()
	if formula == EXIT:
		exit()
## run
script()