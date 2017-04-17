import sys
import global_scope
import constants
import time
from structures import Quad
from structures import Activation_Record
from memory import Program_Memory

#Reads the current instruction (Quad) operation and executes it
def execute_code():
    global_scope.instruction_pointer = 0

    #Loops until break (end_proc is in charge of breaking)
    while True:
        current_instruction = global_scope.program_memory.get_quad_from_memory(global_scope.instruction_pointer)
        operator = current_instruction.get_operator()

        if operator == constants.Operators.OP_ADDITION:
            #print "addition"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_SUBTRACTION:
            #print "subtraction"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_MULTIPLICATION:
            #print "multiplication"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_DIVISION:
            #print "division"
            binary_arithmetic_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_ASSIGN:
            #print "assign"
            assign_operation(current_instruction)
        elif operator == constants.Operators.OP_GREATER:
            #print "greater"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GREATER_EQUAL:
            #print "greater than or equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_LESS:
            #print "less than"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_LESS_EQUAL:
            #print "less than or equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_EQUAL:
            #print "equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_NOT_EQUAL:
            #print "not equal"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_AND:
            #print "and"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_OR:
            #print "or"
            binary_boolean_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_NEGATION:
            #print "negation"
            negation_operation(current_instruction)
        elif operator == constants.Operators.OP_VERIFY_INDEX:
            #print "verify index"
            verify_index_operation(current_instruction)
        elif operator == constants.Operators.OP_GO_TO:
            #print "go to"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GO_TO_T:
            #print "go to if true"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_GO_TO_F:
            #print "go to if false"
            go_to_operation(operator, current_instruction)
        elif operator == constants.Operators.OP_PRINT:
            #print "print"
            print_operation(current_instruction)
        elif operator == constants.Operators.OP_INPUT:
            #print "input"
            input_operation(current_instruction)
        elif operator == constants.Operators.OP_ERA:
            #print "era"
            era_operation(current_instruction)
        elif operator == constants.Operators.OP_PARAM:
            #print "param"
            pass
        elif operator == constants.Operators.OP_GO_SUB:
            #print "go to subroutine"
            go_sub_operation(current_instruction)
        elif operator == constants.Operators.OP_RETURN:
            #print "return value"
            pass
        elif operator == constants.Operators.OP_END_PROC:
            #print "end procedure"
            end_proc_operation(current_instruction)

            #If all functions have finished executing (including starting), end program
            if global_scope.program_memory.stack_segment_is_empty():
                break
        else:
            #print "unsupported"
            stop_exec()

#Initializes memory for Run-Time 
def initialize_memory():
    starting_block = global_scope.function_directory.starting_block_key
    starting_local_type_counter = global_scope.function_directory.get_local_type_counter(starting_block)
    starting_temporary_type_counter = global_scope.function_directory.get_temporary_type_counter(starting_block)
    starting_activation_record = Activation_Record(starting_local_type_counter, starting_temporary_type_counter, 0)
    cc = global_scope.function_directory.memory_handler.get_constant_counter()

    aux_program_memory = Program_Memory(global_scope.quad_list, starting_activation_record, cc, global_scope.function_directory.constant_table)
    global_scope.program_memory = aux_program_memory

#Executes an arithmetic operation
def binary_arithmetic_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.program_memory.read_from_memory(left_operand_address)
    right_operand_value = global_scope.program_memory.read_from_memory(right_operand_address)

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
        stop_exec()

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Assigns a value to an ID
def assign_operation(current_instruction):
    value_to_assign_address = current_instruction.get_left_operand()
    assignee_address = current_instruction.get_result()

    if str(assignee_address)[0] == '*':
        assignee_address = global_scope.program_memory.read_from_memory(int(assignee_address[1:]))

    value_to_assign = global_scope.program_memory.read_from_memory(value_to_assign_address)
    global_scope.program_memory.write_to_memory(value_to_assign, assignee_address)

    global_scope.instruction_pointer += 1

