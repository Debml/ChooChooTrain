"""Collection of classes for memory storage and management,
contains memory implementations,
memory handling, and other functions 
as detailed in the class"""
import constants
from structures import Quad_List
from structures import Dictionary

"""Contains actual memory arrays to manage"""
class Memory_Section:
	def __init__(self):
		#program memory 0-4999, read only
		self._quad_memory = Quad_List()	

		#local memory arrays 5000-6999
		self._local_whole_memory = []
		self._local_decimal_memory = []
		self._local_words_memory = []
		self._local_boolean_memory = []

		#temporary memory arrays 7000-12999
		self._temporary_whole_memory = []
		self._temporary_decimal_memory = []
		self._temporary_words_memory = []
		self._temporary_boolean_memory = []

		#constant memory arrays 13000-16999
		self._constant_whole_memory = []
		self._constant_decimal_memory = []
		self._constant_words_memory = []
		self._constant_boolean_memory = []

		#global memory arrays 17000-18999
		self._global_whole_memory = []
		self._global_decimal_memory = []
		self._global_words_memory = []
		self._global_boolean_memory = []

	#add variable to local whole memory
	def add_to_local_whole_memory(self, value = None, offset_address = None):
		#add to local whole memory
		self._local_whole_memory[offset_address] = value

	#add variable to local decimal memory
	def add_to_local_decimal_memory(self, value = None, offset_address = None):
		#add to local decimal memory
		self._local_decimal_memory[offset_address] = value

	#add variable to local words memory
	def add_to_local_words_memory(self, value = None, offset_address = None):
		#add to local words memory
		self._local_words_memory[offset_address] = value

	#add variable to local boolean memory
	def add_to_local_boolean_memory(self, value = None, offset_address = None):
		#add to local boolean memory
		self._local_boolean_memory[offset_address] = value

	#add variable to temporary whole memory
	def add_to_temporary_whole_memory(self, value = None, offset_address = None):
		#add to temporary whole memory
		self._temporary_whole_memory[offset_address] = value

	#add variable to temporary decimal memory
	def add_to_temporary_decimal_memory(self, value = None, offset_address = None):
		#add to temporary decimal memory
		self._temporary_decimal_memory[offset_address] = value

	#add variable to temporary words memory
	def add_to_temporary_words_memory(self, value = None, offset_address = None):
		#add to temporary words memory
		self._temporary_words_memory[offset_address] = value

	#add variable to temporary boolean memory
	def add_to_temporary_boolean_memory(self, value = None, offset_address = None):
		#add to temporary boolean memory
		self._temporary_boolean_memory[offset_address] = value

	#add variable to constant whole memory
	def add_to_constant_whole_memory(self, value = None, offset_address = None):
		#add to constant whole memory
		self._constant_whole_memory[offset_address] = value

	#add variable to constant decimal memory
	def add_to_constant_decimal_memory(self, value = None, offset_address = None):
		#add to constant decimal memory
		self._constant_decimal_memory[offset_address] = value

	#add variable to constant words memory
	def add_to_constant_words_memory(self, value = None, offset_address = None):
		#add to constant words memory
		self._constant_words_memory[offset_address] = value

	#add variable to constant boolean memory
	def add_to_constant_boolean_memory(self, value = None, offset_address = None):
		#add to constant boolean memory
		self._constant_boolean_memory[offset_address] = value

	#add variable to global whole memory
	def add_to_global_whole_memory(self, value = None, offset_address = None):
		#add to global whole memory
		self._global_whole_memory[offset_address] = value

	#add variable to global decimal memory
	def add_to_global_decimal_memory(self, value = None, offset_address = None):
		#add to global decimal memory
		self._global_decimal_memory[offset_address] = value

	#add variable to global words memory
	def add_to_global_words_memory(self, value = None, offset_address = None):
		#add to global words memory
		self._global_words_memory[offset_address] = value

	#add variable to global boolean memory
	def add_to_global_boolean_memory(self, value = None, offset_address = None):
		#add to global boolean memory
		self._global_boolean_memory[offset_address] = value

	#get variable from local whole memory
	def get_from_local_whole_memory(self, offset_address = None):
		#get from local whole memory
		return self._local_whole_memory[offset_address]

	#get variable from local decimal memory
	def get_from_local_decimal_memory(self, offset_address = None):
		#get from local decimal memory
		return self._local_decimal_memory[offset_address]

	#get variable from local words memory
	def get_from_local_words_memory(self, offset_address = None):
		#get from local words memory
		return self._local_words_memory[offset_address]

	#get variable from local boolean memory
	def get_from_local_boolean_memory(self, offset_address = None):
		#get from local boolean memory
		return self._local_boolean_memory[offset_address]

	#get variable from temporary whole memory
	def get_from_temporary_whole_memory(self, offset_address = None):
		#get from temporary whole memory
		return self._temporary_whole_memory[offset_address]

	#get variable from temporary decimal memory
	def get_from_temporary_decimal_memory(self, offset_address = None):
		#get from temporary decimal memory
		return self._temporary_decimal_memory[offset_address]

	#get variable from temporary words memory
	def get_from_temporary_words_memory(self, offset_address = None):
		#get from temporary words memory
		return self._temporary_words_memory[offset_address]

	#get variable from temporary boolean memory
	def get_from_temporary_boolean_memory(self, offset_address = None):
		#get from temporary boolean memory
		return self._temporary_boolean_memory[offset_address]

	#get variable from constant whole memory
	def get_from_constant_whole_memory(self, offset_address = None):
		#get from constant whole memory
		return self._constant_whole_memory[offset_address]

	#get variable from constant decimal memory
	def get_from_constant_decimal_memory(self, offset_address = None):
		#get from constant decimal memory
		return self._constant_decimal_memory[offset_address]

	#get variable from constant words memory
	def get_from_constant_words_memory(self, offset_address = None):
		#get from constant words memory
		return self._constant_words_memory[offset_address]

	#get variable from constant boolean memory
	def get_from_constant_boolean_memory(self, offset_address = None):
		#get from constant boolean memory
		return self._constant_boolean_memory[offset_address]

	#get variable from global whole memory
	def get_from_global_whole_memory(self, offset_address = None):
		#get from global whole memory
		return self._global_whole_memory[offset_address]

	#get variable from global decimal memory
	def get_from_global_decimal_memory(self, offset_address = None):
		#get from global decimal memory
		return self._global_decimal_memory[offset_address]

	#get variable from global words memory
	def get_from_global_words_memory(self, offset_address = None):
		#get from global words memory
		return self._global_words_memory[offset_address]

	#get variable from global boolean memory
	def get_from_global_boolean_memory(self, offset_address = None):
		#get from global boolean memory
		return self._global_boolean_memory[offset_address]
			
	#add to quad memory
	def upload_quads_to_memory(self, quad_list_to_copy = None):
		#quad must not be empty
		if quad_list_to_copy is not None:
			#upload to memory
			self._quad_memory = quad_list_to_copy

	#get quad from memory
	def get_quad_from_memory(self, index = None):
		#index must not be empty
		if index is not None:
			#return quad
			return self._quad_memory.get_quad(index)
	#receives counters for arrays and initializes
	def activate(self, lc, tc, cc, gc):
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

		#constant memory arrays 13000-16999
		self._constant_whole_memory = [None]*cc[0]
		self._constant_decimal_memory = [None]*cc[1]
		self._constant_words_memory = [None]*cc[2]
		self._constant_boolean_memory = [None]*cc[3]

		#global memory arrays 17000-18999
		self._global_whole_memory = [None]*gc[0]
		self._global_decimal_memory = [None]*gc[1]
		self._global_words_memory = [None]*gc[2]
		self._global_boolean_memory = [None]*gc[3]

	#Overrides print method
	def print_method(self):
		printlist = []
		printlist.append('Quad Memory:\n')
		printlist.append(self._quad_memory.print_method())
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
		printlist.append('\n\nConstant Whole Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._constant_whole_memory))
		printlist.append('\n\nConstant Decimal Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._constant_decimal_memory))
		printlist.append('\n\nConstant Words Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._constant_words_memory))
		printlist.append('\n\nConstant Boolean Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._constant_boolean_memory))
		printlist.append('\n\nGlobal Whole Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._global_whole_memory))
		printlist.append('\n\nGlobal Decimal Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._global_decimal_memory))
		printlist.append('\n\nGlobal Words Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._global_words_memory))
		printlist.append('\n\nGlobal Boolean Memory:\n')
		printlist.append('\n'.join(str(e) for e in self._global_boolean_memory))

		s = ''.join(printlist)

		return (s)
		
class Memory_Handler:
	def __init__(self):
    	#Memory section instance that stores values
		self._memory = Memory_Section()

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
		
	#Assign memory address of local variable/list and return it, blocks to assign is 1 for variable
	def assign_memory_address_local_variable(self, variable_type = None, blocks_to_assign = None):
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
	def assign_memory_address_temporary_variable(self, variable_type = None):
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
	def assign_memory_address_constant(self, constant_type = None):
		#constant_type should have value
		if constant_type is not None:
			#memory address for constant whole
			if(constant_type == constants.DataTypes.WHOLE):
				address = (self._constant_ranges[0] + self._constant_counter[0])
				self._constant_counter[0] = self._constant_counter[0] + 1
				return address

			#memory address for constant decimal
			elif(constant_type == constants.DataTypes.DECIMAL):
				address = (self._constant_ranges[1] + self._constant_counter[1])
				self._constant_counter[1] = self._constant_counter[1] + 1
				return address

			#memory address for constant words
			elif(constant_type == constants.DataTypes.WORDS):
				address = (self._constant_ranges[2] + self._constant_counter[2])
				self._constant_counter[2] = self._constant_counter[2] + 1
				return address

			#memory address for constant boolean
			elif(constant_type == constants.DataTypes.BOOLEAN):
				address = (self._constant_ranges[3] + self._constant_counter[3])
				self._constant_counter[3] = self._constant_counter[3] + 1
				return address

			#does not recognize constant type
			else:
				return -1

	#Assign memory address of global variable/list and return it, blocks to assign is 1 for variable
	def assign_memory_address_global_variable(self, variable_type = None, blocks_to_assign = None):
		#variable_type should have value
		if variable_type is not None:
			#blocks_to_assign should have value
			if blocks_to_assign is not None:
				#memory address for whole
				if(variable_type == constants.DataTypes.WHOLE):
					address = (self._global_ranges[0] + self._global_counter[0])
					self._global_counter[0] = self._global_counter[0] + blocks_to_assign
					return address

				#memory address for decimal
				elif(variable_type == constants.DataTypes.DECIMAL):
					address = (self._global_ranges[1] + self._global_counter[1])
					self._global_counter[1] = self._global_counter[1] + blocks_to_assign
					return address

				#memory address for words
				elif(variable_type == constants.DataTypes.WORDS):
					address = (self._global_ranges[2] + self._global_counter[2])
					self._global_counter[2] = self._global_counter[2] + blocks_to_assign
					return address

				#memory address for boolean
				elif(variable_type == constants.DataTypes.BOOLEAN):
					address = (self._global_ranges[3] + self._global_counter[3])
					self._global_counter[3] = self._global_counter[3] + blocks_to_assign
					return address

				#does not recognize variable type
				else:
					return -1

					
	#upload quads
	def upload_quads_to_memory(self, quad_list_to_copy = None):
		#quad must not be empty
		if quad_list_to_copy is not None:
			#upload to memory
			self._memory.upload_quads_to_memory(quad_list_to_copy)

	#activate memory arrays
	def activate_memory(self, constant_table = None):
		#activate memory
		self._memory.activate(self._local_counter, self._temporary_counter, self._constant_counter, self._global_counter)

		#transfer constants
		if constant_table is not None:
			for k,v in constant_table.get_instance().items():
				self.add_to_memory(k, v[1])

	#get quad from memory
	def get_quad_from_memory(self, index = None):
		#index must not be empty
		if index is not None:
			#check if index is  valid
			if index < 5000 and index >= 0:
				#return quad
				return self._memory.get_quad_from_memory(index)#add value to memory

	#add value to memory arrays
	def add_to_memory(self, value = None, address = None):
		#value must not be empty
		if value is not None:
			#address must not be empty
			if address is not None:
				#address is valid in range of writeable memory already assigned for locals
				if address >= self._local_ranges[0] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
					#add memory to local
					return self._add_to_local_memory(value, address)

				elif address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[3]+self._temporary_counter[3]-1):
					#add memory to temporary
					return self._add_to_temporary_memory(value, address)

				elif address >= self._constant_ranges[0] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
					#add memory to constant
					return self._add_to_constant_memory(value, address)

				elif address >= self._global_ranges[0] and address <= (self._global_ranges[3]+self._global_counter[3]-1):
					#add memory to global
					return self._add_to_global_memory(value, address)

				else:
					#Error
					return False

	#get value from memory
	def get_from_memory(self, address = None):
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
					return self.get_from_memory(self.get_from_memory(num))

				#address is regular address
				else:	
					#address is valid in range of writeable memory already assigned for locals
					if address >= self._local_ranges[0] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
						#add memory to local
						return self._get_from_local_memory(address)

					elif address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[3]+self._temporary_counter[3]-1):
						#add memory to temporary
						return self._get_from_temporary_memory(address)

					elif address >= self._constant_ranges[0] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
						#add memory to constant
						return self._get_from_constant_memory(address)

					elif address >= self._global_ranges[0] and address <= (self._global_ranges[3]+self._global_counter[3]-1):
						#add memory to global
						return self._get_from_global_memory(address)

					else:
						#error
						return None

	#add value for local memory, size is 500
	def _add_to_local_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._local_ranges[0] and address <= (self._local_ranges[0]+self._local_counter[0]-1):
					#add to memory with offset
					self._memory.add_to_local_whole_memory(value, address-self._local_ranges[0])

				#address belongs to decimal memory already assigned
				elif address >= self._local_ranges[1] and address <= (self._local_ranges[1]+self._local_counter[1]-1):
					#add to memory with offset
					self._memory.add_to_local_decimal_memory(value, address-self._local_ranges[1])

				#address belongs to words memory already assigned
				elif address >= self._local_ranges[2] and address <= (self._local_ranges[2]+self._local_counter[2]-1):
					#add to memory with offset
					self._memory.add_to_local_words_memory(value, address-self._local_ranges[2])

				#address belongs to boolean memory already assigned
				elif address >= self._local_ranges[3] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
					#add to memory with offset
					self._memory.add_to_local_boolean_memory(value, address-self._local_ranges[3])

				else:
    				#error
					return False
				
				return True

	#add value for temporary memory, size is 1500
	def _add_to_temporary_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[0]+self._temporary_counter[0]-1):
					#add to memory with offset
					self._memory.add_to_temporary_whole_memory(value, address-self._temporary_ranges[0])

				#address belongs to decimal memory already assigned
				elif address >= self._temporary_ranges[1] and address <= (self._temporary_ranges[1]+self._temporary_counter[1]-1):
					#add to memory with offset
					self._memory.add_to_temporary_decimal_memory(value, address-self._temporary_ranges[1])

				#address belongs to words memory already assigned
				elif address >= self._temporary_ranges[2] and address <= (self._temporary_ranges[2]+self._temporary_counter[2]-1):
					#add to memory with offset
					self._memory.add_to_temporary_words_memory(value, address-self._temporary_ranges[2])

				#address belongs to boolean memory already assigned
				elif address >= self._temporary_ranges[3] and address <= (self._temporary_ranges[3]+self._temporary_counter[3]-1):
					#add to memory with offset
					self._memory.add_to_temporary_boolean_memory(value, address-self._temporary_ranges[3])


				else:
    				#error
					return False
				
				return True

	#add value for constant memory, size is 1000
	def _add_to_constant_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._constant_ranges[0] and address <= (self._constant_ranges[0]+self._constant_counter[0]-1):
					#add to memory with offset
					self._memory.add_to_constant_whole_memory(value, address-self._constant_ranges[0])

				#address belongs to decimal memory already assigned
				elif address >= self._constant_ranges[1] and address <= (self._constant_ranges[1]+self._constant_counter[1]-1):
					#add to memory with offset
					self._memory.add_to_constant_decimal_memory(value, address-self._constant_ranges[1])

				#address belongs to words memory already assigned
				elif address >= self._constant_ranges[2] and address <= (self._constant_ranges[2]+self._constant_counter[2]-1):
					#add to memory with offset
					self._memory.add_to_constant_words_memory(value, address-self._constant_ranges[2])

				#address belongs to boolean memory already assigned
				elif address >= self._constant_ranges[3] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
					#add to memory with offset
					self._memory.add_to_constant_boolean_memory(value, address-self._constant_ranges[3])

				else:
    				#error
					return False
				
				return True

	#add value for global memory, size is 500
	def _add_to_global_memory(self, value = None, address = None):
		#value is not empty
		if value is not None:
			#address not empty
			if address is not None:
				#address belongs to whole memory already assigned
				if address >= self._global_ranges[0] and address <= (self._global_ranges[0]+self._global_counter[0]-1):
					#add to memory with offset
					self._memory.add_to_global_whole_memory(value, address-self._global_ranges[0])

				#address belongs to decimal memory already assigned
				elif address >= self._global_ranges[1] and address <= (self._global_ranges[1]+self._global_counter[1]-1):
					#add to memory with offset
					self._memory.add_to_global_decimal_memory(value, address-self._global_ranges[1])

				#address belongs to words memory already assigned
				elif address >= self._global_ranges[2] and address <= (self._global_ranges[2]+self._global_counter[2]-1):
					#add to memory with offset
					self._memory.add_to_global_words_memory(value, address-self._global_ranges[2])

				#address belongs to boolean memory already assigned
				elif address >= self._global_ranges[3] and address <= (self._global_ranges[3]+self._global_counter[3]-1):
					#add to memory with offset
					self._memory.add_to_global_boolean_memory(value, address-self._global_ranges[3])

				else:
    				#error
					return False
				
				return True

	#get value from local memory
	def _get_from_local_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._local_ranges[0] and address <= (self._local_ranges[0]+self._local_counter[0]-1):
				#add to memory with offset
				return self._memory.get_from_local_whole_memory(address-self._local_ranges[0])

			#address belongs to decimal memory already assigned
			if address >= self._local_ranges[1] and address <= (self._local_ranges[1]+self._local_counter[1]-1):
				#add to memory with offset
				return self._memory.get_from_local_decimal_memory(address-self._local_ranges[1])

			#address belongs to words memory already assigned
			if address >= self._local_ranges[2] and address <= (self._local_ranges[2]+self._local_counter[2]-1):
				#add to memory with offset
				return self._memory.get_from_local_words_memory(address-self._local_ranges[2])

			#address belongs to boolean memory already assigned
			if address >= self._local_ranges[3] and address <= (self._local_ranges[3]+self._local_counter[3]-1):
				#add to memory with offset
				return self._memory.get_from_local_boolean_memory(address-self._local_ranges[3])

	#get value from temporary memory
	def _get_from_temporary_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._temporary_ranges[0] and address <= (self._temporary_ranges[0]+self._temporary_counter[0]-1):
				#add to memory with offset
				return self._memory.get_from_temporary_whole_memory(address-self._temporary_ranges[0])

			#address belongs to decimal memory already assigned
			if address >= self._temporary_ranges[1] and address <= (self._temporary_ranges[1]+self._temporary_counter[1]-1):
				#add to memory with offset
				return self._memory.get_from_temporary_decimal_memory(address-self._temporary_ranges[1])

			#address belongs to words memory already assigned
			if address >= self._temporary_ranges[2] and address <= (self._temporary_ranges[2]+self._temporary_counter[2]-1):
				#add to memory with offset
				return self._memory.get_from_temporary_words_memory(address-self._temporary_ranges[2])

			#address belongs to boolean memory already assigned
			if address >= self._temporary_ranges[3] and address <= (self._temporary_ranges[3]+self._temporary_counter[3]-1):
				#add to memory with offset
				return self._memory.get_from_temporary_boolean_memory(address-self._temporary_ranges[3])

	#get value from constant memory
	def _get_from_constant_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._constant_ranges[0] and address <= (self._constant_ranges[0]+self._constant_counter[0]-1):
				#add to memory with offset
				return self._memory.get_from_constant_whole_memory(address-self._constant_ranges[0])

			#address belongs to decimal memory already assigned
			if address >= self._constant_ranges[1] and address <= (self._constant_ranges[1]+self._constant_counter[1]-1):
				#add to memory with offset
				return self._memory.get_from_constant_decimal_memory(address-self._constant_ranges[1])

			#address belongs to words memory already assigned
			if address >= self._constant_ranges[2] and address <= (self._constant_ranges[2]+self._constant_counter[2]-1):
				#add to memory with offset
				return self._memory.get_from_constant_words_memory(address-self._constant_ranges[2])

			#address belongs to boolean memory already assigned
			if address >= self._constant_ranges[3] and address <= (self._constant_ranges[3]+self._constant_counter[3]-1):
				#add to memory with offset
				return self._memory.get_from_constant_boolean_memory(address-self._constant_ranges[3])

	#get value from global memory
	def _get_from_global_memory(self, address = None):
		#address not empty
		if address is not None:
			#address belongs to whole memory already assigned
			if address >= self._global_ranges[0] and address <= (self._global_ranges[0]+self._global_counter[0]-1):
				#add to memory with offset
				return self._memory.get_from_global_whole_memory(address-self._global_ranges[0])

			#address belongs to decimal memory already assigned
			if address >= self._global_ranges[1] and address <= (self._global_ranges[1]+self._global_counter[1]-1):
				#add to memory with offset
				return self._memory.get_from_global_decimal_memory(address-self._global_ranges[1])

			#address belongs to words memory already assigned
			if address >= self._global_ranges[2] and address <= (self._global_ranges[2]+self._global_counter[2]-1):
				#add to memory with offset
				return self._memory.get_from_global_words_memory(address-self._global_ranges[2])

			#address belongs to boolean memory already assigned
			if address >= self._global_ranges[3] and address <= (self._global_ranges[3]+self._global_counter[3]-1):
				#add to memory with offset
				return self._memory.get_from_global_boolean_memory(address-self._global_ranges[3])
				
	#Overrides print method
	def __str__(self):
		return self._memory.print_method()

#for testing purposes
if __name__ == '__main__':
	MemHand = Memory_Handler()

	ad1 = MemHand.assign_memory_address_local_variable(constants.DataTypes.DECIMAL,1)
	ad2 = MemHand.assign_memory_address_local_variable(constants.DataTypes.DECIMAL,1)
	ad9 = MemHand.assign_memory_address_local_variable(constants.DataTypes.WHOLE,1)		

	ad3 = MemHand.assign_memory_address_temporary_variable(constants.DataTypes.WHOLE)
	ad4 = MemHand.assign_memory_address_temporary_variable(constants.DataTypes.WHOLE)
	ad5 = MemHand.assign_memory_address_temporary_variable(constants.DataTypes.WHOLE)
	ad6 = MemHand.assign_memory_address_temporary_variable(constants.DataTypes.WHOLE)

	a1 = MemHand.assign_memory_address_constant(constants.DataTypes.WHOLE)
	a11 = MemHand.assign_memory_address_constant(constants.DataTypes.WHOLE)

	quadli = Quad_List()
	quadli.append_quad(constants.Operators.OP_ASSIGN, '5', '-1', 'B')
	quadli.append_quad(constants.Operators.OP_ADDITION, '10', '20', 'A')
	quadli.append_quad(constants.Operators.OP_GO_TO, '-1', '20', "pending")
	quadli.append_quad(constants.Operators.OP_GO_TO_T, 'T1', '20', 'D')

	cons = Dictionary()
	cons.insert(33,[constants.DataTypes.WHOLE,a1])
	cons.insert(66,[constants.DataTypes.WHOLE,a11])

	MemHand.upload_quads_to_memory(quadli)
	MemHand.activate_memory(cons)

	MemHand.add_to_memory(1.2, ad1)
	MemHand.add_to_memory(34.2, ad2)
	MemHand.add_to_memory(5500, ad9)

	MemHand.add_to_memory(1, ad3)
	MemHand.add_to_memory(2, ad4)
	MemHand.add_to_memory(4, ad5)
	MemHand.add_to_memory(9, ad6)

	print MemHand.get_from_memory(5500)
	print MemHand.get_from_memory('&5500')
	print MemHand.get_from_memory('*5000')

	print MemHand
	s = 'hello'
	print s[1:]

	