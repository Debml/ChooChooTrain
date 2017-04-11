import constants

"""Module for memory handling, contains memory implementations,
memory handling, and other functions as detailed in the class"""
class Memory_Handler:
	def __init__(self):
		#counter for local variables memory
		self._local_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] variables
		self._local_ranges = [5000, 5500, 6000, 6500]
		#size of each local variable partition
		self._local_size = 500

		#counter for temporary variable memory
		self._temporary_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] temporary variables
		self._temporary_ranges = [7000, 8500, 10000, 11500]
		#size of each temporary variable partition
		self._temporary_size = 1500

		#counter for constant memory
		self._constant_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] constants
		self._constant_ranges = [13000, 14000, 15000, 16000]
		#size of each constant partition
		self._constant_size = 1000

		#counter for global variables memory
		self._global_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] global variables
		self._global_ranges = [17000, 17500, 18000, 18500]
		#size of each global variable partition
		self._global_size = 500

	#Assign memory address of local variable/list and return it
	def _assign_memory_address_local_variable(self, variable_type = None, blocks_to_assign = None):
		#variable_type should have value
		if variable_type is not None:
			#blocks_to_assign should have value
			if blocks_to_assign is not None:
				#memory address for whole
				if(variable_type == constants.DataTypes.WHOLE):
					address = (self._local_ranges[0] + self._local_counter[0])
					self._local_counter[0] = self._local_counter[0] + blocks_to_assign
					return address

				#memory address for decimal
				elif(variable_type == constants.DataTypes.DECIMAL):
					address = (self._local_ranges[1] + self._local_counter[1])
					self._local_counter[1] = self._local_counter[1] + blocks_to_assign
					return address

				#memory address for words
				elif(variable_type == constants.DataTypes.WORDS):
					address = (self._local_ranges[2] + self._local_counter[2])
					self._local_counter[2] = self._local_counter[2] + blocks_to_assign
					return address

				#memory address for boolean
				elif(variable_type == constants.DataTypes.BOOLEAN):
					address = (self._local_ranges[3] + self._local_counter[3])
					self._local_counter[3] = self._local_counter[3] + blocks_to_assign
					return address

				#does not recognize variable type
				else:
					return -1

	#Assign memory address of temporary variable and return it
	def _assign_memory_address_temporary_variable(self, variable_type = None):
		#variable_type should have value
		if variable_type is not None:
			#memory address for whole
			if(variable_type == constants.DataTypes.WHOLE):
				address = (self._temporary_ranges[0] + self._temporary_counter[0])
				self._temporary_counter[0] = self._temporary_counter[0] + 1
				return address

			#memory address for decimal
			elif(variable_type == constants.DataTypes.DECIMAL):
				address = (self._temporary_ranges[1] + self._temporary_counter[1])
				self._temporary_counter[1] = self._temporary_counter[1] + 1
				return address

			#memory address for words
			elif(variable_type == constants.DataTypes.WORDS):
				address = (self._temporary_ranges[2] + self._temporary_counter[2])
				self._temporary_counter[2] = self._temporary_counter[2] + 1
				return address

			#memory address for boolean
			elif(variable_type == constants.DataTypes.BOOLEAN):
				address = (self._temporary_ranges[3] + self._temporary_counter[3])
				self._temporary_counter[3] = self._temporary_counter[3] + 1
				return address

			#does not recognize variable type
			else:
				return -1

	#Assign memory address of constant and return it
	def _assign_memory_address_constant(self, constant_type = None):
		#constant_type should have value
		if constant_type is not None:
			#memory address for constant whole
			if(constant_type == "cst_whole"):
				address = (self._constant_ranges[0] + self._constant_counter[0])
				self._constant_counter[0] = self._constant_counter[0] + 1
				return address

			#memory address for constant decimal
			elif(constant_type == "cst_decimal"):
				address = (self._constant_ranges[1] + self._constant_counter[1])
				self._constant_counter[1] = self._constant_counter[1] + 1
				return address

			#memory address for constant words
			elif(constant_type == "cst_words"):
				address = (self._constant_ranges[2] + self._constant_counter[2])
				self._constant_counter[2] = self._constant_counter[2] + 1
				return address

			#memory address for constant boolean
			elif(constant_type == "cst_boolean"):
				address = (self._constant_ranges[3] + self._constant_counter[3])
				self._constant_counter[3] = self._constant_counter[3] + 1
				return address

			#does not recognize constant type
			else:
				return -1