import sys
import global_scope
import constants
from structures import Quad

#Reads the current instruction (Quad) operation and executes it
def execute_code():
    global_scope.instruction_pointer = 0

    #Loops until break (end_proc is in charge of breaking)
    while True:
        current_instruction = global_scope.function_directory.memory_handler.get_quad_from_memory(global_scope.instruction_pointer)
        operator = current_instruction.get_operator()

        if operator == constants.Operators.OP_ADDITION:
            print "addition"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_SUBTRACTION:
            print "subtraction"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_MULTIPLICATION:
            print "multiplication"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_DIVISION:
            print "division"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_ASSIGN:
            print "assign"
            assign_operation(current_instruction)
        elif operator == constants.Operators.OP_GREATER:
            print "greater"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GREATER_EQUAL:
            print "greater than or equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_LESS:
            print "less than"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_LESS_EQUAL:
            print "less than or equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_EQUAL:
            print "equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_NOT_EQUAL:
            print "not equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_AND:
            print "and"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_OR:
            print "or"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_NEGATION:
            print "negation"
            negation_operation(current_instruction)
        elif operator == constants.Operators.OP_VERIFY_INDEX:
            print "verify index"
            verify_index_operation(current_instruction)
        elif operator == constants.Operators.OP_GO_TO:
            print "go to"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GO_TO_T:
            print "go to if true"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GO_TO_F:
            print "go to if false"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_PRINT:
            print "print"
            print_operation(current_instruction)
        elif operator == constants.Operators.OP_INPUT:
            print "input"
            input_operation(current_instruction)
        elif operator == constants.Operators.OP_ERA:
            print "era"
        elif operator == constants.Operators.OP_PARAM:
            print "param"
        elif operator == constants.Operators.OP_GO_SUB:
            print "go to subroutine"
        elif operator == constants.Operators.OP_RETURN:
            print "return value"
        elif operator == constants.Operators.OP_END_PROC:
            print "end procedure"
            break
        else:
            print "unsupported"
            unknown_operation()

#Initializes memory for Run-Time 
def initialize_memory():
    global_scope.function_directory.memory_handler.upload_quads_to_memory(global_scope.quad_list)
    global_scope.function_directory.memory_handler.activate_memory(global_scope.function_directory.constant_table)

#Executes an arithmetic operation
def binary_arithmetic_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.function_directory.memory_handler.get_from_memory(left_operand_address)
    right_operand_value = global_scope.function_directory.memory_handler.get_from_memory(right_operand_address)

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_ADDITION:
        result_value = left_operand_value + right_operand_value
    elif operator == constants.Operators.OP_SUBTRACTION:
        result_value = left_operand_value - right_operand_value
    elif operator == constants.Operators.OP_MULTIPLICATION:
        result_value = left_operand_value * right_operand_value
    elif operator == constants.Operators.OP_DIVISION:
        if right_operand_value == 0:
            stop_exec("Cannot divide by 0")
        else:
            result_value = left_operand_value / right_operand_value
    else:
        unknown_operation()

    global_scope.function_directory.memory_handler.add_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Assigns a value to an ID
def assign_operation(current_instruction):
    value_to_assign_address = current_instruction.get_left_operand()
    assignee_address = current_instruction.get_result()

    value_to_assign = global_scope.function_directory.memory_handler.get_from_memory(value_to_assign_address)
    global_scope.function_directory.memory_handler.add_to_memory(value_to_assign, assignee_address)

    global_scope.instruction_pointer += 1

#Executes a binary boolean operation
def binary_boolean_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.function_directory.memory_handler.get_from_memory(left_operand_address)
    right_operand_value = global_scope.function_directory.memory_handler.get_from_memory(right_operand_address)

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_GREATER:
        result_value = left_operand_value > right_operand_value

        print (result_value)
        print (left_operand_value)
        print (right_operand_value)


    elif operator == constants.Operators.OP_GREATER_EQUAL:
        result_value = left_operand_value >= right_operand_value
    elif operator == constants.Operators.OP_LESS:
        result_value = left_operand_value < right_operand_value
    elif operator == constants.Operators.OP_LESS_EQUAL:
        result_value = left_operand_value <= right_operand_value
    elif operator == constants.Operators.OP_EQUAL:
        result_value = left_operand_value == right_operand_value
    elif operator == constants.Operators.OP_NOT_EQUAL:
        result_value = not left_operand_value == right_operand_value
    elif operator == constants.Operators.OP_AND:
        result_value = left_operand_value and right_operand_value
    elif operator == constants.Operators.OP_OR:
        result_value = left_operand_value or right_operand_value
    else:
        unknown_operation()

    global_scope.function_directory.memory_handler.add_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Executes a negation operation
def negation_operation(current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.function_directory.memory_handler.get_from_memory(left_operand_address)
    result_value = not left_operand_value

    global_scope.function_directory.memory_handler.add_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Verifies that the given index is inside the bounds of the array
def verify_index_operation(current_instruction):
    index_address = current_instruction.get_left_operand()
    array_size = current_instruction.get_right_operand()

    index_value = global_scope.function_directory.memory_handler.get_from_memory(index_address)

    if index_value >= 0 and index_value < array_size:
        global_scope.instruction_pointer += 1
    else:
        stop_exec("Array index out of bounds")

#Prints to console
def print_operation(current_instruction):
    expression_to_print_address = current_instruction.get_left_operand()
    expression_to_print_value = global_scope.function_directory.memory_handler.get_from_memory(expression_to_print_address)

    print expression_to_print_value

    global_scope.instruction_pointer += 1

#Reads from console
def input_operation(current_instruction):
    input_address = current_instruction.get_result()
    input_value = input()

    global_scope.function_directory.memory_handler.add_to_memory(input_value, input_address)

    global_scope.instruction_pointer += 1

#Executes a Go-To (True/False/Independent) operation
def go_to_operation(operator, current_instruction):
    new_instruction = current_instruction.get_result()

    if operator == constants.Operators.OP_GO_TO:
        global_scope.instruction_pointer = new_instruction
    elif operator == constants.Operators.OP_GO_TO_T:
        evaluation_result = current_instruction.get_left_operand()

        #If evaluation_result resolves to true, go to the given instruction
        if evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to false, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    elif operator == constants.Operators.OP_GO_TO_F:
        evaluation_result = current_instruction.get_left_operand()
        evaluation_result = global_scope.function_directory.memory_handler.get_from_memory(evaluation_result)
        #If evaluation_result resolves to false, go to the given instruction
        if not evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to true, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    else:
        unknown_operation()

#Shows an unknown operation error and stops program execution
def unknown_operation():
    sys.exit("Run-Time error: Unknown operation")

#Prints an error message and stops the program execution
#message is a string with an appropriate error message
def stop_exec(message):
	sys.exit("Run-Time error: " % message)

#Entry method to start the intermediate code execution
def start_execution():
    initialize_memory()
    #print global_scope.function_directory.memory_handler
    execute_code()
    #print global_scope.function_directory.memory_handler
