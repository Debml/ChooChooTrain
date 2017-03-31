"""
Collection of classes "structures" containing Stack, Queue, and Dictionary
Author: Paulina Escalante Campbell
January 19, 2016
"""
#import deque for implementation of queue
from collections import deque

"""
Fixed Semantic cube class defining a data structure behving like a semantic
cube where given two operand types and one operator, returns, if operation is valid,
the resulting type of the operation. If not valid, returns None.
"""
class Semantic_Cube:
	#Constructor method
	#Params: -
	#Returns: -
	def __init__(self):
		#operand 2 dictionary
		dictionary_whole = Dictionary()
		dictionary_decimal = Dictionary()
		dictionary_words = Dictionary()
		dictionary_bool = Dictionary()

		#create operator depth for each type
		#whole-whole
		whole_whole_valid_operators = Dictionary()
		whole_whole_valid_operators.insert("op_addition","whole")
		whole_whole_valid_operators.insert("op_subtraction","whole")
		whole_whole_valid_operators.insert("op_multiplication","whole")
		whole_whole_valid_operators.insert("op_division","decimal")

		whole_whole_valid_operators.insert("op_less","boolean")
		whole_whole_valid_operators.insert("op_less_equal","boolean")
		whole_whole_valid_operators.insert("op_greater","boolean")
		whole_whole_valid_operators.insert("op_greater_equal","boolean")
		whole_whole_valid_operators.insert("op_equal","boolean")
		whole_whole_valid_operators.insert("op_not_equal","boolean")
		whole_whole_valid_operators.insert("op_assign","whole")

		#whole-decimal
		whole_decimal_valid_operators = Dictionary()
		whole_decimal_valid_operators.insert("op_addition","decimal")
		whole_decimal_valid_operators.insert("op_subtraction","decimal")
		whole_decimal_valid_operators.insert("op_multiplication","decimal")
		whole_decimal_valid_operators.insert("op_division","decimal")

		whole_decimal_valid_operators.insert("op_less","boolean")
		whole_decimal_valid_operators.insert("op_less_equal","boolean")
		whole_decimal_valid_operators.insert("op_greater","boolean")
		whole_decimal_valid_operators.insert("op_greater_equal","boolean")
		whole_decimal_valid_operators.insert("op_equal","boolean")
		whole_decimal_valid_operators.insert("op_not_equal","boolean")

		#decimal-whole, decimal-decimal
		decimal_valid_operators = Dictionary()
		decimal_valid_operators.insert("op_addition","decimal")
		decimal_valid_operators.insert("op_subtraction","decimal")
		decimal_valid_operators.insert("op_multiplication","decimal")
		decimal_valid_operators.insert("op_division","decimal")

		decimal_valid_operators.insert("op_less","boolean")
		decimal_valid_operators.insert("op_less_equal","boolean")
		decimal_valid_operators.insert("op_greater","boolean")
		decimal_valid_operators.insert("op_greater_equal","boolean")
		decimal_valid_operators.insert("op_equal","boolean")
		decimal_valid_operators.insert("op_not_equal","boolean")
		decimal_valid_operators.insert("op_assign","decimal")

		#words-words
		words_valid_operators = Dictionary()
		words_valid_operators.insert("op_addition","words")
		words_valid_operators.insert("op_equal","boolean")
		words_valid_operators.insert("op_not_equal","boolean")
		words_valid_operators.insert("op_assign","words")

		#bool-bool
		bool_valid_operators = Dictionary()
		bool_valid_operators.insert("op_and","boolean")
		bool_valid_operators.insert("op_or","boolean")		
		bool_valid_operators.insert("op_negation","boolean")	
		bool_valid_operators.insert("op_assign","boolean")	

		#insert operator depth
		dictionary_whole.insert("whole",whole_whole_valid_operators)
		dictionary_whole.insert("decimal",whole_decimal_valid_operators)

		dictionary_decimal.insert("whole",decimal_valid_operators)
		dictionary_decimal.insert("decimal",decimal_valid_operators)

		dictionary_words.insert("words",words_valid_operators)

		dictionary_bool.insert("boolean",bool_valid_operators)

		self.cube = [dictionary_whole,dictionary_decimal,dictionary_words,dictionary_bool]

	#gets operand type code
	def get_operand_type_code(self, operand = None):
		if (operand == "whole"):
			return 0

		elif (operand == "decimal"):
			return 1

		elif (operand == "words"):
			return 2

		elif (operand == "boolean"):
			return 3

		else:
			return -1

	#if valid returns resulting type, if not it returns -1
	def validate_operation(self, operator = None, operand_one_type = None, operand_two_type = None):
		#Parameters must exist
		if operator is not None:
			if operand_one_type is not None:
				#if operator is negation, then operand_two is boolean by default for cube look-up
				if (operator == "op_negation"):
					operand_two_type = "boolean"

				#all operands now have data
				if operand_two_type is not None:
					#get code for operand 
					operand_one_type_code = self.get_operand_type_code(operand_one_type)
					#check static semantic cube for type if not -1
					if operand_one_type_code is not -1:
						#the two operands share a valid operator
						if(self.cube[operand_one_type_code].contains(operand_two_type)):
							#the operator matches
							if(self.cube[operand_one_type_code][operand_two_type].contains(operator)):
								return self.cube[operand_one_type_code][operand_two_type][operator]

							#operator not valid for operands
							else:
								return -1

						#operands do not share a valid operator
						else:
							return -1

