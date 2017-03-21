"""class for Function Directory
Stores characteristics of each block in the program
Must contain starting block
The function directory is represented as a Python Class
This Class contains two instance variables representing values for
1. Starting Block Key: String
2. Function Reference Table: Python Dictionary
"""
from structures import Dictionary

class Function_Directory():
	def __init__(self):
		#public variable for starting block key
		self.starting_block_key = "-1"

		#public variable for function reference table
		self.function_reference_table = Dictionary()

		#public variable for constant table
		self.constant_table = Dictionary()

	#add block information for new block
	def add_block_name(self, block_name = None):
		#block_name should have value
		if block_name is not None:
			#private variable for block return type (string)
			return_type = "void"

			#private variable for block primitives (Dictionary)
			primitives = Dictionary()

			#private variable for block lists (Dictionary)
			lists = Dictionary()

			#private variable for block parameters(list)
			parameters = []

			#private variable for block memory address (string)
			memory_address = ""

			#declare block_data
			block_data = [return_type,[primitives,lists],parameters,memory_address]

			#add new block name as key
			self.function_reference_table.insert(block_name,block_data)

			#Add memory address
			self.add_memory_address(block_name, self._get_memory_address_block())

	#Key for current block, add block return type if any	
	def add_block_return_type(self, key = None, block_return_type = None):
		#key should have value
		if key is not None:
			#block_return_type should have value
			if block_return_type is not None:
				#Index 0 of list is for block return type
				self.function_reference_table[key][0] = block_return_type

	#Key for current block, add primitive to primitive dictionary	
	def add_primitive(self, key = None, variable_name = None, variable_type = None):
		#key should have vaye
		if key is not None:
			#variable_name should have value
			if variable_name is not None:
				#variable_type should have value
				if variable_type is not None:
					#Index 1 of list is for primitives and lists dictionaries
					#Index 0 of such list is specifically for primitives
					variable_data = [variable_type, self._get_memory_address_variable(variable_type)]
					self.function_reference_table[key][1][0].insert(variable_name,variable_data)

	#Key for current block, add list to list dictionary	
	def add_list(self, key = None, variable_name = None, variable_size = None, variable_type = None):
		#key should have value
		if key is not None:
			#variable_name should have value
			if variable_name is not None:
				#variable_size should have value

				#patch for list variable size
				#if variable_size is not None:

					#variable_type should have value
				if variable_type is not None:
					#Index 1 of list is for primitives and lists dictionaries
					#Index 1 of such list is specifically for lists
					variable_data = [variable_type, self._get_memory_address_variable(variable_type), variable_size]
					self.function_reference_table[key][1][1].insert(variable_name,variable_data)

	#Constant value and constant type to identify constant
	def add_constant(self, constant_value = None, constant_type = None):
		#key should have value
		if constant_value is not None:
			if constant_type is not None:
				#create list for entry
				#value for dictionary entry
				constant_data = [constant_type, self._get_memory_address_constant(constant_type)]
				
				#insert to constant table
				self.constant_table.insert(constant_value,constant_data)

	#Key for current block, add one parameter found to parameters list
	def add_parameter_type(self, key = None, parameter_type = None):
		#key should have value
		if key is not None:
			#parameter should have value
			if parameter_type is not None:
				#Index 0 of list is for parameter list
				self.function_reference_table[key][2].append(parameter_type)

    #Key for current block, add memory address of block
	def add_memory_address(self, key, memory_address = None):
		#memory_address should have value
		if memory_address is not None:
			#Index 3 of list is for memory address
			if (memory_address != -1):
				self.function_reference_table[key][3] = memory_address

	#Get memory address of block
	def _get_memory_address_block(self):
		#memory address for block
		return 100

	#Get memory address of block
	def _get_memory_address_variable(self, variable_type = None):
		#variable_type should have value
		if variable_type is not None:
			#memory address for whole
			if(variable_type == "whole"):
				return 200

			#memory address for decimal
			elif(variable_type == "decimal"):
				return 300

			#memory address for words
			elif(variable_type == "words"):
				return 400

			#memory address for boolean
			elif(variable_type == "boolean"):
				return 500

			#does not recognize variable type
			else:
				return -1

	#Get memory address of block
	def _get_memory_address_constant(self, constant_type = None):
		#constant_type should have value
		if constant_type is not None:
			#memory address for constant whole
			if(constant_type == "cst_whole"):
				return 600

			#memory address for constant decimal
			elif(constant_type == "cst_decimal"):
				return 700

			#memory address for constant words
			elif(constant_type == "cst_words"):
				return 800

			#memory address for constant boolean
			elif(constant_type == "cst_boolean"):
				return 900

			#does not recognize constant type
			else:
				return -1

	#Check if a function id does not exist in the Function Reference Table
	def block_id_exists(self, block_id = None):
		#block_id should have value
		if block_id is not None:
			#Check the function names
			if block_id in self.function_reference_table:
				return True
								
			return False

	#Check if a var id exists in the Function Reference Table
	def var_id_exists(self, var_id = None, block_id = None):
		#var_id should have value
		if var_id is not None:
			#block_id should have value
			if block_id is not None:
				#Check the function name
				if self.block_id_exists(var_id):
					return True
				
				#Check the variable names
				if var_id in self.function_reference_table[block_id][1][0]:
					return True
				
				#check the list names
				if var_id in self.function_reference_table[block_id][1][1]:
					return True
									
				return False

	def constant_exists(self, constant_value = None, constant_type = None):
		#constant_id should have value
		if constant_value is not None:
			#constant_type should have value
			if constant_type is not None:
				#check if entry exists
				if self.constant_table.contains(constant_value):
					#check if entry exists as its corresponding type
					if (self.constant_table[constant_value][0] == constant_type):
						#value exists with corresponding type
						return True

					return False

	def get_variable_type_for_block(self, var_id = None, block_id = None):
		#var_id should have value
		if var_id is not None:
			#block_id should have value
			if block_id is not None:
				return self.function_reference_table[block_id][1][0][var_id][0]


	#print block information for all blocks
	def print_table(self):
		#print table formatted
		print("Function Reference Table\n")
		for key in self.function_reference_table.getInstance():
			print("*" + key + "* :")
			print("Return Type: " + self.function_reference_table[key][0])
			print("Primitives: ")
			print(self.function_reference_table[key][1][0])
			print("Lists: ")
			print(self.function_reference_table[key][1][1])
			print("Parameters: ")
			print(self.function_reference_table[key][2])
			print("Constants: ")
			print(self.constant_table)
			print("Function Memory Address: ")
			print(self.function_reference_table[key][3])
			print("\n")

#for testing purposes
if __name__ == '__main__':
	directory = Function_Directory()

	directory.add_block_name("Block1")
	directory.add_block_name("Block2")

	directory.add_block_return_type("Block1","whole")

	directory.add_parameter_type("Block1","decimal")
	directory.add_parameter_type("Block1","whole")
	directory.add_parameter_type("Block1","words")

	directory.add_parameter_type("Block2","whole")
	directory.add_parameter_type("Block2","words")

	#parameters
	directory.add_primitive("Block1","parameter1","decimal")
	directory.add_primitive("Block1","parameter2","whole")
	directory.add_primitive("Block1","parameter3","words")

	directory.add_primitive("Block2","parameter1","whole")
	directory.add_primitive("Block2","parameter2","words")

	#variables
	directory.add_primitive("Block1","variable1","words")
	directory.add_primitive("Block1","variable2","words")

	directory.add_list("Block2","listvariable1","5","whole")

	directory.print_table()
	