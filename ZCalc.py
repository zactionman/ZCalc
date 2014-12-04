#! /usr/bin/python3

from tkinter import *
from tkinter.ttk import *
import ZMath

class App():

	def __init__(self, master):
		self.master = master
		self.master.option_add('*tearOff', FALSE)
		
		# Variables needed for program
		# This variable is for the conetents of the entry widget (current number entered).
		self.number = StringVar(); self.number.set('0')
		# This varialbe is to detect when decimal has been used.
		self.dec = 'No'
		# This is to detect if the operator has been set.
		self.oper = 'No'
		# The two numbers and operation to use for maths!
		self.number1 = 0
		self.number2 = 0
		self.operation = ''

		# Build GUI!
		# Master content frame
		self.MFrame = Frame(master)
		self.MFrame.grid()
		# This is for the entry widget which will show input numbers and results of calculation.
		# The actual entry widget itself.
		self.NumView = Entry(self.MFrame, textvariable=self.number, justify=RIGHT)
		self.NumView.grid(column=0, row=0, columnspan=4, sticky='ew')
		self.NumView.state(['readonly'])
		# For knowing when to clear entry widget. 0 for yes, 1 for no.
		self.eclear = 0

		self.master.bind('<Delete>', lambda e: self.Backspace())
		
		# Buttons 1-3 for the calculator.
		Button(self.MFrame, text=1, width=8, command=lambda: self.NumInput('1')).grid(column=0, row=3)
		Button(self.MFrame, text=2, width=8, command=lambda: self.NumInput('2')).grid(column=1, row=3)
		Button(self.MFrame, text=3, width=8, command=lambda: self.NumInput('3')).grid(column=2, row=3)
		# Buttons 4-6 for the calculator.
		Button(self.MFrame, text=4, width=8, command=lambda: self.NumInput('4')).grid(column=0, row=2)
		Button(self.MFrame, text=5, width=8, command=lambda: self.NumInput('5')).grid(column=1, row=2)
		Button(self.MFrame, text=6, width=8, command=lambda: self.NumInput('6')).grid(column=2, row=2)
		# Buttons 7-9 for the calculator.
		Button(self.MFrame, text=7, width=8, command=lambda: self.NumInput('7')).grid(column=0, row=1)
		Button(self.MFrame, text=8, width=8, command=lambda: self.NumInput('8')).grid(column=1, row=1)
		Button(self.MFrame, text=9, width=8, command=lambda: self.NumInput('9')).grid(column=2, row=1)
		# button 0, operators, decimal, and = button.
		Button(self.MFrame, text=0, width=12, command=lambda: self.NumInput('0')).grid(column=0, row=4, columnspan=2, sticky='w')
		Button(self.MFrame, text='.', width=4, command=lambda: self.NumInput('.')).grid(column=1, row=4, sticky='e')
		Button(self.MFrame, text='=', width=8, command=self.GetCalc).grid(column=2, row=4)
		Button(self.MFrame, text='+', width=4, command=lambda: self.OperInput('+')).grid(column=3, row=1)
		Button(self.MFrame, text='-', width=4, command=lambda: self.OperInput('-')).grid(column=3, row=2)
		Button(self.MFrame, text='*', width=4, command=lambda: self.OperInput('*')).grid(column=3, row=3)
		Button(self.MFrame, text='/', width=4, command=lambda: self.OperInput('/')).grid(column=3, row=4)

	
	def NumInput(self, num):
		# Detect when to overwright the entry.
		if self.eclear == 0 and num != '.':
			self.number.set(num)
			self.eclear = 1
		# Detect when adding a decimal is appropriate
		elif num == '.' and self.dec == 'No':
			old = self.number.get()
			self.number.set(old + num)
			self.dec = 'Yes'
		# If a decimal already exists do nothing when decimal button is pressed.
		elif num == '.' and self.dec == 'Yes':
			pass
		# In all other situations append the number pressed to the entry widget.
		else:
			old = self.number.get()
			self.number.set(old + num)
			

	def OperInput(self, operation):
		# If an operator has not already been chosen then set the operator.
		if self.oper == 'No':
			# Convert and store number1 as a float
			self.number1 = float(self.number.get())
			self.operation = operation	
			self.eclear = 0
			self.oper = 'Yes'

		else:
			# If an operator has already been chosen do nothing when operator button is pressed.
			pass
	
	def Backspace(self):
		entrysnap = self.number.get()
		prune = entrysnap[-1]

		if len(entrysnap) > 1 and prune != '.':
			# Code to remove diget from entry when not pruning decimal
			entrysnap = entrysnap[0:-1]
			self.number.set(entrysnap)

		elif len(entrysnap) > 1 and prune == '.':

			# Code to remove decimal from entry
			entrysnap = entrysnap[0:-1]
			self.number.set(entrysnap)
			self.dec = 'No'

		else:
			self.number.set('0')
			self.eclear = 0

	def GetCalc(self):
		# Has an operator been chosen?
		if self.oper == 'Yes':
			# Convert number2 into a float
			self.number2 = float(self.number.get())
			# Call the function that actually calculates the answer
			answer = ZMath.calculator(self.number1, self.number2, self.operation)
			# Show the answer in the entry field
			self.number.set(str(answer))
			# Reset global variables
			self.oper = 'No'
			self.eclear = 0
			self.dec = 'No'
		else:
			pass



	def plchldr(self):
		print ('placeholder')

		

root = Tk()
root.title('ZCalc')
app = App(root)
root.mainloop()