"""
Class holds list of quads
"""
class Quad_list:
	def __init__(self):
		self._quads = []
		self._quad_count = 0

	def __str__(self):
		return ('\n'.join('{} \t {}'.format(index,quad) for index, quad in enumerate(self._quads,start = 0)))

	def append_quad(self,operator, left_operand, right_operand, result):
		temp_quad = Quad(operator, left_operand, right_operand, result)
		self._quads.append(temp_quad)
		self._quad_count = self._quad_count + 1

	def set_result(self, quad_index):
		self._quads[quad_index].set_result(self._quad_count)

	def get_quad_count(self):
		return self._quad_count

"""
Quadruple class represents quadruple for intermediate code representation
"""
class Quad:
    def __init__(self, operator = None, left_operand = None, right_operand = None, result = None):
        if operator is not None:
            if left_operand is not None:
                if right_operand is not None: 
                    if result is not None:
                        #private variable for operator code
                        self._operator = operator

                        #private variable for left operand memory address
                        self._left_operand = left_operand

                        #private variable for right operand memory address
                        self._right_operand = right_operand

                        #private variable for quad result memory address
                        self._result = result

    def __str__(self):
    	return ('%s\t\t%s\t%s\t%s' % (self._operator, self._left_operand, self._right_operand, self._result))

    #Returns the quad operator code
    def get_operator(self):
        return self._operator

    #Sets the value of result for a given quad
    def set_result(self, result = None):
    	if result is not None:
    		self._result = result

    #Returns the quad left operand memory address
    def get_left_operand(self):
        return self._left_operand

    #Returns the quad right operand memory address
    def get_right_operand(self):
        return self._right_operand

    #Returns the quad result memory address
    def get_result(self):
        return self._result

    #Prints the information for the specified quad
    def print_quad(self):
        #print("Operator: " + self.get_operator())
        #print("Left Operand: " + self.get_left_operand())
        #print("Right Operand: " + self.get_right_operand())
        #print("Result: " + self.get_result())
		print(self.get_operator(), self.get_left_operand(), self.get_right_operand(), self.get_result())

"""
Dictionary class defining a data structure behaving like hash/table/dict
Key must be inmutable: string, number, tuple
"""
class Dictionary:
	#Constructor method, new empty dictionary
	#Params: -
	#Returns: -
	def __init__(self):
		self._dictionary = {}

	#Returns whether dictionary is empty
	#Params: -
	#Returns: (bool) TRUE if dictionary is empty
	def empty(self):
		return self._dictionary == {}

	#Adds key and item to dictionary
	#Params: key, item
	#Returns: -
	def insert(self,key,item):
		self._dictionary[key] = item

	#Overrides setting element method e.g. dict[key] = x
	#Params: key, item
	#Returns: -
	def __setitem__(self, key, item):
		self._dictionary[key] = item

	#Deletes element with corresponding key, if any
	#Params: key
	#Returns: -
	def erase(self,key):
		if (key in self._dictionary.keys()):
			del self._dictionary[key]

	#Overrides del and deletes element with corresponding key, if any
	#Params: key, item
	#Returns: -
	def __delitem__(self,key):
		if (key in self._dictionary.keys()):
			del self._dictionary[key]

	#Clears all data
	#Params: -
	#Returns: -
	def clear(self):
		self._dictionary.clear()

	#Overrides access element method e.g. dict[key]
	#Params: key
	#Returns: value of item with given key in dictionary
	def __getitem__(self, key):
		val = self._dictionary.__getitem__(key)
		return val

	#Returns size of dictionary
	#Params: -
	#Returns: number of elements in dictionary
	def size(self):
		return len(self._dictionary)

	#Overrides print method, prints alphabetically e.g. print dict
	#Params: -
	#Returns: formatted string containing values of dictionary
	def __str__(self):
		return ('\n'.join('{}: {}'.format(key, val) for key, val in self._dictionary.items()))

	#Returns whether key exists in dictionary or not
	#Params: key
	#Returns: bool TRUE if key exists in dictionary
	def contains(self,key):
		return (key in self._dictionary.keys())

	#Returns whether key exists in dictionary or not
	#Params: key
	#Returns: bool TRUE if key exists in dictionary
	def __contains__(self,key):
		return (key in self._dictionary.keys())

	#Returns instance of actual dictionary
	#Params: -
	#Returns: dictionary instance
	def getInstance(self):
		return self._dictionary

