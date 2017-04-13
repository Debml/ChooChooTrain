import sys
import global_scope
import constants

def execute_code():
    instruction_pointer = 1

    while True:
        current_instruction = read_current_quad(instruction_pointer)
        operator = current_instruction.get_operator()

        if operator == constants.Operators.OP_ADDITION:
            print "addition"
            arithmetic_expression(operator, current_instruction)
        elif operator == constants.Operators.OP_SUBTRACTION:
            print "subtraction"
            arithmetic_expression(operator, current_instruction)
        elif operator == constants.Operators.OP_MULTIPLICATION:
            print "multiplication"
            arithmetic_expression(operator, current_instruction)
        elif operator == constants.Operators.OP_DIVISION:
            print "division"
            arithmetic_expression(operator, current_instruction)
        elif operator == constants.Operators.OP_GREATER:
            print "greater"
        elif operator == constants.Operators.OP_GREATER_EQUAL:
            print "greater than or equal"
        elif operator == constants.Operators.OP_LESS:
            print "less than"
        elif operator == constants.Operators.OP_LESS_EQUAL:
            print "less than or equal"
        elif operator == constants.Operators.OP_EQUAL:
            print "equal"
        elif operator == constants.Operators.OP_NOT_EQUAL:
            print "not equal"
        elif operator == constants.Operators.OP_ASSIGN:
            print "assign"
            value_to_assign_address = current_instruction.get_left_operand()
            assignee_address = current_instruction.get_result()

            value_to_assign = get_value_by_address(value_to_assign_address)
            store_in_memory(value_to_assign, assignee_address)

            instruction_pointer += 1
        elif operator == constants.Operators.OP_NEGATION:
            print "negation"
        elif operator == constants.Operators.OP_AND:
            print "and"
        elif operator == constants.Operators.OP_OR:
            print "or"
        elif operator == constants.Operators.OP_VERIFY_INDEX:
            print "verify index"
        elif operator == constants.Operators.OP_GO_TO:
            print "go to"
        elif operator == constants.Operators.OP_GO_TO_T:
            print "go to if true"
        elif operator == constants.Operators.OP_GO_TO_F:
            print "go to if false"
        elif operator == constants.Operators.OP_PRINT:
            print "print"
            expression_to_print_address = current_instruction.get_left_operand()
            expression_to_print_value = get_value_by_address(expression_to_print_address)

            print expression_to_print_value
        elif operator == constants.Operators.OP_INPUT:
            print "input"
            input_address = current_instruction.get_result()
            input_value = input()

            store_in_memory(input_value, input_address)
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

def create_memory():
    #create_code_segment()
    #create_local_memory()
    #create_temp_memory()
    #store_constants()
    #create_global_memory()

def arithmetic_expression(operator, current_instruction):
    left_operand_address = current_instruction.get_left_operand()
    right_operand_address = current_instruction.get_right_operand()
    result_address = current_instruction.get_result()

    left_operand_value = get_value_by_address(left_operand_address)
    right_operand_value = get_value_by_address(right_operand_address)

    if operator == constants.Operators.OP_ADDITION:
        result_value = left_operand_address + right_operand_address
    elif operator == constants.Operators.OP_SUBTRACTION:
        result_value = left_operand_address - right_operand_address
    elif operator == constants.Operators.OP_MULTIPLICATION:
        result_value = left_operand_address * right_operand_address
    elif operator == constants.Operators.OP_DIVISION:
        result_value = left_operand_address / right_operand_address
    else:
        #error

    store_in_memory(result_value, result_address)

    instruction_pointer += 1
