import scanner
import sys
import ply.yacc as yacc
import globalScope

from structures import Quad

tokens = scanner.tokens

def stop_exec(message):
	sys.exit("Error in line %d: %s" % (globalScope.line_count, message))

def p_PROGRAM(p):
	'''
	PROGRAM : PROGRAM_AUX
	'''
	print('Compilation Successful!')
	globalScope.function_directory.print_table()
	i = 0
	for quad in globalScope.quads:
		print(i)
		quad.print_quad()
		i = i + 1

def p_PROGRAM_AUX(p):
	'''
	PROGRAM_AUX : BLOCK
				  | PROGRAM_AUX BLOCK
	'''

def p_BLOCK(p):
	'''
	BLOCK : BLOCK_AUX block id EC_SEEN_BLOCK_ID RECEIVES_AUX RETURNS_AUX BLOCK_BODY
	'''

def p_BLOCK_AUX(p):
	'''
	BLOCK_AUX : starting EC_SEEN_STARTING
				| empty
	'''

def p_RECEIVES_AUX(p):
	'''
	RECEIVES_AUX : receives colon id EC_SEEN_PARAM_ID of_type TYPE EC_SEEN_TYPE RECEIVES_AUX1
				   | empty
	'''

def p_RECEIVES_AUX1(p):
	'''
	RECEIVES_AUX1 : comma id EC_SEEN_PARAM_ID of_type TYPE EC_SEEN_TYPE RECEIVES_AUX1
					| empty
	'''

def p_RETURNS_AUX(p):
	'''
	RETURNS_AUX : block_returns TYPE EC_SEEN_RETURN_TYPE
				  | empty
	'''

def p_BLOCK_BODY(p):
	'''
	BLOCK_BODY : curlybraces_open BLOCK_BODY_AUX curlybraces_close
	'''

def p_BLOCK_BODY_AUX1(p):
	'''
	BLOCK_BODY_AUX1 : STATEMENT BLOCK_BODY_AUX1
					 | empty
	'''

def p_BLOCK_BODY_AUX(p):
	'''
	BLOCK_BODY_AUX : DECLARATIONS BLOCK_BODY_AUX
					 | BLOCK_BODY_AUX1
	'''

def p_TYPE(p):
	'''
	TYPE : whole
		   | decimal
		   | words
		   | boolean
	'''
	p[0] = p[1]

def p_BODY(p):
	'''
	BODY : curlybraces_open BODY_AUX curlybraces_close
	'''

def p_BODY_AUX(p):
	'''
	BODY_AUX : STATEMENT BODY_AUX
			   | empty
	'''

def p_CONDITION(p):
	'''
	CONDITION : if parenthesis_open EXPRESSION parenthesis_close EC_SEEN_IF_EXP BODY CONDITION_AUX EC_SEEN_END_IF
	'''

def p_CONDITION_AUX(p):
	'''
	CONDITION_AUX : else EC_SEEN_ELSE BODY
					| empty
	'''

def p_CONSTANT(p):
	'''
	CONSTANT : id CONSTANT_AUX
			   | cst_whole  EC_SEEN_CONST SEEN_CONST_WHOLE
	   		   | cst_decimal  EC_SEEN_CONST SEEN_CONST_DECIMAL
		 	   | cst_words  EC_SEEN_CONST SEEN_CONST_WORDS
			   | cst_boolean  EC_SEEN_CONST SEEN_CONST_BOOLEAN
	'''
	p[0] = p[1]

def p_CONSTANT_AUX(p):
	'''
	CONSTANT_AUX : squarebracket_open EXPRESSION squarebracket_close
				   | parenthesis_open EXPRESSION CONSTANT_AUX1 parenthesis_close
				   |  EC_SEEN_CONST SEEN_CONST_ID empty
	'''

def p_CONSTANT_AUX1(p):
	'''
	CONSTANT_AUX1 : comma EXPRESSION CONSTANT_AUX1
					| empty
	'''

def p_DECLARATIONS(p):
	'''
	DECLARATIONS : VAR_DECLARATION
				   | LIST_DECLARATION
	'''

def p_VAR_DECLARATION(p):
	'''
	VAR_DECLARATION : variable EC_SEEN_VAR_KEYWORD id EC_SEEN_VAR_ID VAR_DECLARATION_AUX of_type TYPE EC_SEEN_VAR_TYPE semicolon
	'''

