import scanner
tokens = scanner.tokens

import ply.yacc as yacc
from directories import Function_Directory

function_directory = Function_Directory()
is_starting_block = False
current_block_id = ""
current_var_id = ""
var_names = []
current_list_id = ""
current_list_size = ""
current_list_type = ""

def stop_exec(message):
	sys.exit(message)

def p_PROGRAM(p):
	'''
	PROGRAM : PROGRAM_AUX
	'''
	print('OKAY')

def p_PROGRAM_AUX(p):
	'''
	PROGRAM_AUX : BLOCK
				  | PROGRAM_AUX BLOCK
	'''

def p_BLOCK(p):
	'''
	BLOCK : BLOCK_AUX block id SEEN_BLOCK_ID RECEIVES_AUX RETURNS_AUX BLOCK_BODY
	'''

def p_BLOCK_AUX(p):
	'''
	BLOCK_AUX : starting SEEN_STARTING
				| empty
	'''

def p_RECEIVES_AUX(p):
	'''
	RECEIVES_AUX : receives colon id SEEN_PARAM_ID of_type TYPE SEEN_TYPE RECEIVES_AUX1
				   | empty
	'''

def p_RECEIVES_AUX1(p):
	'''
	RECEIVES_AUX1 : comma id SEEN_PARAM_ID of_type TYPE SEEN_TYPE RECEIVES_AUX1
					| empty
	'''

def p_RETURNS_AUX(p):
	'''
	RETURNS_AUX : block_returns TYPE SEEN_RETURN_TYPE
				  | empty
	'''

#BLOCK action 1
def p_SEEN_STARTING(p):
	"SEEN_STARTING : "
	if function_directory._starting_block_key == "-1":
		is_starting_block = True
	else:
		stop_exec("ERROR: Starting block is already defined")

#BLOCK action 2
def p_SEEN_BLOCK_ID(p):
	"SEEN_BLOCK_ID : "
	current_block_id = p[-1]
	if current_block_id not in function_directory.function_reference_table:
		if is_starting_block:
			function_directory._starting_block_key = current_block_id

		function_directory.add_block_name(current_block_id)
	else:
		stop_exec("ERROR: Block name is already defined")

#BLOCK action 3
def p_SEEN_TYPE(p):
	"SEEN_TYPE : "
	#Find current_var_id in primitives dictionary for current_block_id row
	print (current_var_id)
	if current_var_id not in function_directory.function_reference_table[current_block_id][1][0]:
		function_directory.add_parameter_type(current_block_id, p[-1])
		function_directory.add_primitive(current_block_id, current_var_id, p[-1])
	else:
		stop_exec("ERROR: Parameter name is already defined")

#BLOCK action 4
def p_SEEN_RETURN_TYPE(p):
	"SEEN_RETURN_TYPE : "
	function_directory.add_block_return_type(current_block_id, p[-1])

#BLOCK action 5
def p_SEEN_PARAM_ID(p):
	"SEEN_PARAM_ID : "
	current_var_id = p[-1]

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
	BLOCK_BODY_AUX : DECLARATIONS BLOCK_BODY_AUX1
					 | BLOCK_BODY_AUX1
	'''

def p_TYPE(p):
	'''
	TYPE : whole
		   | decimal
		   | words
		   | boolean
	'''

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
	CONDITION : if parenthesis_open EXPRESSION parenthesis_close BODY CONDITION_AUX
	'''

def p_CONDITION_AUX(p):
	'''
	CONDITION_AUX : else BODY
					| empty
	'''

def p_CONSTANT(p):
	'''
	CONSTANT : id CONSTANT_AUX
			   | cst_whole
	   		   | cst_decimal
		 	   | cst_words
			   | cst_boolean
	'''

