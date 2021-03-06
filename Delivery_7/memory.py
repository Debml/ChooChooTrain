"""Collection of classes for memory storage and management,
contains memory implementations,
memory handling, and other functions 
as detailed in the class"""
import constants
import structures

"""Contains the blocks of memory for local and temporary variables"""
class Block_Memory:
	def __init__(self, lc = None, tc = None):
		if lc is not None:
			if tc is not None:
				#counter for local variables memory
				self._local_counter = lc
				#starting position for [whole, decimal, words, boolean] variables
				self._local_ranges = constants.Memory_Limits.LOCAL_RANGES
				#size of each local variable partition
				self._local_size = constants.Memory_Limits.LOCAL_SIZE

				#counter for temporary variable memory
				self._temporary_counter = tc
				#starting position for [whole, decimal, words, boolean] temporary variables
				self._temporary_ranges = constants.Memory_Limits.TEMPORARY_RANGES
				#size of each temporary variable partition
				self._temporary_size = constants.Memory_Limits.TEMPORARY_SIZE

				#local memory array
				self._local_whole_memory = [None]*lc[0]
				self._local_decimal_memory = [None]*lc[1]
				self._local_words_memory = [None]*lc[2]
				self._local_boolean_memory = [None]*lc[3]

				#temporary memory arrays 7000-12999
				self._temporary_whole_memory = [None]*tc[0]
				self._temporary_decimal_memory = [None]*tc[1]
				self._temporary_words_memory = [None]*tc[2]
				self._temporary_boolean_memory = [None]*tc[3]

	#get value from local memory
	def read_from_local_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._local_ranges[0] and address <= (self._local_ranges[0]+self._local_counter[0]-1):
				#add to memory with offset
				return self._local_whole_memory[address-self._local_ranges[0]]

			#address belongs to decimal memory already assigned
			if address >= self._local_ranges[1] and address <= (self._local_ranges[1]+self._local_counter[1]-1):
				#add to memory with offset
				return self._local_decimal_memory[address-self._local_ranges[1]]

			#address belongs to words memory already assigned
			if address >= self._local_ranges[2] and address <= (self._local_ranges[2]+self._local_counter[2]-1):
				#add to memory with offset
				return self._local_words_memory[address-self._local_ranges[2]]

			#address belongs to boolean memory already assigned
			if address >= self._local_ranges[3] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
				#add to memory with offset
				return self._local_boolean_memory[address-self._local_ranges[3]]

	#get value from temporary memory
	def read_from_temporary_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[0] + self._temporary_counter[0] - 1):
				#add to memory with offset
				return self._temporary_whole_memory[address-self._temporary_ranges[0]]

			#address belongs to decimal memory already assigned
			if address >= self._temporary_ranges[1] and address <= (self._temporary_ranges[1] + self._temporary_counter[1] - 1):
				#add to memory with offset
				return self._temporary_decimal_memory[address-self._temporary_ranges[1]]

			#address belongs to words memory already assigned
			if address >= self._temporary_ranges[2] and address <= (self._temporary_ranges[2] + self._temporary_counter[2] - 1):
				#add to memory with offset
				return self._temporary_words_memory[address-self._temporary_ranges[2]]

			#address belongs to boolean memory already assigned
			if address >= self._temporary_ranges[3] and address <= (self._temporary_ranges[3] + self._temporary_counter[3] - 1):
				#add to memory with offset
				return self._temporary_boolean_memory[address-self._temporary_ranges[3]]
			else:
				return None

	#add value for local memory, size is 500
	def write_to_local_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._local_ranges[0] and address <= (self._local_ranges[0]+self._local_counter[0]-1):
					#add to memory with offset
					self._local_whole_memory[address-self._local_ranges[0]] = value

				#address belongs to decimal memory already assigned
				elif address >= self._local_ranges[1] and address <= (self._local_ranges[1]+self._local_counter[1]-1):
					#add to memory with offset
					self._local_decimal_memory[address-self._local_ranges[1]] = value

				#address belongs to words memory already assigned
				elif address >= self._local_ranges[2] and address <= (self._local_ranges[2]+self._local_counter[2]-1):
					#add to memory with offset
					self._local_words_memory[address-self._local_ranges[2]] = value

				#address belongs to boolean memory already assigned
				elif address >= self._local_ranges[3] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
					#add to memory with offset
					self._local_boolean_memory[address-self._local_ranges[3]] = value

				else:
    				#error
					return False
				
				return True

	#add value for temporary memory, size is 1500
	def write_to_temporary_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[0]+self._temporary_counter[0]-1):
					#add to memory with offset
					self._temporary_whole_memory[address-self._temporary_ranges[0]] = value

				#address belongs to decimal memory already assigned
				elif address >= self._temporary_ranges[1] and address <= (self._temporary_ranges[1]+self._temporary_counter[1]-1):
					#add to memory with offset
					self._temporary_decimal_memory[address-self._temporary_ranges[1]] = value

				#address belongs to words memory already assigned
				elif address >= self._temporary_ranges[2] and address <= (self._temporary_ranges[2]+self._temporary_counter[2]-1):
					#add to memory with offset
					self._temporary_words_memory[address-self._temporary_ranges[2]] = value

				#address belongs to boolean memory already assigned
				elif address >= self._temporary_ranges[3] and address <= (self._temporary_ranges[3]+self._temporary_counter[3]-1):
					#add to memory with offset
					self._temporary_boolean_memory[address-self._temporary_ranges[3]] = value

				else:
    				#error
					return False
				
				return True

	#Overrides print method
	def print_method(self):
		printlist = []

		printlist.append('\n\nLocal Whole Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._local_whole_memory))
		printlist.append('\n\nLocal Decimal Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._local_decimal_memory))
		printlist.append('\n\nLocal Words Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._local_words_memory))
		printlist.append('\n\nLocal Boolean Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._local_boolean_memory))
		printlist.append('\n\nTemporary Whole Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._temporary_whole_memory))
		printlist.append('\n\nTemporary Decimal Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._temporary_decimal_memory))
		printlist.append('\n\nTemporary Words Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._temporary_words_memory))
		printlist.append('\n\nTemporary Boolean Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._temporary_boolean_memory))

		s = ''.join(printlist)

		return (s)
		
'''Verifies the memory limits and assigns an address to a variable/temporary/constant'''
class Memory_Handler:
	def __init__(self):
		#counter for local variables memory per block
		self._local_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] variables
		self._local_ranges = constants.Memory_Limits.LOCAL_RANGES
		#size of each local variable partition
		self._local_size = constants.Memory_Limits.LOCAL_SIZE

		#counter for temporary variable memory per block
		self._temporary_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] temporary variables
		self._temporary_ranges = constants.Memory_Limits.TEMPORARY_RANGES
		#size of each temporary variable partition
		self._temporary_size = constants.Memory_Limits.TEMPORARY_SIZE

		#counter for constant memory
		self._constant_counter = [0, 0, 0, 0]
		#starting position for [whole, decimal, words, boolean] constants
		self._constant_ranges = constants.Memory_Limits.CONSTANT_RANGES
		#size of each constant partition
		self._constant_size = constants.Memory_Limits.CONSTANT_SIZE
		
	#Assign memory address of local variable/list and return it, blocks to assign is 1 for variable, list_size of lists
	def assign_memory_address_local_variable(self, variable_type = None, blocks_to_assign = None):
		#variable_type should have value
		if variable_type is not None:
			#blocks_to_assign should have value
			if blocks_to_assign is not None:
				#memory address for whole
				if variable_type == constants.Data_Types.WHOLE:
					index = 0

				#memory address for decimal
				elif variable_type == constants.Data_Types.DECIMAL:
					index = 1

				#memory address for words
				elif variable_type == constants.Data_Types.WORDS:
					index = 2

				#memory address for boolean
				elif variable_type == constants.Data_Types.BOOLEAN:
					index = 3

				#does not recognize variable type
				else:
					return -2

				if not self.local_memory_is_full_for_data_type(variable_type, blocks_to_assign):
					address = (self._local_ranges[index] + self._local_counter[index])
					self._local_counter[index] = self._local_counter[index] + blocks_to_assign
					return address
				else:
					return -1	

	#Assign memory address of temporary variable and return it
	def assign_memory_address_temporary_variable(self, variable_type = None):
		#variable_type should have value
		if variable_type is not None:
			#memory address for whole
			if variable_type == constants.Data_Types.WHOLE:
				index = 0

			#memory address for decimal
			elif variable_type == constants.Data_Types.DECIMAL:
				index = 1

			#memory address for words
			elif variable_type == constants.Data_Types.WORDS:
				index = 2

			#memory address for boolean
			elif variable_type == constants.Data_Types.BOOLEAN:
				index = 3

			#does not recognize variable type
			else:
				return -2

			if not self.temporary_memory_is_full_for_data_type(variable_type):
				address = (self._temporary_ranges[index] + self._temporary_counter[index])
				self._temporary_counter[index] = self._temporary_counter[index] + 1
				return address
			else:
				return -1

	#Assign memory address of constant and return it
	def assign_memory_address_constant(self, constant_type = None):
		#constant_type should have value
		if constant_type is not None:
			#memory address for constant whole
			if constant_type == constants.Data_Types.WHOLE:
				index = 0

			#memory address for constant decimal
			elif constant_type == constants.Data_Types.DECIMAL:
				index = 1

			#memory address for constant words
			elif constant_type == constants.Data_Types.WORDS:
				index = 2

			#memory address for constant boolean
			elif constant_type == constants.Data_Types.BOOLEAN:
				index = 3

			#does not recognize constant type
			else:
				return -1

			if not self.constant_memory_is_full_for_data_type(constant_type):
				address = (self._constant_ranges[index] + self._constant_counter[index])
				self._constant_counter[index] = self._constant_counter[index] + 1
				return address
			else:
				return -1	

	#Returns the constant counter for each data type
	def get_constant_counter(self):
		return self._constant_counter	

	#Resets the local variable counter for each data type
	def reset_local_counter(self):
		#counter for local variables memory
		temp_local_counter = self._local_counter
		self._local_counter = [0, 0, 0, 0]
		return temp_local_counter	

	#Resets the temporary variable counter for each data type
	def reset_temporary_counter(self):
		#counter for temporary variables memory
		temp_temporary_counter = self._temporary_counter
		self._temporary_counter = [0, 0, 0, 0]
		return temp_temporary_counter

	#Returns true if the counter for the given data type exceeds the size allocated for local variables
	def local_memory_is_full_for_data_type(self, data_type, blocks):
		if data_type == constants.Data_Types.WHOLE:
			index = 0
		elif data_type == constants.Data_Types.DECIMAL:
			index = 1
		elif data_type == constants.Data_Types.WORDS:
			index = 2
		elif data_type == constants.Data_Types.BOOLEAN:
			index = 3
		else:
			return None
		
		#Takes into account the variable (or list) about to be added
		if self._local_counter[index] + blocks > self._local_size:
			return True
		else:
			return False

	#Returns true if the counter for the given data type exceeds the size allocated for temporary variables
	def temporary_memory_is_full_for_data_type(self, data_type):
		if data_type == constants.Data_Types.WHOLE:
			index = 0
		elif data_type == constants.Data_Types.DECIMAL:
			index = 1
		elif data_type == constants.Data_Types.WORDS:
			index = 2
		elif data_type == constants.Data_Types.BOOLEAN:
			index = 3
		else:
			return None

		#Takes into account the temporary variable about to be added
		if self._temporary_counter[index] + 1 > self._temporary_size:
			return True
		else:
			return False

	#Returns true if the counter for the given data type exceeds the size allocated for constants
	def constant_memory_is_full_for_data_type(self, data_type):
		if data_type == constants.Data_Types.WHOLE:
			index = 0
		elif data_type == constants.Data_Types.DECIMAL:
			index = 1
		elif data_type == constants.Data_Types.WORDS:
			index = 2
		elif data_type == constants.Data_Types.BOOLEAN:
			index = 3
		else:
			return None

		#Takes into account the constant about to be added
		if self._constant_counter[index] + 1 > self._constant_size:
			return True
		else:
			return False

	#Returns the address of a parameter given its type and the counter of read parameters
	def get_parameter_address(self, parameter_type, param_counter):
		if parameter_type == constants.Data_Types.WHOLE:
			index = 0
		elif parameter_type == constants.Data_Types.DECIMAL:		
			index = 1
		elif parameter_type == constants.Data_Types.WORDS:
			index = 2
		elif parameter_type == constants.Data_Types.BOOLEAN:
			index = 3

		address = self._local_ranges[index] + param_counter[index]
		return address
'''Contains the quad list, the activation records, and the constant table'''
class Program_Memory:
	def __init__(self, quad_list = None, starting_activation_record = None, cc = None, constant_table = None):
		if quad_list is not None:
			if starting_activation_record is not None:
				if cc is not None:
					if constant_table is not None:
						#program memory 0-4999, read only
						self._quad_memory = quad_list	

						#starting position for [whole, decimal, words, boolean] variables
						self._local_ranges = constants.Memory_Limits.LOCAL_RANGES
						#size of each local variable partition
						self._local_size = constants.Memory_Limits.LOCAL_SIZE

						#starting position for [whole, decimal, words, boolean] temporary variables
						self._temporary_ranges = constants.Memory_Limits.TEMPORARY_RANGES
						#size of each temporary variable partition
						self._temporary_size = constants.Memory_Limits.TEMPORARY_SIZE

						#stack of activation records, top of the stack holds the memory for 5000-6999 (local variables)
						#and 7000-12999 (temporary variables) for the current block
						#The stack is only allowed to hold 500 activations record (1 active + 499 pending)
						self._stack_segment = structures.Stack()
						self._stack_segment.push(starting_activation_record)
						self._stack_segment_limit = constants.Memory_Limits.STACK_SEGMENT_SIZE

						#counter for constant memory
						self._constant_counter = cc
						#starting position for [whole, decimal, words, boolean] constants
						self._constant_ranges = constants.Memory_Limits.CONSTANT_RANGES
						#size of each constant partition
						self._constant_size = constants.Memory_Limits.CONSTANT_SIZE
						
						#constant memory arrays 13000-16999
						self._constant_whole_memory = [None]*cc[0]
						self._constant_decimal_memory = [None]*cc[1]
						self._constant_words_memory = [None]*cc[2]
						self._constant_boolean_memory = [None]*cc[3]
						self.initialize_constant_memory(constant_table)

	#gets a quad in a given index from memory
	def get_quad_from_memory(self, index = None):
		#index must not be empty
		if index is not None:
			#check if index is valid for a quad
			if index >= 0 and index < constants.Memory_Limits.QUAD_SIZE:
				#return quad
				return self._quad_memory.get_quad(index)

	#Transforms the constant table from a dictionary to an array
	def initialize_constant_memory(self, constant_table = None):
		if constant_table is not None:
			for k, v in constant_table.get_instance().items():
				self.write_to_memory(k, v[1])

	#Reads a value from  memory
	def read_from_memory(self, address = None):
		#address must not be empty
		if address is not None:
			#address is special character for memory location
			if str(address)[0] == '&':
				#return addres
				num = int(address[1:])
				return num

			#address is special character for memory location
			elif str(address)[0] == '*':
				num = int(address[1:])
				return self.read_from_memory(self.read_from_memory(num))

			#address is regular address
			else:	
				#read from current (top of stack) activation record's local memory
				if address >= self._local_ranges[0] and address < (self._local_ranges[3] + self._local_size):
					current_activation_record = self._stack_segment.peek()
					value = current_activation_record.get_block_memory().read_from_local_memory(address)
					return value

				#read from current (top of stack) activation record's temporary memory
				elif address >= self._temporary_ranges[0] and address < (self._temporary_ranges[3] + self._temporary_size):
					current_activation_record = self._stack_segment.peek()
					value = current_activation_record.get_block_memory().read_from_temporary_memory(address)
					return value

				#read from constant table
				elif address >= self._constant_ranges[0] and address < (self._constant_ranges[3] + self._constant_counter[3] - 1):
					#add memory to constant
					value = self._read_from_constant_memory(address)
					return value

				else:
					#error
					return None

	#Reads a value from constant memory
	def _read_from_constant_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._constant_ranges[0] and address <= (self._constant_ranges[0]+self._constant_counter[0]-1):
				#add to memory with offset
				return self._constant_whole_memory[address-self._constant_ranges[0]]

			#address belongs to decimal memory already assigned
			if address >= self._constant_ranges[1] and address <= (self._constant_ranges[1]+self._constant_counter[1]-1):
				#add to memory with offset
				return self._constant_decimal_memory[address-self._constant_ranges[1]]

			#address belongs to words memory already assigned
			if address >= self._constant_ranges[2] and address <= (self._constant_ranges[2]+self._constant_counter[2]-1):
				#add to memory with offset
				return self._constant_words_memory[address-self._constant_ranges[2]][1:-1]

			#address belongs to boolean memory already assigned
			if address >= self._constant_ranges[3] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
				#add to memory with offset
				return self._constant_boolean_memory[address-self._constant_ranges[3]]

	#Writes a value to memory
	def write_to_memory(self, value = None, address = None):
		#value must not be empty
		if value is not None:
			#address must not be empty
			if address is not None:
				#Normalize address if it is a pointer or an address as a constant
				if str(address)[0] == '*' or str(address)[0] == '&':
					address = int(address[1:])

				#address is valid in range of writeable memory already assigned for locals
				if address >= self._local_ranges[0] and address < (self._local_ranges[3] + self._local_size):
					#add memory to local
					current_activation_record = self._stack_segment.peek()
					return current_activation_record.get_block_memory().write_to_local_memory(value, address)

				elif address >= self._temporary_ranges[0] and address < (self._temporary_ranges[3] + self._temporary_size):
					#add memory to temporary
					current_activation_record = self._stack_segment.peek()
					return current_activation_record.get_block_memory().write_to_temporary_memory(value, address)

				elif address >= self._constant_ranges[0] and address <= (self._constant_ranges[3] + self._constant_counter[3]-1):
					#add memory to constant
					return self._write_to_constant_memory(value, address)

				else:
					#Error
					return False

	#Writes a value to constant memory
	def _write_to_constant_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._constant_ranges[0] and address <= (self._constant_ranges[0]+self._constant_counter[0]-1):
					#add to memory with offset
					self._constant_whole_memory[address - self._constant_ranges[0]] = value

				#address belongs to decimal memory already assigned
				elif address >= self._constant_ranges[1] and address <= (self._constant_ranges[1]+self._constant_counter[1]-1):
					#add to memory with offset
					self._constant_decimal_memory[address - self._constant_ranges[1]] = value

				#address belongs to words memory already assigned
				elif address >= self._constant_ranges[2] and address <= (self._constant_ranges[2]+self._constant_counter[2]-1):
					#add to memory with offset
					self._constant_words_memory[address - self._constant_ranges[2]] = value

				#address belongs to boolean memory already assigned
				elif address >= self._constant_ranges[3] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
					#add to memory with offset
					self._constant_boolean_memory[address - self._constant_ranges[3]] = value

				else:
    				#error
					return False
				
				return True

	#returns the current (top of the stack) activation record
	def get_current_activation_record(self):
		return self._stack_segment.peek()

	#returns the return value of the block
	def remove_current_activation_record(self):
		return self._stack_segment.pop()

	#adds a new activation record to the stack
	def add_activation_record(self, activation_record = None):
		if activation_record is not None:
			if not self.stack_segment_is_full():
				self._stack_segment.push(activation_record)
				return True
			else:
				return False

	#verifies that the number of activation records in the stack is not bigger than the limit
	def stack_segment_is_full(self):
		if self._stack_segment.size() >= self._stack_segment_limit:
			return True
		else:
			return False

	#Returns true if there are no more activation records on the stack
	def stack_segment_is_empty(self):
		if self._stack_segment.empty():
			return True
		else:
			return False