def p_VAR_DECLARATION_AUX(p):
	'''
	VAR_DECLARATION_AUX : comma id EC_SEEN_VAR_ID VAR_DECLARATION_AUX
						  | empty
	'''

def p_LIST_DECLARATION(p):
	'''
	LIST_DECLARATION : list id EC_SEEN_LIST_ID squarebracket_open EXPRESSION EC_SEEN_LIST_SIZE squarebracket_close of_type TYPE EC_SEEN_LIST_TYPE semicolon EC_SEEN_LIST
	'''

def p_EXPRESSION(p):
	'''
	EXPRESSION : EXPRESSION_AUX EXP EXPRESSION_AUX1
	'''

def p_EXPRESSION_AUX(p):
	'''
	EXPRESSION_AUX : op_negation
					 | empty
	'''

def p_EXPRESSION_AUX1(p):
	'''
	EXPRESSION_AUX1 : op_and EXPRESSION_AUX EXP
					 | op_or EXPRESSION_AUX EXP
					 | empty
	'''

def p_EXP(p):
	'''
	EXP : ITEM EXP_AUX
	'''

def p_EXP_AUX(p):
	'''
	EXP_AUX : op_less EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | op_less_equal EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | op_greater EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | op_greater_equal EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | op_equal EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | op_not_equal EC_SEEN_RELOP ITEM EC_SEEN_RELOP_ITEM
			  | empty
	'''

def p_FACTOR(p):
	'''
	FACTOR : parenthesis_open EC_SEEN_FACT_LP EXPRESSION parenthesis_close EC_SEEN_FACT_RP
			 | FACTOR_AUX
	'''

def p_FACTOR_AUX(p):
	'''
	FACTOR_AUX : op_addition CONSTANT
				 | op_subtraction CONSTANT
				 | CONSTANT
	'''

def p_ITEM(p):
	'''
	ITEM : TERM EC_SEEN_TERM ITEM_AUX
	'''

def p_ITEM_AUX(p):
	'''
	ITEM_AUX : op_addition EC_SEEN_ITEM_OP ITEM
			   | op_subtraction EC_SEEN_ITEM_OP ITEM
			   | empty
	'''

def p_TERM(p):
	'''
	TERM : FACTOR EC_SEEN_FACTOR TERM_AUX
	'''

def p_TERM_AUX(p):
	'''
	TERM_AUX : op_multiplication EC_SEEN_TERM_OP TERM
			   | op_division EC_SEEN_TERM_OP TERM
			   | empty
	'''

def p_STATEMENT(p):
	'''
	STATEMENT : ASSIGN
				| CONDITION
				| READ
				| WRITE
				| LOOP
				| RETURN
				| CALL
	'''

def p_CALL(p):
	'''
	CALL : call id parenthesis_open EXPRESSION CALL_AUX parenthesis_close semicolon
	'''

def p_CALL_AUX(p):
	'''
	CALL_AUX : comma EXPRESSION CALL_AUX
			   | empty
	'''

def p_LOOP(p):
	'''
	LOOP : do EC_SEEN_DO BODY until parenthesis_open EXPRESSION parenthesis_close EC_SEEN_UNTIL
	'''

def p_ASSIGN(p):
	'''
	ASSIGN : id EC_SEEN_CONST SEEN_CONST_ID ASSIGN_AUX op_assign EC_SEEN_ASSIGN_OP EXPRESSION EC_SEEN_ASSIGN_VALUE semicolon
	'''

def p_ASSIGN_AUX(p):
	'''
	ASSIGN_AUX : squarebracket_open EXPRESSION squarebracket_close
				 | empty
	'''

def p_RETURN(p):
	'''
	RETURN : return_statement EXPRESSION semicolon
	'''

def p_READ(p):
	'''
	READ : input parenthesis_open id READ_AUX parenthesis_close semicolon
	'''

def p_READ_AUX(p):
	'''
	READ_AUX : squarebracket_open EXPRESSION squarebracket_close
			   | empty
	'''

def p_WRITE(p):
	'''
	WRITE : print parenthesis_open EXPRESSION WRITE_AUX parenthesis_close semicolon
	'''

def p_WRITE_AUX(p):
	'''
	WRITE_AUX : comma EXPRESSION WRITE_AUX
				| empty
	'''

def p_empty(p):
    'empty :'
    pass

#Embedded Actions
#BLOCK action 1 - Sets starting block
def p_EC_SEEN_STARTING(p):
	"EC_SEEN_STARTING : "
	if globalScope.function_directory.starting_block_key == "-1":
		globalScope.is_starting_block = True
	else:
		stop_exec("Starting block is already defined")

