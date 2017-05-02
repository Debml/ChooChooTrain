#"Enum" for QUADRUPLE operators
class Operators:
    OP_ADDITION = 1
    OP_SUBTRACTION = 2
    OP_MULTIPLICATION = 3
    OP_DIVISION = 4
    OP_ASSIGN = 5
    OP_GREATER = 6
    OP_GREATER_EQUAL = 7
    OP_LESS = 8
    OP_LESS_EQUAL = 9
    OP_EQUAL = 10
    OP_NOT_EQUAL = 11
    OP_AND = 12
    OP_OR = 13
    OP_NEGATION = 14
    OP_VERIFY_INDEX = 15
    OP_GO_TO = 16
    OP_GO_TO_T = 17
    OP_GO_TO_F = 18
    OP_PRINT = 19
    OP_INPUT = 20
    OP_ERA = 21
    OP_PARAM = 22
    OP_GO_SUB = 23
    OP_RETURN = 24
    OP_END_PROC = 25
'''
#Uncomment this one for better readeability during testing and printing
class Operators:
    OP_ADDITION = "op_addition"
    OP_SUBTRACTION = "op_subtraction"
    OP_MULTIPLICATION = "op_multiplication"
    OP_DIVISION = "op_division"
    OP_ASSIGN = "op_assign"
    OP_GREATER = "op_greater"
    OP_GREATER_EQUAL = "op_greater_equal"
    OP_LESS = "op_less"
    OP_LESS_EQUAL = "op_less_equal"
    OP_EQUAL = "op_equal"
    OP_NOT_EQUAL = "op_not_equal"
    OP_AND = "op_and"
    OP_OR = "op_or"
    OP_NEGATION = "op_negation"
    OP_VERIFY_INDEX = "op_verify_index"
    OP_GO_TO = "op_go_to"
    OP_GO_TO_T = "op_go_to_t"
    OP_GO_TO_F = "op_go_to_f"
    OP_PRINT = "op_print"
    OP_INPUT = "op_input"
    OP_ERA = "op_era"
    OP_PARAM = "op_param"
    OP_GO_SUB = "op_go_sub"
    OP_RETURN = "op_return"
    OP_END_PROC = "op_end_proc"
'''
#"Enum" for data types
class Data_Types:
    WHOLE = "whole"
    DECIMAL = "decimal"
    WORDS = "words"
    BOOLEAN = "boolean"
    VOID = "void"

#"Enum" for misc strings
class Misc:
    FALSE_BOTTOM = "("
    POINTER = "*"
    ADDRESS = "&"

#"Enum" for data type memory limits and ranges
class Memory_Limits:
    QUAD_SIZE = 500
    LOCAL_RANGES = [5000, 5500, 6000, 6500]
    LOCAL_SIZE = 500
    TEMPORARY_RANGES = [7000, 8500, 10000, 11500]
    TEMPORARY_SIZE = 1500
    CONSTANT_RANGES = [13000, 14000, 15000, 16000]
    CONSTANT_SIZE = 1000
    STACK_SEGMENT_SIZE = 500

class Error(Exception):
    pass

class ChooChooSyntaxError(Error):
    def __init__(self, message):
        self.message = message

class ChooChooExecutionError(Error):
    def __init__(self, message):
        self.message = message

class ChooChooInput(Error):
    def __init__(self, output_builder):
        self.accum_output = output_builder

class ChooChooExecutionError(Error):
    def __init__(self, message):
        self.message = message