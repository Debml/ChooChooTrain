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
    status_code = 1
    error_flag = False

    #Increase block call counter for the current block
    global_scope.code_review.increase_num_call_to_block(global_scope.starting_block)

    #Loops until break (end_proc is in charge of breaking)
    while True:
        #If all functions have finished executing (including starting), end program
        if global_scope.program_memory.stack_segment_is_empty() or error_flag:
            global_scope.code_review.print_data()
            if (error_flag == True):
                return 0
            else:
                return 1

        current_instruction = global_scope.program_memory.get_quad_from_memory(global_scope.instruction_pointer)
        operator = current_instruction.get_operator()

        current_block = global_scope.program_memory.get_current_activation_record().get_block_name()
        #Do not add initial go to, since it belong to program
        if global_scope.instruction_pointer > 0:
            #Increase quad counter for the current block
            global_scope.code_review.increase_executed_quad_counter(current_block)

        if operator == constants.Operators.OP_ADDITION:
            #print "addition"
            status_code = binary_arithmetic_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_SUBTRACTION:
            #print "subtraction"
            status_code = binary_arithmetic_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_MULTIPLICATION:
            #print "multiplication"
            status_code = binary_arithmetic_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_DIVISION:
            #print "division"
            status_code = binary_arithmetic_operation(operator, current_instruction)
            print status_code
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_ASSIGN:
            #print "assign"
            status_code = assign_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GREATER:
            #print "greater"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GREATER_EQUAL:
            #print "greater than or equal"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_LESS:
            #print "less than"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_LESS_EQUAL:
            #print "less than or equal"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_EQUAL:
            #print "equal"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_NOT_EQUAL:
            #print "not equal"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_AND:
            #print "and"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_OR:
            #print "or"
            status_code = binary_boolean_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_NEGATION:
            #print "negation"
            status_code = negation_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_VERIFY_INDEX:
            #print "verify index"
            status_code = verify_index_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GO_TO:
            #print "go to"
            status_code = go_to_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GO_TO_T:
            #print "go to if true"
            status_code = go_to_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GO_TO_F:
            #print "go to if false"
            status_code = go_to_operation(operator, current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_PRINT:
            #print "print"
            status_code = print_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_INPUT:
            #print "input"
            status_code = input_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_ERA:
            #print "era"
            status_code = era_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_PARAM:
            #print "param"
            status_code = param_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_GO_SUB:
            #print "go to subroutine"
            #add the number of activation records at the moment of the function call
            ar_count = global_scope.program_memory.get_stack_segment_size()
            global_scope.code_review.add_num_ar_on_call(ar_count)

            status_code = go_sub_operation(current_instruction)

            #Increase block call counter for the current block
            current_block = global_scope.program_memory.get_current_activation_record().get_block_name()
            global_scope.code_review.increase_num_call_to_block(current_block)

            if (status_code == 0):
                error_flag = True
                
        elif operator == constants.Operators.OP_RETURN:
            #print "return value"
            status_code = return_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        elif operator == constants.Operators.OP_END_PROC:
            #print "end procedure"
            status_code = end_proc_operation(current_instruction)
            if (status_code == 0):
                error_flag = True
        else:
            #print "unsupported"
            status_code = stop_exec()
            if (status_code == 0):
                error_flag = True

#Initializes memory for Run-Time 
def initialize_memory():
    global_scope.starting_block = global_scope.function_directory.starting_block_key
    starting_local_type_counter = global_scope.function_directory.get_local_type_counter(global_scope.starting_block)
    starting_temporary_type_counter = global_scope.function_directory.get_temporary_type_counter(global_scope.starting_block)
    starting_activation_record = Activation_Record(global_scope.starting_block, starting_local_type_counter, starting_temporary_type_counter, 0)
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

    if left_operand_value == None or right_operand_value == None:
        return stop_exec("Variable does not have a value")

    #Does the corresponding operation based on the operator
    if operator == constants.Operators.OP_ADDITION:
        result_value = left_operand_value + right_operand_value
    elif operator == constants.Operators.OP_SUBTRACTION:
        result_value = left_operand_value - right_operand_value
    elif operator == constants.Operators.OP_MULTIPLICATION:
        result_value = left_operand_value * right_operand_value
    elif operator == constants.Operators.OP_DIVISION:
        if right_operand_value == 0:
            return stop_exec("Cannot divide by 0")
        else:
            result_value = left_operand_value / right_operand_value
    else:
        return stop_exec()

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Assigns a value to an ID
def assign_operation(current_instruction):
    value_to_assign_address = current_instruction.get_left_operand()
    assignee_address = current_instruction.get_result()

    #if the value is not an address, it is a function name and the value should be read from the return value
    if not value_is_address(value_to_assign_address):
        value_to_assign = global_scope.current_return_value

        #if for some reason (logical error by programmer) the function did not return anything, stop execution
        if value_to_assign is None:
            return stop_exec("Block '%s' did not return any value" % value_to_assign_address)

        #reset value for next functions
        global_scope.current_return_value = None
    else:
        if str(assignee_address)[0] == '*':
            assignee_address = global_scope.program_memory.read_from_memory(int(assignee_address[1:]))

        value_to_assign = global_scope.program_memory.read_from_memory(value_to_assign_address)

        if value_to_assign == None:
            return stop_exec("Variable does not have a value")

    global_scope.program_memory.write_to_memory(value_to_assign, assignee_address)

    global_scope.instruction_pointer += 1

#Executes a binary boolean operation
def binary_boolean_operation(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.program_memory.read_from_memory(left_operand_address)
    right_operand_value = global_scope.program_memory.read_from_memory(right_operand_address)

    if left_operand_value == None or right_operand_value == None:
        return stop_exec("Variable does not have a value")

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
        return stop_exec()

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Executes a negation operation
def negation_operation(current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    result_address = current_instruction.get_result()

    left_operand_value = global_scope.program_memory.read_from_memory(left_operand_address)

    if left_operand_value == None:
        return stop_exec("Variable does not have a value")

    result_value = not left_operand_value

    global_scope.program_memory.write_to_memory(result_value, result_address)

    global_scope.instruction_pointer += 1

#Verifies that the given index is inside the bounds of the array
def verify_index_operation(current_instruction):
    index_address = current_instruction.get_left_operand()
    array_size = current_instruction.get_right_operand()

    index_value = global_scope.program_memory.read_from_memory(index_address)

    if index_value == None:
        return stop_exec("Variable does not have a value")

    if index_value >= 0 and index_value < array_size:
        global_scope.instruction_pointer += 1
    else:
        return stop_exec("Array index '%i' is out of bounds" % index_value)

#Prints to console
def print_operation(current_instruction):
    expression_to_print_address = current_instruction.get_left_operand()
    expression_to_print_value = global_scope.program_memory.read_from_memory(expression_to_print_address)

    if expression_to_print_value == None:
        return stop_exec("Variable does not have a value")
    

    global_scope.output_builder = global_scope.output_builder + str(expression_to_print_value) + "\n"
    global_scope.last_output = str(expression_to_print_value) + "\n"

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
        return stop_exec("Input value '%s' is not of type '%s'" % (input_value, input_type))

#Executes a Go-To (True/False/Independent) operation
def go_to_operation(operator, current_instruction):
    new_instruction = current_instruction.get_result()

    if operator == constants.Operators.OP_GO_TO:
        global_scope.instruction_pointer = new_instruction
    elif operator == constants.Operators.OP_GO_TO_T:
        evaluation_address = current_instruction.get_left_operand()
        evaluation_result = global_scope.program_memory.read_from_memory(evaluation_address)

        if evaluation_result == None:
            return stop_exec("Variable does not have a value")

        #If evaluation_result resolves to true, go to the given instruction
        if evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to false, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    elif operator == constants.Operators.OP_GO_TO_F:
        evaluation_address = current_instruction.get_left_operand()
        evaluation_result = global_scope.program_memory.read_from_memory(evaluation_address)

        if evaluation_result == None:
            return stop_exec("Variable does not have a value")

        #If evaluation_result resolves to false, go to the given instruction
        if not evaluation_result:
            global_scope.instruction_pointer = new_instruction
        #If evaluation_result resolves to true, go to the next instruction
        else:
            global_scope.instruction_pointer += 1
    else:
        return stop_exec()

#Generates an activation record
def era_operation(current_instruction):
    block_name = current_instruction.get_left_operand()
    local_counter_for_block = global_scope.function_directory.get_local_type_counter(block_name)
    temporary_counter_for_block = global_scope.function_directory.get_temporary_type_counter(block_name)

    #Leaving the return address pending for when the go_to_sub operation is called
    global_scope.temp_activation_record = Activation_Record(block_name, local_counter_for_block, temporary_counter_for_block, -1)

    global_scope.instruction_pointer += 1

#saves the argument value into the activation record of the function being called
def param_operation(current_instruction):
    #argument is the value to be sent
    argument_address = current_instruction.get_left_operand()
    #parameter is who will store the argument
    parameter_address = current_instruction.get_result()

    argument_value = global_scope.program_memory.read_from_memory(argument_address)

    if argument_value == None:
        return stop_exec("Variable does not have a value")

    #write the argument value from the current activation record into the one that is being constructed
    global_scope.temp_activation_record.get_block_memory().write_to_local_memory(argument_value, parameter_address)

    global_scope.instruction_pointer += 1

#adds an activation record to the stack segment and goes to the function's initial quad
def go_sub_operation(current_instruction):
    #Program should go the current next line after executing the called block
    return_address = global_scope.instruction_pointer + 1

    global_scope.temp_activation_record.set_return_address(return_address)

    #Verify that the stack segment can still hold activation records
    if global_scope.program_memory.add_activation_record(global_scope.temp_activation_record):
        #sets the new instruction pointer to the first quad of the called block
        block_initial_quad = current_instruction.get_result()
        global_scope.instruction_pointer = block_initial_quad
    else:
        return stop_exec("Number of pending function calls exceeded the limit")

#saves the return value and ends the function call
def return_operation(current_instruction):
    return_value_address = current_instruction.get_left_operand()
    return_value = global_scope.program_memory.read_from_memory(return_value_address)

    #save the return value in the current activation record
    global_scope.program_memory.get_current_activation_record().set_return_value(return_value)

    #end the function call
    end_proc_operation(current_instruction)

#removes the activation record from the stack segment
def end_proc_operation(current_instruction):
    removed_activation_record = global_scope.program_memory.remove_current_activation_record()
    return_address = removed_activation_record.get_return_address()

    #gets the return value (value is 'None' if it never returned anything)
    global_scope.current_return_value = removed_activation_record.get_return_value()

    #goes to the quad that was next in the previous function
    global_scope.instruction_pointer = return_address

#Validates that the user input can be cast to the type it should be
def validate_input(input_value, input_type):
    if input_type == constants.Data_Types.WHOLE:
        try:
            whole_value = int(input_value)
            return whole_value
        except ValueError:
            return None
    elif input_type == constants.Data_Types.DECIMAL:
        try:
            decimal_value = float(input_value)
            return decimal_value
        except ValueError:
            return None
    elif input_type == constants.Data_Types.WORDS:
        try:
            str_value = str(input_value)
            return str_value
        except ValueError:
            return None
    elif input_type == constants.Data_Types.BOOLEAN:
        if input_value == 'true' or input_value == 'True':
            return True
        elif input_value == 'false' or input_value == 'False':
            return False
        else:
            return None
    else:
        return None

#Verifies if a value is an address (an int value)
def value_is_address(value):
    try:
        address = int(value)
        return True
    #if value can't be casted to int, then it is a function
    except ValueError:
        if str(value)[0] == "*" or str(value)[0] == "&":
            return True
        else:
            return False

#Checks if the 'Go-To' corresponds to an If or a Loop, and updates the corresponding counter
def increase_go_to_counter(current_block, current_instruction):
    jump_to_position = current_instruction.get_result()

    #If the jump is to a quad that comes next, it is an 'If' condition operation
    if jump_to_position > global_scope.instruction_pointer:
        global_scope.code_review.increase_program_branches()
    #If the jump is to a previous quad, it is an 'Until' loop operation
    else:
        global_scope.code_review.increase_block_executed_loop_counter(current_block, global_scope.instruction_pointer)

#Prints an error message and stops the program execution
#message is a string with an appropriate error message
def stop_exec(message = "Unknown operation"):
    global_scope.last_output =  "Runtime error: " + message + "\n"
    global_scope.output_builder = global_scope.output_builder + "Runtime error: " + message + "\n"

    #sys.exit("Runtime error: %s" % message)
    #stop execution
    return 0

#Entry method to start the intermediate code execution
def start_execution():
    initialize_memory()
    #print global_scope.function_directory.memory_handler
    #print(global_scope.cr_block_quad_counter)
    #global_scope.code_review.print_data()
    return execute_code()
    #print global_scope.function_directory.memory_handler