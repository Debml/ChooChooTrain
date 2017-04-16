import sys
import global_scope
import constants
from structures import Quad

#Reads the current instruction (Quad) operation and executes it
def execute_code():
    global_scope.instruction_pointer = 1

    #Loops until break (end_proc is in charge of breaking)
    while True:
        current_instruction = read_current_quad(global_scope.instruction_pointer)
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
    #create_code_segment()
    #create_local_memory()
    #create_temp_memory()
    #store_constants()
    #create_global_memory()

#Executes an arithmetic operation
def binary_arithmetic_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = get_value_by_address(left_operand_address)
    right_operand_value = get_value_by_address(right_operand_address)

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_ADDITION:
        result_value = left_operand_address + right_operand_address
    elif operator == constants.Operators.OP_SUBTRACTION:
        result_value = left_operand_address - right_operand_address
    elif operator == constants.Operators.OP_MULTIPLICATION:
        result_value = left_operand_address * right_operand_address
    elif operator == constants.Operators.OP_DIVISION:
        if right_operand_address == 0:
            stop_exec("Cannot divide by 0")
        else:
            result_value = left_operand_address / right_operand_address
    else:
        unknown_operation()

    store_in_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Assigns a value to an ID
def assign_operation(current_instruction):
    value_to_assign_address = current_instruction.get_left_operand()
    assignee_address = current_instruction.get_result()

    value_to_assign = get_value_by_address(value_to_assign_address)
    store_in_memory(value_to_assign, assignee_address)

    global_scope.instruction_pointer += 1

#Executes a binary boolean operation
def binary_boolean_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = get_value_by_address(left_operand_address)
    right_operand_value = get_value_by_address(right_operand_address)

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_GREATER:
        result_value = left_operand_address > right_operand_address
    elif operator == constants.Operators.OP_GREATER_EQUAL:
        result_value = left_operand_address >= right_operand_address
    elif operator == constants.Operators.OP_LESS:
        result_value = left_operand_address < right_operand_address
    elif operator == constants.Operators.OP_LESS_EQUAL:
        result_value = left_operand_address <= right_operand_address
    elif operator == constants.Operators.OP_EQUAL:
        result_value = left_operand_address == right_operand_address
    elif operator == constants.Operators.OP_NOT_EQUAL:
        result_value = not left_operand_address == right_operand_address
    elif operator == constants.Operators.OP_AND:
        result_value = left_operand_address and right_operand_address
    elif operator == constants.Operators.OP_OR:
        result_value = left_operand_address or right_operand_address
    else:
        unknown_operation()

    store_in_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Executes a negation operation
def negation_operation(current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    result_address = current_instruction.get_result()

    left_operand_value = get_value_by_address(left_operand_address)
    result_value = not left_operand_address

    store_in_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Verifies that the given index is inside the bounds of the array
def verify_index_operation(current_instruction):
    index_address = current_instruction.get_left_operand()
    array_size = current_instruction.get_right_operand()

    index_value = get_value_by_address(index_address)

    if index_value >= 0 and index_value < array_size:
        global_scope.instruction_pointer += 1
    else:
        stop_exec("Array index out of bounds")

#Prints to console
def print_operation(current_instruction):
    expression_to_print_address = current_instruction.get_left_operand()
    expression_to_print_value = get_value_by_address(expression_to_print_address)

    print expression_to_print_value

    global_scope.instruction_pointer += 1

#Reads from console
def input_operation(current_instruction):
    input_address = current_instruction.get_result()
    input_value = input()

    store_in_memory(input_value, input_address)

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