def p_CONSTANT_AUX(p):
	'''
	CONSTANT_AUX : squarebracket_open EXPRESSION squarebracket_close
				   | parenthesis_open EXPRESSION CONSTANT_AUX1 parenthesis_close
				   | empty
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
	VAR_DECLARATION : variable SEEN_VAR_KEYWORD id SEEN_VAR_ID VAR_DECLARATION_AUX of_type TYPE SEEN_VAR_TYPE semicolon
	'''

def p_VAR_DECLARATION_AUX(p):
	'''
	VAR_DECLARATION_AUX : comma id SEEN_VAR_ID VAR_DECLARATION_AUX
						  | empty
	'''

#VAR_DECLARATION action 1
def p_SEEN_VAR_KEYWORD(p):
	"SEEN_VAR_KEYWORD : "
	var_names = []

#VAR_DECLARATION action 2
def p_SEEN_VAR_ID(p):
	"SEEN_VAR_ID : "
	var_names.append(p[-1])

#VAR_DECLARATION action 3
def p_SEEN_VAR_TYPE(p):
	"SEEN_VAR_TYPE : "
	for var_name in var_names:
		#Find current_var_id in primitives dictionary for current_block_id row
		if var_name not in function_directory.function_reference_table[current_block_id][1][0]:
			function_directory.add_primitive(current_block_id, var_name, p[-1])
		else:
			stop_exec("ERROR: Variable name is already defined")

def p_LIST_DECLARATION(p):
	'''
	LIST_DECLARATION : variable id SEEN_LIST_ID squarebracket_open EXPRESSION SEEN_LIST_SIZE squarebracket_close of_type TYPE SEEN_LIST_TYPE semicolon SEEN_LIST
	'''

#LIST_DECLARATION action 1
def p_SEEN_LIST_ID(p):
	"SEEN_LIST_ID : "
	current_list_id = p[-1]

#LIST_DECLARATION action 2
def p_SEEN_LIST_SIZE(p):
	"SEEN_LIST_SIZE : "
	current_list_size = p[-1]

#LIST_DECLARATION action 3
def p_SEEN_LIST_TYPE(p):
	"SEEN_LIST_TYPE : "
	current_list_type = p[-1]

#LIST_DECLARATION action 4
def p_SEEN_LIST(p):
	"SEEN_LIST : "
	if current_list_id not in function_directory.function_reference_table[current_block_id][1][1]:
		function_directory.add_list(current_block_id, current_list_id, current_list_size, current_list_type)
	else:
		stop_exec("ERROR: List name is already defined")

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
	EXP_AUX : op_less ITEM
			  | op_less_equal ITEM
			  | op_greater ITEM
			  | op_greater_equal ITEM
			  | op_equal ITEM
			  | op_not_equal ITEM
			  | empty
	'''

def p_FACTOR(p):
	'''
	FACTOR : parenthesis_open EXPRESSION parenthesis_close
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
	ITEM : TERM ITEM_AUX
	'''

def p_ITEM_AUX(p):
	'''
	ITEM_AUX : op_addition ITEM
			   | op_subtraction ITEM
			   | empty
	'''

def p_TERM(p):
	'''
	TERM : FACTOR TERM_AUX
	'''

def p_TERM_AUX(p):
	'''
	TERM_AUX : op_multiplication TERM
			   | op_division TERM
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
	LOOP : do BODY until parenthesis_open EXPRESSION parenthesis_close 
	'''

def p_ASSIGN(p):
	'''
	ASSIGN : id ASSIGN_AUX op_assign EXPRESSION semicolon
	'''

def p_ASSIGN_AUX(p):
	'''
	ASSIGN_AUX : squarebracket_open EXPRESSION squarebracket_close
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

def p_error(p):
	print("***ERROR '%s'" % p)

yacc.yacc()

data ='''starting block Block1
receives :
parameter1 oftype decimal ,
parameter2 oftype whole ,
parameter3 oftype words

returns whole 

{
	variable variable1 , variable2 oftype words;
}

block Block2
receives :
parameter1 oftype whole ,
parameter2 oftype words ,

{
	variable variable1 [ 5 ] oftype whole
}
'''
yacc.parse(data)