#Executes a binary boolean operation
def binary_boolean_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.program_memory.read_from_memory(left_operand_address)
    right_operand_value = global_scope.program_memory.read_from_memory(right_operand_address)

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_GREATER:
        result_value = left_operand_value > right_operand_value
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
        stop_exec()

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Executes a negation operation
def negation_operation(current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.program_memory.read_from_memory(left_operand_address)

    result_value = not left_operand_value

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Verifies that the given index is inside the bounds of the array
def verify_index_operation(current_instruction):
    index_address = current_instruction.get_left_operand()
    array_size = current_instruction.get_right_operand()

    index_value = global_scope.program_memory.read_from_memory(index_address)

    if index_value >= 0 and index_value < array_size:
        global_scope.instruction_pointer += 1
    else:
        stop_exec("Array index out of bounds")

#Prints to console
def print_operation(current_instruction):
    expression_to_print_address = current_instruction.get_left_operand()
    expression_to_print_value = global_scope.program_memory.read_from_memory(expression_to_print_address)

    print expression_to_print_value

    global_scope.instruction_pointer += 1

#Reads from console
def input_operation(current_instruction):
    input_address = current_instruction.get_result()
    input_type = current_instruction.get_left_operand()

    #counts time for input
    start_input_timer = time.time()
    input_value = raw_input()
    global_scope.timer_counter = time.time() - start_input_timer

    validated_input = validate_input(input_value, input_type)

    if  validated_input is not None:
        global_scope.program_memory.write_to_memory(validated_input, input_address)
        global_scope.instruction_pointer += 1
    else:
        stop_exec("Input value '%s' is not of type '%s'" % (input_value, input_type))

#Executes a Go-To (True/False/Independent) operation
def go_to_operation(operator, current_instruction):
    new_instruction = current_instruction.get_result()

    if operator == constants.Operators.OP_GO_TO:
        global_scope.instruction_pointer = new_instruction
    elif operator == constants.Operators.OP_GO_TO_T:
        evaluation_address = current_instruction.get_left_operand()
        evaluation_result = global_scope.program_memory.read_from_memory(evaluation_address)


        #If evaluation_result resolves to true, go to the given instruction
        if evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to false, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    elif operator == constants.Operators.OP_GO_TO_F:
        evaluation_address = current_instruction.get_left_operand()
        evaluation_result = global_scope.program_memory.read_from_memory(evaluation_address)

        #If evaluation_result resolves to false, go to the given instruction
        if not evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to true, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    else:
        stop_exec()

#Generates an activation record
def era_operation(current_instruction):
    block_name = current_instruction.get_left_operand()
    local_counter_for_block = global_scope.function_directory.get_local_type_counter(block_name)
    temporary_counter_for_block = global_scope.function_directory.get_temporary_type_counter(block_name)

    #Leaving the return address pending for when the go_to_sub operation is called
    global_scope.temp_activation_record = Activation_Record(local_counter_for_block, temporary_counter_for_block, -1)

    global_scope.instruction_pointer += 1

#
def go_sub_operation(current_instruction):
    #Program should go the current next line after executing the called block
    return_address = global_scope.instruction_pointer + 1

    global_scope.temp_activation_record.set_return_address(return_address)
    global_scope.program_memory.add_activation_record(global_scope.temp_activation_record)

    #sets the new instruction pointer to the first quad of the called block
    block_initial_quad = current_instruction.get_result()
    global_scope.instruction_pointer = block_initial_quad

#
def end_proc_operation(current_instruction):
    removed_activation_record = global_scope.program_memory.remove_current_activation_record()
    return_address = removed_activation_record.get_return_address()
    global_scope.instruction_pointer = return_address

#Validates that the user input can be cast to the type it should be
def validate_input(input_value, input_type):
    if input_type == constants.DataTypes.WHOLE:
        try:
            whole_value = int(input_value)
            return whole_value
        except ValueError:
            return None
    elif input_type == constants.DataTypes.DECIMAL:
        try:
            decimal_value = float(input_value)
            return decimal_value
        except ValueError:
            return None
    elif input_type == constants.DataTypes.WORDS:
        try:
            str_value = str(input_value)
            return str_value
        except ValueError:
            return None
    elif input_type == constants.DataTypes.BOOLEAN:
        if input_value == 'true' or input_value == 'True':
            return True
        elif input_value == 'false' or input_value == 'False':
            return False
        else:
            return None
    else:
        return None

#Prints an error message and stops the program execution
#message is a string with an appropriate error message
def stop_exec(message = "Unknown operation"):
	sys.exit("Run-Time error: %s" % message)

#Entry method to start the intermediate code execution
def start_execution():
    initialize_memory()
    #print global_scope.function_directory.memory_handler
    execute_code()
    #print global_scope.function_directory.memory_handler