#BLOCK action 2 - Creates a new Row in FRT with block id as key
def p_EC_SEEN_BLOCK_ID(p):
	"EC_SEEN_BLOCK_ID : "
	globalScope.current_block_id = p[-1]
	if not globalScope.function_directory.block_id_exists(globalScope.current_block_id):
		if globalScope.is_starting_block:
			globalScope.function_directory._starting_block_key = globalScope.current_block_id

		globalScope.function_directory.add_block_name(globalScope.current_block_id)
	else:
		stop_exec("Block named '" + globalScope.current_block_id + "' is already defined")

#BLOCK action 3 - Creates the list of parameter types and adds them to the variable list
def p_EC_SEEN_TYPE(p):
	"EC_SEEN_TYPE : "
	if not globalScope.function_directory.var_id_exists(globalScope.current_var_id, globalScope.current_block_id):
		globalScope.function_directory.add_parameter_type(globalScope.current_block_id, p[-1])
		globalScope.function_directory.add_primitive(globalScope.current_block_id, globalScope.current_var_id, p[-1])
	else:
		stop_exec("Parameter named '" + globalScope.current_var_id + "' is already defined")

#BLOCK action 4 - Sets the block return type
def p_EC_SEEN_RETURN_TYPE(p):
	"EC_SEEN_RETURN_TYPE : "
	globalScope.function_directory.add_block_return_type(globalScope.current_block_id, p[-1])

#BLOCK action 5 - gets the current variable id being analyzed
def p_EC_SEEN_PARAM_ID(p):
	"EC_SEEN_PARAM_ID : "
	globalScope.current_var_id = p[-1]

#VAR_DECLARATION action 1
def p_EC_SEEN_VAR_KEYWORD(p):
	"EC_SEEN_VAR_KEYWORD : "
	globalScope.var_names = []

#VAR_DECLARATION action 2
def p_EC_SEEN_VAR_ID(p):
	"EC_SEEN_VAR_ID : "
	globalScope.var_names.append(p[-1])

#VAR_DECLARATION action 3
def p_EC_SEEN_VAR_TYPE(p):
	"EC_SEEN_VAR_TYPE : "
	for var_name in globalScope.var_names:
		#Find current_var_id in primitives dictionary for current_block_id row
		if not globalScope.function_directory.var_id_exists(var_name, globalScope.current_block_id):
			globalScope.function_directory.add_primitive(globalScope.current_block_id, var_name, p[-1])
		else:
			stop_exec("Variable named '" + var_name + "' is already defined")

#LIST_DECLARATION action 1
def p_EC_SEEN_LIST_ID(p):
	"EC_SEEN_LIST_ID : "
	globalScope.current_list_id = p[-1]

#LIST_DECLARATION action 2
def p_EC_SEEN_LIST_SIZE(p):
	"EC_SEEN_LIST_SIZE : "
	globalScope.current_list_size = p[-1]

#LIST_DECLARATION action 3
def p_EC_SEEN_LIST_TYPE(p):
	"EC_SEEN_LIST_TYPE : "
	globalScope.current_list_type = p[-1]

#LIST_DECLARATION action 4
def p_EC_SEEN_LIST(p):
	"EC_SEEN_LIST : "
	if not globalScope.function_directory.var_id_exists(globalScope.current_list_id, globalScope.current_block_id):
		globalScope.function_directory.add_list(globalScope.current_block_id, globalScope.current_list_id, globalScope.current_list_size, globalScope.current_list_type)
	else:
		stop_exec("List named '" + globalScope.current_list_id + "' is already defined")

#FACTOR action 1
def p_EC_SEEN_FACT_LP(p):	
	"EC_SEEN_FACT_LP : "
	globalScope.pending_operators.push("(")

#FACTOR action 2
def p_EC_SEEN_FACT_RP(p):	
	"EC_SEEN_FACT_RP : "
	globalScope.pending_operators.pop()

#CONSTANT action 1
def p_EC_SEEN_CONST(p):
	"EC_SEEN_CONST : "
	globalScope.pending_operands.push(p[-1])

