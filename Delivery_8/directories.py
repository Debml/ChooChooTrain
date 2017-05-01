"""class for Function Directory
Stores characteristics of each block in the program
Must contain starting block
The function directory is represented as a Python Class
This Class contains two instance variables representing values for
1. Starting Block Key: String
2. Function Reference Table: Python Dictionary
"""
from structures import Dictionary
from structures import Stack
from memory import Memory_Handler
import constants

class Function_Directory:
    def __init__(self):
        #public variable for starting block key
        self.starting_block_key = "-1"

        #public variable for function reference table
        self.function_reference_table = Dictionary()

        #public variable for constant table
        self.constant_table = Dictionary()

        #private variable for memory handler
        self.memory_handler = Memory_Handler()

    #add block information for new block
    def add_block_name(self, block_name = None):
        #block_name should have value
        if block_name is not None:
            #public variable for block return type (string)
            return_type = constants.Data_Types.VOID

            #public variable for block primitives (Dictionary)
            primitives = Dictionary()

            #public variable for block lists (Dictionary)
            lists = Dictionary()

            #public variable for block parameters types(list)
            parameters = []

            #public variable for quad position where block begins
            quad_position = -1

            #public variable for local variable type counter
            local_type_counter = [0,0,0,0]

            #public variable for temporary variable type counter
            temporary_type_counter = [0,0,0,0]

            #declare block_data
            block_data = [return_type, [primitives, lists], parameters, quad_position, local_type_counter, temporary_type_counter]

            #add new block name as key
            self.function_reference_table.insert(block_name, block_data)

    #adds a local_type_counter to a block
    def add_local_type_counter(self, key = None, local_type_counter = None):
        #key should have value
        if key is not None:
            #local_type_counter should have some value
            if local_type_counter is not None:
                self.function_reference_table[key][4] = local_type_counter

    #adds a temporary_type_counter to a block
    def add_temporary_type_counter(self, key = None, temporary_type_counter = None):
        #key should have value
        if key is not None:
            #temporary_type_counter should have some value
            if temporary_type_counter is not None:
                self.function_reference_table[key][5] = temporary_type_counter

    #returns the local_type_counter of a block
    def get_local_type_counter(self, key = None):
        #key should have value
        if key is not None:
            return self.function_reference_table[key][4]

    #returns the temporary_type_counter of a block
    def get_temporary_type_counter(self, key = None):
        #key should have value
        if key is not None:
            return self.function_reference_table[key][5]
            
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
                    memory_address = self.memory_handler.assign_memory_address_local_variable(variable_type, 1)

                    #If there was no space for adding variables left, send an error to the parser
                    if memory_address == -1:
                        return False

                    #Index 1 of list is for primitives and lists dictionaries
                    #Index 0 of such list is specifically for primitives
                    variable_data = [variable_type, memory_address]
                    self.function_reference_table[key][1][0].insert(variable_name, variable_data)
                    return True

    #Key for current block, add list to list dictionary 
    def add_list(self, key = None, list_id = None, list_size = None, list_type = None):
        #key should have value
        if key is not None:
            #variable_name should have value
            if list_id is not None:
                #list_size should have value
                if list_size is not None:

                    #list_type should have value
                    if list_type is not None:

                        memory_address = self.memory_handler.assign_memory_address_local_variable(list_type, list_size)

                        #If there was no space for adding variables left, send an error to the parser
                        if memory_address == -1:
                            return False

                        #Index 1 of list is for primitives and lists dictionaries
                        #Index 1 of such list is specifically for lists
                        list_data = [list_type, memory_address, list_size]
                        self.function_reference_table[key][1][1].insert(list_id, list_data)
                        return True

    #Constant value and constant type to identify constant
    def add_constant(self, constant_value = None, constant_type = None):
        #key should have value
        if constant_value is not None:
            if constant_type is not None:
                #create list for entry
                #value for dictionary entry
                memory_address =  self.memory_handler.assign_memory_address_constant(constant_type)

                #If there was no space for adding constants left, send an error to the parser
                if memory_address == -1:
                    return -1

                constant_data = [constant_type, memory_address]
                
                #insert to constant table
                self.constant_table.insert(constant_value, constant_data)

                return memory_address

    #Key for current block, add one parameter found to parameters list
    def add_parameter_type(self, key = None, parameter_type = None):
        #key should have value
        if key is not None:
            #parameter should have value
            if parameter_type is not None:
                #Index 0 of list is for parameter list
                self.function_reference_table[key][2].append(parameter_type)

    #Key for current block, add quad_position of block
    def add_quad_position_block(self, key, quad_position = None):
        #quad_position should have value
        if quad_position is not None:
            #Index 3 of list is for quad_position
            self.function_reference_table[key][3] = quad_position

    #Gets the number of the first quad for a given block
    def get_quad_position_block(self, block_name):
        #block_name should have value
        if block_name is not None:
            #Index 3 of list is for quad_position
            return self.function_reference_table[block_name][3]

    #Gets the return type for a block
    def get_return_type_for_block(self, block_name):
        #block_name should not be none
        if block_name is not None:
            #Index 0 of list is for block return type
            return self.function_reference_table[block_name][0]

    #Gets the variable type for a variable in a given block
    def get_variable_type_for_block(self, var_id = None, block_id = None):
        #var_id should have value
        if var_id is not None:
            #block_id should have value
            if block_id is not None:
                return self.function_reference_table[block_id][1][0][var_id][0]   

    #Gets the Nth (param_count) parameter data type for a given block
    def get_parameter_type_for_block(self, block_id, n):
        #block_id should have value
        if block_id is not None:
            #n should have value
            if n is not None:
                #Index 2 is the list of parameter types
                return self.function_reference_table[block_id][2][n]

    #Get parameter count
    def get_parameter_count_for_block(self, block_id = None):
        #block_id should have value
        if block_id is not None:
            #parameter signature
            return len(self.function_reference_table[block_id][2])

    #Get variable count
    def get_variable_count_for_block(self, block_id = None):
        #block_id should have value
        if block_id is not None:
           #add primitives and list 
            return self.function_reference_table[block_id][1][0].size()+self.function_reference_table[block_id][1][1].size()

    #Gets the size of a list on a given block
    def get_list_size_for_block(self, list_id = None, block_id = None):
        #list_id should have value
        if list_id is not None:
            #block_id should have value
            if block_id is not None:
                #Index 1 of list is for primitives and lists dictionaries
                #Index 1 of such list is specifically for lists
                #Index 2 holds the size of a list
                return self.function_reference_table[block_id][1][1][list_id][2]

    #Gets the type of a list on a given block
    def get_list_type_for_block(self, list_id = None, block_id = None):
        #list_id should have value
        if list_id is not None:
            #block_id should have value
            if block_id is not None:
                #Index 1 of list is for primitives and lists dictionaries
                #Index 1 of such list is specifically for lists
                #Index 0 holds the type of a list
                return self.function_reference_table[block_id][1][1][list_id][0]

    #Gets the address of a primitive variable on a given block
    def get_primitive_address_for_block(self, primitive_id = None, block_id = None):
        #primitive_id should have value
        if primitive_id is not None:
            #block_id should have value
            if block_id is not None:
                #Index 1 of list is for primitives and lists dictionaries
                #Index 0 of such list is specifically for primitives
                #Index 1 holds the address of a primitive
                return self.function_reference_table[block_id][1][0][primitive_id][1]

    #Gets the next available temporary address for a given type
    def get_temporary_address(self, variable_type = None):
        #variable_type should have value
        if variable_type is not None:
            return self.memory_handler.assign_memory_address_temporary_variable(variable_type)

    #Gets the address of a list on a given block
    def get_list_address_for_block(self, list_id = None, block_id = None):
        #list_id should have value
        if list_id is not None:
            #block_id should have value
            if block_id is not None:
                #Index 1 of list is for primitives and lists dictionaries
                #Index 1 of such list is specifically for lists
                #Index 1 holds the address of a list
                return self.function_reference_table[block_id][1][1][list_id][1]

    #Check if a function id does not exist in the Function Reference Table
    def block_id_exists(self, block_id = None):
        #block_id should have value
        if block_id is not None:
            #Check the function names
            if block_id in self.function_reference_table:
                return True
                                
            return False

    #Check if a var id exists in the Function Reference Table
    def id_exists(self, var_id = None, block_id = None):
        #var_id should have value
        if var_id is not None:
            #block_id should have value
            if block_id is not None:
                #Check the function name
                if self.block_id_exists(var_id):
                    return True
                
                #Check the primitive names
                if var_id in self.function_reference_table[block_id][1][0]:
                    return True
                
                #check the list names
                if var_id in self.function_reference_table[block_id][1][1]:
                    return True
                                    
                return False

    #Check if a given ID is a primitive
    def primitive_id_exists(self, primitive_id = None, block_id = None):
        #primitive_id should have value
        if primitive_id is not None:
            #block_id should have value
            if block_id is not None:
                #If a pointer is given, assume it exists
                if str(primitive_id)[0] == "*":
                    return True

                #Check the function name
                if self.block_id_exists(primitive_id):
                    return True
                
                #Check the primitive names
                if primitive_id in self.function_reference_table[block_id][1][0]:
                    return True
                                    
                return False

    #Check if a given ID is a primitive
    def list_id_exists(self, list_id = None, block_id = None):
        #list_id should have value
        if list_id is not None:
            #block_id should have value
            if block_id is not None:
                #Check the function name
                if self.block_id_exists(list_id):
                    return True
                
                #Check the list names
                if list_id in self.function_reference_table[block_id][1][1]:
                    return True
                                    
                return False

    #gets the address of a constant if it exists or adds it and then returns it
    def get_constant_address(self, constant_value = None, constant_type = None):
        #constant_id should have value
        if constant_value is not None:
            #constant_type should have value
            if constant_type is not None:
                #check if entry exists with corresponding type
                if self.constant_table.contains(constant_value) and self.constant_table[constant_value][0] == constant_type:
                    return self.constant_table[constant_value][1]
                #add it to the constant table and return the address
                else:
                    return self.add_constant(constant_value, constant_type)


    #clears variable list (primitives and lists) in a function
    def clear_variable_list(self, block_key = None):
        #block id should have value
        if block_key is not None:
            #if block exists
            if self.block_id_exists(block_key):
                #clear primitive table
                self.function_reference_table[block_key][1][0] = Dictionary()
            
                #clear list table
                self.function_reference_table[block_key][1][1] = Dictionary()

    #print block information for all blocks
    def print_table(self):
        #print table formatted
        print("Function Reference Table\n")
        print("Starting Block: " + self.starting_block_key)
        for key in self.function_reference_table.get_instance():
            print("*" + key + "* :")
            print("Return Type: " + self.function_reference_table[key][0])
            print("Primitives: ")
            print(self.function_reference_table[key][1][0])
            print("Lists: ")
            print(self.function_reference_table[key][1][1])
            print("Parameters: ")
            print(self.function_reference_table[key][2])
            print("Function Starting Quad: ")
            print(self.function_reference_table[key][3])
            print("\n")
            print(self.function_reference_table[key][4])
            print("\n")
            print(self.function_reference_table[key][5])
            print("\n")
            print("Function number of quads: ")
            print(self.function_reference_table[key][6])
            print("\n")
        print("Constants: ")
        print(self.constant_table)
        print("\n")

    #print variable list for specific block
    def print_variable_list(self, block_key = None):
        #print table formatted
        print("Variable Table for " + block_key)
        if self.block_id_exists(block_key):
            print("Primitives: ")
            print(self.function_reference_table[block_key][1][0])
            print("Lists: ")
            print(self.function_reference_table[block_key][1][1])
            print("\n")

