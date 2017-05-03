from directories import Function_Directory
from directories import Code_Review_Data
from structures import Queue
from structures import Stack
from structures import Dictionary
from structures import Semantic_Cube
from structures import Quad_List
from structures import Activation_Record
from memory import Program_Memory

#Compilation variables
#Variables for high level structures
function_directory = Function_Directory()
semantic_cube = Semantic_Cube()
quad_list = Quad_List()
code_review = Code_Review_Data()

#Helper variables for semantic validation
line_count = 1
sign = 1
is_starting_block = False
block_returns = False
current_block_id = ""
current_var_id = ""
current_list_id = ""
current_list_size = ""
current_list_type = ""
primitive_names = []
pending_parameter_type_counter = Stack()
pending_operators = Stack()
pending_operands = Stack()
pending_operand_types = Stack()
pending_jumps = Stack()
pending_blocks = Stack()
pending_blocks_argument_counter = Stack()
pending_lists = Stack()

#generated for javascript output
output_builder = ""
last_output = ""

#Run-Time variables
instruction_pointer = 0
program_memory = Program_Memory()
temp_activation_record = Activation_Record()
current_return_value = None
starting_block = ""
user_input = ""

#timer helper variable
timer_counter = 0
block_run_time = 0

def initialize_structures():
    global function_directory, semantic_cube, quad_list, output_builder, code_review, output_builder, last_output
    code_review = Code_Review_Data()
    function_directory = Function_Directory()
    semantic_cube = Semantic_Cube()
    quad_list = Quad_List()
    output_builder = ""
    last_output = ""
    user_input = ""
    line_count = 1
