"""Module for memory handling, contains memory implementations,
memory handling, and other functions as detailed in the class"""
class Memory_Handler:
	def __init__(self):
		#counter for constant memory
		self._constant_memory = [0,0,0,0]
		#counter for variable memory
		self._variable_memory = [0,0,0,0]

	#Get memory address of variable
	def _get_memory_address_variable(self, variable_type = None):
		#variable_type should have value
		if variable_type is not None:
			#memory address for whole
			if(variable_type == "whole"):
				address = (200+self._variable_memory[0])
				self._variable_memory[0] = self._variable_memory[0]+1
				return address

			#memory address for decimal
			elif(variable_type == "decimal"):
				address = (300+self._variable_memory[1])
				self._variable_memory[1] = self._variable_memory[1]+1
				return address

			#memory address for words
			elif(variable_type == "words"):
				address = (400+self._variable_memory[2])
				self._variable_memory[2] = self._variable_memory[2]+1
				return address

			#memory address for boolean
			elif(variable_type == "boolean"):
				address = (500+self._variable_memory[3])
				self._variable_memory[3] = self._variable_memory[3]+1
				return address

			#does not recognize variable type
			else:
				return -1

	#Get memory address of constant
	def _get_memory_address_constant(self, constant_type = None):
		#constant_type should have value
		if constant_type is not None:
			#memory address for constant whole
			if(constant_type == "cst_whole"):
				address = (600+self._constant_memory[0])
				self._constant_memory[0] = self._constant_memory[0]+1
				return address

			#memory address for constant decimal
			elif(constant_type == "cst_decimal"):
				address = (700+self._constant_memory[1])
				self._constant_memory[1] = self._constant_memory[1]+1
				return address

			#memory address for constant words
			elif(constant_type == "cst_words"):
				address = (800+self._constant_memory[2])
				self._constant_memory[2] = self._constant_memory[2]+1
				return address

			#memory address for constant boolean
			elif(constant_type == "cst_boolean"):
				address = (900+self._constant_memory[3])
				self._constant_memory[3] = self._constant_memory[3]+1
				return address

			#does not recognize constant type
			else:
				return -1