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
		self._starting_block_key = -1

		#public variable for function reference table
		self.function_reference_table = Dictionary()

	#add block information for new block
	def add_block_name(self, block_name_parameter = None):
		#Key should have value
		if block_name_parameter is not None:
			#private variable for block return type (string)
			return_type = ""

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
			self.function_reference_table.insert(block_name_parameter,block_data)

	def add_block_return_type(self, key, block_return_type_parameter = None):
		#Key should have value
		if block_return_type_parameter is not None:
			self.function_reference_table[key][0] = block_return_type_parameter

	#print block information for all blocks
	def print_table(self):
		#
		print(self.function_reference_table)

if __name__ == '__main__':
	directory = Function_Directory()

	directory.add_block_name("Block1")
	directory.add_block_name("Block2")

	
	directory.add_block_name("Block1")
	directory.add_block_name("Block2")

	directory.print_table()
	