from directories import Function_Directory
from structures import Queue
from structures import Stack
from structures import Semantic_Cube
from structures import Quad_List

#Compilation variables
#Variables for high level structures
function_directory = Function_Directory()
semantic_cube = Semantic_Cube()
quad_list = Quad_List()

#Helper variables for semantic validation
line_count = 1
is_starting_block = False
block_returns = False
current_block_id = ""
current_var_id = ""
current_list_id = ""
current_list_size = ""
current_list_type = ""
primitive_names = []
pending_operators = Stack()
pending_operands = Stack()
pending_operand_types = Stack()
pending_jumps = Stack()
pending_blocks = Stack()
pending_blocks_argument_counter = Stack()
pending_lists = Stack()

#Run-Time variables
instruction_pointer = 1