#for testing purposes
if __name__ == '__main__':
    directory = Function_Directory()

    directory.add_block_name("Block1")
    directory.add_block_name("Block2")

    directory.add_block_return_type("Block1", constants.Data_Types.WHOLE)

    directory.add_parameter_type("Block1", constants.Data_Types.DECIMAL)
    directory.add_parameter_type("Block1", constants.Data_Types.WHOLE)
    directory.add_parameter_type("Block1", constants.Data_Types.WORDS)

    directory.add_parameter_type("Block2", constants.Data_Types.WHOLE)
    directory.add_parameter_type("Block2", constants.Data_Types.WORDS)

    #parameters
    directory.add_primitive("Block1", "parameter1", constants.Data_Types.DECIMALw)
    directory.add_primitive("Block1", "parameter2", constants.Data_Types.WHOLE)
    directory.add_primitive("Block1", "parameter3", constants.Data_Types.WORDS)

    directory.add_primitive("Block2", "parameter1", constants.Data_Types.WHOLE)
    directory.add_primitive("Block2", "parameter2", constants.Data_Types.WORDS)

    #variables
    directory.add_primitive("Block1", "variable1", constants.Data_Types.WORDS)
    directory.add_primitive("Block1", "variable2", constants.Data_Types.WORDS)

    directory.add_list("Block2", "listvariable1", "5", constants.Data_Types.WHOLE)

    directory.print_table()

    print ("NUM VARS")
    print directory.get_variable_count("Block1")
    print ("NUM PARAMS")
    print directory.get_parameter_count("Block1")

    print ("NUM VARS")
    print directory.get_variable_count("Block2")
    print ("NUM PARAMS")
    print directory.get_parameter_count("Block2")
    