"""
Queue class defining a data structure behaving in FIFO using deque
"""
class Queue:
	#Constructor method, new empty deque
	#Params: -
	#Returns: -
	def __init__(self):
		self._queue = deque()
		counter = 0

	#Returns whether queue is empty
	#Params: -
	#Returns: (bool) TRUE if queue is empty
	def empty(self):
		return (len(self._queue) == 0)

	#Adds element to back of queue
	#Params: -
	#Returns: -
	def push(self, item):
		self._queue.append(item)

	#Pops top element and returns removed element
	#Params: -
	#Returns: previous top element in queue
	def pop(self):
		return self._queue.popleft()

	#Clears all data
	#Params: -
	#Returns: -
	def clear(self):
		self._queue.clear()

	#Returns top of queue
	#Params: -
	#Returns: top element in queue
	def peek(self):
		return self._queue[0]

	#Returns size of queue
	#Params: -
	#Returns: number of elements in queue
	def size(self):
		return len(self._queue)

	#Overrides print method
	#Params: -
	#Returns: formatted string containing values of queue
	def __str__(self):
		return ('\n'.join('{}'.format(elem) for elem in self._queue))

	#Returns whether element exists in queue
	#Params: item
	#Returns: bool TRUE if item exists in queue
	def contains(self, item):
		return (item in self._queue)

	#Returns instance of actual queue
	#Params: -
	#Returns: queue instance
	def getInstance(self):
		return self._queue

"""
Stack class defining a data structure behaving in LIFO using list
"""
class Stack:
	#Constructor method, new empty stack using a list
	#Params: -
	#Returns: -
	def __init__(self):
		self._stack = []

	#Returns whether stack is empty
	#Params: -
	#Returns: (bool) TRUE if dictionary is empty
	def empty(self):
		return self._stack == []

	#Adds element to top of list
	#Params: item
	#Returns: -
	def push(self, item):
		self._stack.append(item)

	#Pops top element and returns removed element
	#Params: -
	#Returns: previous top element in stack
	def pop(self):
		return self._stack.pop()

	#Clears all data
	#Params: -
	#Returns: -
	def clear(self):
		del self._stack[:]

	#Returns top of stack
	#Params: -
	#Returns: top element in stack
	def peek(self):
		return self._stack[-1]

	#Returns size of stack
	#Params: -
	#Returns: number of elements in stack
	def size(self):
		return len(self._stack)

	#Overrides print method
	#Params: -
	#Returns: formatted string containing values of stack
	def __str__(self):
		return ('\n'.join('{}'.format(elem) for elem in self._stack))

	#Returns whether element exists in stack
	#Params: item
	#Returns: bool TRUE if item exists in stack
	def contains(self, item):
		return (item in self._stack)

	#Returns instance of actual stack
	#Params: -
	#Returns: stack instance
	def getInstance(self):
		return self._stack

#for testing purposes
if __name__ == '__main__':
    quad_1 = Quad('=', '5', '-1', 'B')
    quad_2 = Quad('+', '10', '20', 'A')
    quad_3 = Quad('goto', '-1', '20', 'C')
    quad_4 = Quad('gotoT', 'T1', '20', 'D')

    cube = Semantic_Cube()
    print cube.validate_operation("op_addition","words","whole")

    quadli = QuadList()
    quadli.append_quad('=', '5', '-1', 'B')
    quadli.append_quad('+', '10', '20', 'A')
    quadli.append_quad('goto', '-1', '20', "pending")
    quadli.append_quad('gotoT', 'T1', '20', 'D')

    print quadli