#CONSTANT action 2
def p_SEEN_CONST_ID(p):
	"SEEN_CONST_ID : "
	#checks the id type in the FRT
	if globalScope.function_directory.var_id_exists(globalScope.pending_operands.peek(), globalScope.current_block_id):
		globalScope.operand_types.push(globalScope.function_directory.get_variable_type_for_block(globalScope.pending_operands.peek(), globalScope.current_block_id))
	else:
		stop_exec("ID '" + globalScope.pending_operands.peek() + "' is not declared")

#CONSTANT action 3
def p_SEEN_CONST_WHOLE(p):
	"SEEN_CONST_WHOLE : "
	globalScope.operand_types.push("whole")

#CONSTANT action 4
def p_SEEN_CONST_DECIMAL(p):
	"SEEN_CONST_DECIMAL : "
	globalScope.operand_types.push("decimal")

#CONSTANT action 5
def p_SEEN_CONST_WORDS(p):
	"SEEN_CONST_WORDS : "
	globalScope.operand_types.push("words")

#CONSTANT action 6
def p_SEEN_CONST_BOOLEAN(p):
	"SEEN_CONST_BOOLEAN : "
	globalScope.operand_types.push("boolean")

#ITEM action 1
def p_EC_SEEN_ITEM_OP(p):
	"EC_SEEN_ITEM_OP : "
	if p[-1] == "+":
		globalScope.pending_operators.push("op_addition")
	elif p[-1] == "-":
		globalScope.pending_operators.push("op_subtraction")

#ITEM action 2
def p_EC_SEEN_TERM(p):
	"EC_SEEN_TERM : "

	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_addition" or globalScope.pending_operators.peek() == "op_subtraction"):
		right_operand = globalScope.pending_operands.pop()
		right_type = globalScope.operand_types.pop()

		left_operand = globalScope.pending_operands.pop()
		left_type = globalScope.operand_types.pop()

		operator = globalScope.pending_operators.pop()

		result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

		if result_type != -1:
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1

			temp_quad = Quad(operator, left_operand, right_operand, result)
			globalScope.quads.append(temp_quad)
			globalScope.quad_count = globalScope.quad_count + 1

			globalScope.pending_operands.push(result)
			globalScope.operand_types.push(result_type)

			#free temp operand memory
		else:
			stop_exec("Expressions of type '" + left_type + "' and '" + right_type + "' cannot be combined")

#TERM action 1
def p_EC_SEEN_TERM_OP(p):
	"EC_SEEN_TERM_OP : "
	if p[-1] == "*":
		globalScope.pending_operators.push("op_multiplication")
	elif p[-1] == "/":
		globalScope.pending_operators.push("op_division")

#TERM action 2
def p_EC_SEEN_FACTOR(p):
	"EC_SEEN_FACTOR : "

	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_multiplication" or globalScope.pending_operators.peek() == "op_division"):
		right_operand = globalScope.pending_operands.pop()
		right_type = globalScope.operand_types.pop()

		left_operand = globalScope.pending_operands.pop()
		left_type = globalScope.operand_types.pop()

		operator = globalScope.pending_operators.pop()

		result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

		if result_type != -1:
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1

			temp_quad = Quad(operator, left_operand, right_operand, result)
			globalScope.quads.append(temp_quad)
			globalScope.quad_count = globalScope.quad_count + 1

			globalScope.pending_operands.push(result)
			globalScope.operand_types.push(result_type)

			#free temp operand memory
		else:
			stop_exec("Expressions of type '" + left_type + "' and '" + right_type + "' cannot be combined")

#EXP action 1
def p_EC_SEEN_RELOP(p):
	"EC_SEEN_RELOP : "
	if p[-1] == ">":
		globalScope.pending_operators.push("op_greater")
	elif p[-1] == ">=":
		globalScope.pending_operators.push("op_greater_equal")
	elif p[-1] == "<":
		globalScope.pending_operators.push("op_less")
	elif p[-1] == "<=":
		globalScope.pending_operators.push("op_less_equal")
	elif p[-1] == "==":
		globalScope.pending_operators.push("op_equal")
	elif p[-1] == "!=":
		globalScope.pending_operators.push("op_not_equal")

