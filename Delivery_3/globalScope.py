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
quads = Queue()
pending_operators = Stack()
pending_operands = Stack()
operand_types = Stack()
temp_space = 1