from directories import Function_Directory
from structures import Queue
from structures import Stack
from structures import Semantic_Cube

function_directory = Function_Directory()
semantic_cube = Semantic_Cube()
is_starting_block = False
current_block_id = ""
current_var_id = ""
var_names = []
current_list_id = ""
current_list_size = ""
current_list_type = ""
quads = []
pending_operators = Stack()
pending_operands = Stack()
operand_types = Stack()
pending_jumps = Stack()
#helper variable to handle temporary results counter
temp_space = 1
quad_count = 0
line_count = 1
