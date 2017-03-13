"""
Collection of classes "structures" containing Stack, Queue, and Dictionary
Author: Paulina Escalante Campbell
January 19, 2016
"""
#import deque for implementation of queue
from collections import deque

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
		val = self._dictionary.__getitem__(self, key)
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
		return ('\n'.join(self._queue))

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
		return ('\n'.join(self._stack))

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
