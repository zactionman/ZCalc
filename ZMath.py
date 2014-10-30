#! /usr/bin/python

# the math part of ZCalc

from math import *


def calculator(first, second, oper):

	if oper == '+':
		answer = first + second
		return float(answer)
	elif oper == '-':
		answer = first - second
		return float(answer)
	elif oper == '*':
		answer = first * second
		return float(answer)
	elif oper == '/':
		answer = first / second
		return float(answer)
	else:
		print ('wtf happened?')
	
