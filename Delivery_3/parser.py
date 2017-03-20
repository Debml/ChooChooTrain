import scanner
import sys
import ply.yacc as yacc
import globalScope

from structures import Quad

tokens = scanner.tokens

def stop_exec(message):
	sys.exit(message)

def p_PROGRAM(p):
	'''
	PROGRAM : PROGRAM_AUX
	'''
	print('Compilation Successful!')
	globalScope.function_directory.print_table()
	#print (globalScope.quads)

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
	p[0] = p[1]

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
	FACTOR : parenthesis_open EC_SEEN_FACT_LP EXPRESSION parenthesis_close EC_SEEN_FACT_RP
			 | FACTOR_AUX
	'''

def p_FACTOR_AUX(p):
	'''
	FACTOR_AUX : op_addition CONSTANT EC_SEEN_FACT_CONST
				 | op_subtraction CONSTANT EC_SEEN_FACT_CONST
				 | CONSTANT EC_SEEN_FACT_CONST
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
	LOOP : do BODY until parenthesis_open EXPRESSION parenthesis_close 
	'''

def p_ASSIGN(p):
	'''
	ASSIGN : id ASSIGN_AUX op_assign EXPRESSION semicolon
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
		stop_exec("ERROR: Starting block is already defined")

#BLOCK action 2 - Creates a new Row in FRT with block id as key
def p_EC_SEEN_BLOCK_ID(p):
	"EC_SEEN_BLOCK_ID : "
	globalScope.current_block_id = p[-1]
	if not globalScope.function_directory.block_id_exists(globalScope.current_block_id):
		if globalScope.is_starting_block:
			globalScope.function_directory._starting_block_key = globalScope.current_block_id

		globalScope.function_directory.add_block_name(globalScope.current_block_id)
	else:
		stop_exec("ERROR: Block name is already defined")

#BLOCK action 3 - Creates the list of parameter types and adds them to the variable list
def p_EC_SEEN_TYPE(p):
	"EC_SEEN_TYPE : "
	if not globalScope.function_directory.var_id_exists(globalScope.current_var_id, globalScope.current_block_id):
		globalScope.function_directory.add_parameter_type(globalScope.current_block_id, p[-1])
		globalScope.function_directory.add_primitive(globalScope.current_block_id, globalScope.current_var_id, p[-1])
	else:
		stop_exec("ERROR: Parameter name is already defined")

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
			stop_exec("ERROR: Variable name is already defined")

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
		stop_exec("ERROR: List name is already defined")

#FACTOR action 1
def p_EC_SEEN_FACT_LP(p):	
	"EC_SEEN_FACT_LP : "
	globalScope.pending_operators.push("(")

#FACTOR action 2
def p_EC_SEEN_FACT_RP(p):	
	"EC_SEEN_FACT_RP : "
	globalScope.pending_operators.pop()

#FACTOR action 3
def p_EC_SEEN_FACT_CONST(p):
	"EC_SEEN_FACT_CONST : "
	globalScope.pending_operands.push(p[-1])
	#push tipo				

#ITEM action 1
def p_EC_SEEN_ITEM_OP(p):
	"EC_SEEN_ITEM_OP : "
	if p[-1] == "+":
		globalScope.pending_operators.push("+")
	elif p[-1] == "-":
		globalScope.pending_operators.push("-")

#ITEM action 2
def p_EC_SEEN_TERM(p):
	"EC_SEEN_TERM : "

	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "+" or globalScope.pending_operators.peek() == "-"):
		right_operand = globalScope.pending_operands.pop()
		#right type = 
		left_operand = globalScope.pending_operands.pop()
		#left type = 
		operator = globalScope.pending_operators.pop()
		result_type = 1

		if result_type != -1:
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1
			temp_quad = Quad(operator, left_operand, right_operand, result)
			globalScope.quads.push(temp_quad)
			globalScope.pending_operands.push(result)
			#result_type
			#free temp operand memory
		else:
			print("Types cannot be combined")
			sys.exit()

#TERM action 1
def p_EC_SEEN_TERM_OP(p):
	"EC_SEEN_TERM_OP : "
	if p[-1] == "*":
		globalScope.pending_operators.push("*")
	elif p[-1] == "/":
		globalScope.pending_operators.push("/")

#TERM action 2
def p_EC_SEEN_FACTOR(p):
	"EC_SEEN_FACTOR : "

	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "*" or globalScope.pending_operators.peek() == "/"):
		right_operand = globalScope.pending_operands.pop()
		#right type = 
		left_operand = globalScope.pending_operands.pop()
		#left type = 
		operator = globalScope.pending_operators.pop()
		result_type = 1

		if result_type != -1:
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1
			temp_quad = Quad(operator, left_operand, right_operand, result)
			globalScope.quads.push(temp_quad)
			globalScope.pending_operands.push(result)
			#result_type
			#free temp operand memory
		else:
			print("Types cannot be combined")
			sys.exit()
	
def p_error(p):
	print("***ERROR '%s'" % p)
	sys.exit()

yacc.yacc()

data ='''starting block Block15
receives :
parameter1 oftype decimal ,
parameter2 oftype whole ,
parameter3 oftype words

returns whole

{
	variable var1, var2, var3 oftype whole;
	variable var4, var5, var6 oftype words;
	list list1[5] oftype decimal;

	idName2 = (1 + 2) * 5;

}

block Block16
receives :
param1 oftype decimal

{
	list list1[5] oftype words;
	list list2[10] oftype decimal;
	variable var1 oftype whole;
}
'''

yacc.parse(data)