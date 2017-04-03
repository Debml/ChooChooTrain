from directories import Function_Directory
from structures import Queue
from structures import Stack
from structures import Semantic_Cube
from structures import Quad_List

function_directory = Function_Directory()
semantic_cube = Semantic_Cube()
is_starting_block = False
block_returns = False
current_block_id = ""
current_var_id = ""
call_block_id = ""
var_names = []
current_list_id = ""
current_list_size = ""
current_list_type = ""
quad_list = Quad_List()
pending_operators = Stack()
pending_operands = Stack()
operand_types = Stack()
pending_jumps = Stack()
#helper variable to handle temporary results counter
temp_space = 1
line_count = 1
block_argument_counter = 0