#EXP action 2
def p_EC_SEEN_RELOP_ITEM(p):
	"EC_SEEN_RELOP_ITEM : "
	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_greater" 
														or globalScope.pending_operators.peek() == "op_greater_equal"
														or globalScope.pending_operators.peek() == "op_less"
														or globalScope.pending_operators.peek() == "op_less_equal"
														or globalScope.pending_operators.peek() == "op_equal"
														or globalScope.pending_operators.peek() == "op_not_equal"):
			right_operand = globalScope.pending_operands.pop()
			right_type = globalScope.operand_types.pop()

			left_operand = globalScope.pending_operands.pop()
			left_type = globalScope.operand_types.pop()

			operator = globalScope.pending_operators.pop()

			result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

			if result_type != -1:
				result = "t" + str(globalScope.temp_space)
				globalScope.temp_space = globalScope.temp_space + 1

				temp_quad = Quad(operator, left_operand, right_operand, result)
				globalScope.quads.append(temp_quad)
				globalScope.quad_count = globalScope.quad_count + 1

				globalScope.pending_operands.push(result)
				globalScope.operand_types.push(result_type)

				#free temp operand memory
			else:
				stop_exec("Expressions of type '" + left_type + "' and '" + right_type + "' cannot be combined")


#ASSIGN action 1
def p_EC_SEEN_ASSIGN_OP(p):
	"EC_SEEN_ASSIGN_OP : "
	globalScope.pending_operators.push("op_assign")

#ASSIGN action 2
def p_EC_SEEN_ASSIGN_VALUE(p):
	"EC_SEEN_ASSIGN_VALUE : "
	if not globalScope.pending_operators.empty() and globalScope.pending_operators.peek() == "op_assign":
			#value to be assigned
			right_operand = globalScope.pending_operands.pop()
			right_type = globalScope.operand_types.pop()

			#id where value will be assigned
			left_operand = globalScope.pending_operands.pop()
			left_type = globalScope.operand_types.pop()

			operator = globalScope.pending_operators.pop()

			result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

			if result_type != -1:
				temp_quad = Quad(operator, right_operand, "-1", left_operand)
				globalScope.quads.append(temp_quad)
				globalScope.quad_count = globalScope.quad_count + 1

				#free temp operand memory
			else:
				stop_exec("Expression of type '" + right_type + "' cannot be assigned to ID of type '" + left_type + "'")

#CONDITION action 1
def p_EC_SEEN_IF_EXP(p):
	"EC_SEEN_IF_EXP : "
	exp_type = globalScope.operand_types.pop()

	if exp_type == "boolean":
		result = globalScope.pending_operands.pop()

		temp_quad = Quad("GotoF", result, "-1", "pending")
		globalScope.quads.append(temp_quad)
		globalScope.quad_count = globalScope.quad_count + 1

		globalScope.pending_jumps.push(globalScope.quad_count - 1)
	else:
		stop_exec("Expected a boolean expression, found '" + exp_type + "' expression instead")

#CONDITION action 2
def p_EC_SEEN_END_IF(p):
	"EC_SEEN_END_IF : "
	end = globalScope.pending_jumps.pop()
	globalScope.quads[end]._result = globalScope.quad_count

#CONDITION action 3
def p_EC_SEEN_ELSE(p):
	"EC_SEEN_ELSE : "
	temp_quad = Quad("Goto", "-1", "-1", "-1")
	globalScope.quads.append(temp_quad)
	globalScope.quad_count = globalScope.quad_count + 1

	false = globalScope.pending_jumps.pop()
	globalScope.pending_jumps.push(globalScope.quad_count - 1)
	globalScope.quads[false]._result = globalScope.quad_count

#LOOP action 1
def p_EC_SEEN_DO(p):
	"EC_SEEN_DO : "
	globalScope.pending_jumps.push(globalScope.quad_count)

#LOOP action 2:
def p_EC_SEEN_UNTIL(p):
	"EC_SEEN_UNTIL : "
	exp_type = globalScope.operand_types.pop()

	if exp_type == "boolean":
		result = globalScope.pending_operands.pop()
		start = globalScope.pending_jumps.pop()

		temp_quad = Quad("GotoT", result, "-1", start)
		globalScope.quads.append(temp_quad)
		globalScope.quad_count = globalScope.quad_count + 1
	else:
		stop_exec("Expected a boolean expression, found '" + exp_type + "' expression instead")
	
def p_error(p):
	print("***ERROR '%s'" % p)
	sys.exit()

# Build the parser
parser = yacc.yacc()

# If no argument was given, make the user input a file
if(len(sys.argv) < 2):
    fileName = raw_input('Input the name of the file to parse: ')
    fileToParse = open(fileName, "r")
# If an argument was given, read that file
else:
    fileToParse = open(sys.argv[1], "r")

# Read the file sent as argument and parse it
code = fileToParse.read()
parser.parse(code)