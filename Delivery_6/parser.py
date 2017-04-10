import scanner
import sys
import ply.yacc as yacc
import globalScope
tokens = scanner.tokens

def p_PROGRAM(p):
	'''
	PROGRAM : EC_SEEN_START_PROG PROGRAM_AUX
	'''
	end_compilation()

def p_PROGRAM_AUX(p):
	'''
	PROGRAM_AUX : BLOCK
				  | PROGRAM_AUX BLOCK
	'''

def p_BLOCK(p):
	'''
	BLOCK : BLOCK_AUX block id EC_SEEN_BLOCK_ID RECEIVES_AUX RETURNS_AUX EC_SEEN_BLOCK_SIGNATURE BLOCK_BODY
	'''

def p_BLOCK_AUX(p):
	'''
	BLOCK_AUX : starting EC_SEEN_STARTING
				| empty
	'''

def p_RECEIVES_AUX(p):
	'''
	RECEIVES_AUX : receives colon id EC_SEEN_PARAM_ID of type TYPE EC_SEEN_TYPE RECEIVES_AUX1
				   | empty
	'''

def p_RECEIVES_AUX1(p):
	'''
	RECEIVES_AUX1 : comma id EC_SEEN_PARAM_ID of type TYPE EC_SEEN_TYPE RECEIVES_AUX1
					| empty
	'''

def p_RETURNS_AUX(p):
	'''
	RETURNS_AUX : block_returns TYPE EC_SEEN_RETURN_TYPE
				  | empty
	'''

def p_BLOCK_BODY(p):
	'''
	BLOCK_BODY : curlybraces_open BLOCK_BODY_AUX EC_SEEN_BLOCK_BODY_END curlybraces_close
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
	p[0] = p[1] #Returns the token found

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
			   | cst_whole  EC_SEEN_CONST EC_SEEN_CONST_WHOLE
	   		   | cst_decimal  EC_SEEN_CONST EC_SEEN_CONST_DECIMAL
		 	   | cst_words  EC_SEEN_CONST EC_SEEN_CONST_WORDS
			   | cst_boolean  EC_SEEN_CONST EC_SEEN_CONST_BOOLEAN
	'''
	p[0] = p[1]

def p_CONSTANT_AUX(p):
	'''
	CONSTANT_AUX : EC_SEEN_CONST_LIST_ID squarebracket_open ITEM squarebracket_close EC_SEEN_CONST_LIST
				   |  EC_SEEN_CALL_VAL_BLOCK_ID parenthesis_open EC_SEEN_START_PARAM CONSTANT_AUX1 parenthesis_close EC_SEEN_BLOCK_CALL_VAL
				   |  EC_SEEN_CONST EC_SEEN_CONST_ID empty
	'''

def p_CONSTANT_AUX1(p):
	'''
	CONSTANT_AUX1 : EXPRESSION EC_SEEN_PARAM CONSTANT_AUX2
			   | empty

	'''	

def p_CONSTANT_AUX2(p):
	'''
	CONSTANT_AUX2 : comma EXPRESSION EC_SEEN_PARAM CONSTANT_AUX2
			    | empty
	'''	

def p_DECLARATIONS(p):
	'''
	DECLARATIONS : VAR_DECLARATION
				   | LIST_DECLARATION
	'''

def p_VAR_DECLARATION(p):
	'''
	VAR_DECLARATION : variable EC_SEEN_VAR_KEYWORD id EC_SEEN_VAR_ID VAR_DECLARATION_AUX of type TYPE EC_SEEN_VAR_TYPE semicolon
	'''

def p_VAR_DECLARATION_AUX(p):
	'''
	VAR_DECLARATION_AUX : comma id EC_SEEN_VAR_ID VAR_DECLARATION_AUX
						  | empty
	'''

def p_LIST_DECLARATION(p):
	'''
	LIST_DECLARATION : list id EC_SEEN_LIST_ID squarebracket_open cst_whole EC_SEEN_LIST_SIZE squarebracket_close of type TYPE EC_SEEN_LIST_TYPE semicolon EC_SEEN_LIST
	'''

def p_EXPRESSION(p):
	'''
	EXPRESSION : EXPRESSION_AUX EXP EC_SEEN_EXPRESSION EXPRESSION_AUX1
	'''

def p_EXPRESSION_AUX(p):
	'''
	EXPRESSION_AUX : op_negation EC_SEEN_NOT
					 | empty
	'''

def p_EXPRESSION_AUX1(p):
	'''
	EXPRESSION_AUX1 : op_and EC_SEEN_AND_OR EXPRESSION
					 | op_or EC_SEEN_AND_OR EXPRESSION
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
	CALL : call id EC_SEEN_CALL_VOID_BLOCK_ID parenthesis_open EC_SEEN_START_PARAM CALL_AUX parenthesis_close EC_SEEN_BLOCK_CALL semicolon
	'''

def p_CALL_AUX(p):
	'''
	CALL_AUX : EXPRESSION EC_SEEN_PARAM CALL_AUX2
			   | empty

	'''	

def p_CALL_AUX2(p):
	'''
	CALL_AUX2 : comma EXPRESSION EC_SEEN_PARAM CALL_AUX2
			    | empty
	'''

def p_LOOP(p):
	'''
	LOOP : do EC_SEEN_DO BODY until parenthesis_open EXPRESSION parenthesis_close EC_SEEN_UNTIL
	'''

def p_ASSIGN(p):
	'''
	ASSIGN : id ASSIGN_AUX op_assign EC_SEEN_ASSIGN_OP EXPRESSION EC_SEEN_ASSIGN_VALUE semicolon
	'''

def p_ASSIGN_AUX(p):
	'''
	ASSIGN_AUX : EC_SEEN_CONST_LIST_ID squarebracket_open ITEM squarebracket_close EC_SEEN_CONST_LIST
				 | EC_SEEN_CONST EC_SEEN_CONST_ID empty
	'''

def p_RETURN(p):
	'''
	RETURN : return_statement EXPRESSION EC_SEEN_RETURN semicolon
	'''

def p_READ(p):
	'''
	READ : input parenthesis_open id READ_AUX EC_SEEN_READ_ID parenthesis_close semicolon
	'''

def p_READ_AUX(p):
	'''
	READ_AUX : EC_SEEN_CONST_LIST_ID squarebracket_open ITEM squarebracket_close EC_SEEN_CONST_LIST
			   | EC_SEEN_CONST EC_SEEN_CONST_ID empty
	'''

def p_WRITE(p):
	'''
	WRITE : print parenthesis_open EXPRESSION EC_SEEN_WRITE_EXP WRITE_AUX parenthesis_close semicolon
	'''

def p_WRITE_AUX(p):
	'''
	WRITE_AUX : comma EXPRESSION EC_SEEN_WRITE_EXP WRITE_AUX
				| empty
	'''

def p_empty(p):
    'empty : '
    pass

#Embedded Actions
#BLOCK action 1 - Sets starting block
def p_EC_SEEN_STARTING(p):
	"EC_SEEN_STARTING : "
	#If no starting block had been found yet
	if globalScope.function_directory.starting_block_key == "-1":
		globalScope.is_starting_block = True

		#Sets program's first quad to jump to starting block's first quad
		go_to_start = globalScope.pending_jumps.pop()
		globalScope.quad_list.set_result(go_to_start)
	else:
		stop_exec("Multiple starting blocks found")

#BLOCK action 2 - Creates a new row in the FRT for a new block
def p_EC_SEEN_BLOCK_ID(p):
	"EC_SEEN_BLOCK_ID : "
	globalScope.block_returns = False
	globalScope.current_block_id = p[-1]

	#Block name should not be a duplicate
	if not globalScope.function_directory.block_id_exists(globalScope.current_block_id):
		if globalScope.is_starting_block:
			globalScope.function_directory.starting_block_key = globalScope.current_block_id

		globalScope.function_directory.add_block_name(globalScope.current_block_id)
	else:
		stop_exec("Block named '%s' is already defined" % globalScope.current_block_id)

#BLOCK action 3 - Creates the block signature and adds parameters to the block's primitives list
def p_EC_SEEN_TYPE(p):
	"EC_SEEN_TYPE : "
	#Variable name should not be duplicate (in the current block)
	if not globalScope.function_directory.id_exists(globalScope.current_var_id, globalScope.current_block_id):
		parameter_type = p[-1]
		globalScope.function_directory.add_parameter_type(globalScope.current_block_id, parameter_type)
		globalScope.function_directory.add_primitive(globalScope.current_block_id, globalScope.current_var_id, parameter_type)
	else:
		stop_exec("Parameter named '%s' is already defined" % globalScope.current_var_id)

#BLOCK action 4 - Sets the block return type
def p_EC_SEEN_RETURN_TYPE(p):
	"EC_SEEN_RETURN_TYPE : "
	block_return_type = p[-1]
	globalScope.function_directory.add_block_return_type(globalScope.current_block_id, block_return_type)

#BLOCK action 5 - Gets the current parameter being analyzed
def p_EC_SEEN_PARAM_ID(p):
	"EC_SEEN_PARAM_ID : "
	globalScope.current_var_id = p[-1]

#BLOCK action 6 - Sets block's first quad in the FRT
def p_EC_SEEN_BLOCK_SIGNATURE(p):
	"EC_SEEN_BLOCK_SIGNATURE : "
	globalScope.function_directory.add_quad_position_block(globalScope.current_block_id, globalScope.quad_list.get_quad_count())

#BLOCK_BODY action 1 - Validates the return type with the one saved in the FRT for the current block
def p_EC_SEEN_BLOCK_BODY_END(p):
	"EC_SEEN_BLOCK_BODY_END : "
	block_return_type = globalScope.function_directory.get_return_type_for_block(globalScope.current_block_id)

	#Block should be returning something if it stated it would do so (Return type validation is done EC_SEEN_RETURN)
	if (globalScope.block_returns and block_return_type != "void") or (not globalScope.block_returns and block_return_type == "void"):
		globalScope.quad_list.append_quad("op_end_proc", "-1", "-1", "-1")
		globalScope.function_directory.clear_variable_list(globalScope.current_block_id)
	else:
		stop_exec("Block '%s' should return a '%s' value" % (globalScope.current_block_id, block_return_type))

#VAR_DECLARATION action 1 - Resets the list of primitives for the current type
def p_EC_SEEN_VAR_KEYWORD(p):
	"EC_SEEN_VAR_KEYWORD : "
	globalScope.var_names = []

#VAR_DECLARATION action 2 - Adds the previously seen primitive to the primitives list for the current type
def p_EC_SEEN_VAR_ID(p):
	"EC_SEEN_VAR_ID : "
	primitive_name = p[-1]
	globalScope.var_names.append(primitive_name)

#VAR_DECLARATION action 3 - Adds the list of primitives for the current type into the FRT for the current block
def p_EC_SEEN_VAR_TYPE(p):
	"EC_SEEN_VAR_TYPE : "
	for var_name in globalScope.var_names:
		#Primitive id should not be a duplicate
		if not globalScope.function_directory.id_exists(var_name, globalScope.current_block_id):
			primitive_type = p[-1]
			globalScope.function_directory.add_primitive(globalScope.current_block_id, var_name, primitive_type)
		else:
			stop_exec("Variable named '%s' is already defined" % var_name)

#LIST_DECLARATION action 1 - Sets the current list id being analyzed
def p_EC_SEEN_LIST_ID(p):
	"EC_SEEN_LIST_ID : "
	globalScope.current_list_id = p[-1]

#LIST_DECLARATION action 2 - Sets the current list size being analyzed
def p_EC_SEEN_LIST_SIZE(p):
	"EC_SEEN_LIST_SIZE : "
	globalScope.current_list_size = p[-1]

#LIST_DECLARATION action 3 - Sets the current list type being analyzed
def p_EC_SEEN_LIST_TYPE(p):
	"EC_SEEN_LIST_TYPE : "
	globalScope.current_list_type = p[-1]

#LIST_DECLARATION action 4 - Adds a list to the FRT for the current block
def p_EC_SEEN_LIST(p):
	"EC_SEEN_LIST : "
	#List id should not be a duplicate
	if not globalScope.function_directory.id_exists(globalScope.current_list_id, globalScope.current_block_id):
		globalScope.function_directory.add_list(globalScope.current_block_id, globalScope.current_list_id, globalScope.current_list_size, globalScope.current_list_type)
	else:
		stop_exec("List named '%s' is already defined" % globalScope.current_list_id)

#FACTOR action 1 - Adds a false bottom mark to the operators stack
def p_EC_SEEN_FACT_LP(p):	
	"EC_SEEN_FACT_LP : "
	globalScope.pending_operators.push("(")

#FACTOR action 2 - Removes the false bottom mark of the operators stack
def p_EC_SEEN_FACT_RP(p):	
	"EC_SEEN_FACT_RP : "
	globalScope.pending_operators.pop()

#CONSTANT action 1 - Adds the just read constant to the operands stack
def p_EC_SEEN_CONST(p):
	"EC_SEEN_CONST : "
	operand = p[-1]
	globalScope.pending_operands.push(operand)

#CONSTANT action 2 - Adds the id type of the just read id to the operand types stack
def p_EC_SEEN_CONST_ID(p):
	"EC_SEEN_CONST_ID : "
	primitive_id = globalScope.pending_operands.peek()

	#Primitive should exist in the current block
	if globalScope.function_directory.primitive_id_exists(primitive_id, globalScope.current_block_id):
		globalScope.pending_operand_types.push(globalScope.function_directory.get_variable_type_for_block(globalScope.pending_operands.peek(), globalScope.current_block_id))
	else:
		stop_exec("Variable '%s' is not declared in block '%s'" % (primitive_id, globalScope.current_block_id))

#CONSTANT action 3 - Adds the type whole to the operand types stack
def p_EC_SEEN_CONST_WHOLE(p):
	"EC_SEEN_CONST_WHOLE : "
	globalScope.pending_operand_types.push("whole")

#CONSTANT action 4 - Adds the type decimal to the operand types stack
def p_EC_SEEN_CONST_DECIMAL(p):
	"EC_SEEN_CONST_DECIMAL : "
	globalScope.pending_operand_types.push("decimal")

#CONSTANT action 5 - Adds the type words to the operand types stack
def p_EC_SEEN_CONST_WORDS(p):
	"EC_SEEN_CONST_WORDS : "
	globalScope.pending_operand_types.push("words")

#CONSTANT action 6 - Adds the type boolean to the operand types stack
def p_EC_SEEN_CONST_BOOLEAN(p):
	"EC_SEEN_CONST_BOOLEAN : "
	globalScope.pending_operand_types.push("boolean")

#CONSTANT action 7 - Validates block return type with a return value
def p_EC_SEEN_CALL_VAL_BLOCK_ID(p):
	"EC_SEEN_CALL_VAL_BLOCK_ID : "
	abstract_seen_block_id(p, True)

#CONSTANT action 8 - Generate block call quads for blocks with a return value
def p_EC_SEEN_BLOCK_CALL_VAL(p):
	"EC_SEEN_BLOCK_CALL_VAL : "
	abstract_seen_block_call(p, True)

#CONSTANT action 9 - Adds the just read list to the pending lists stack
def p_EC_SEEN_CONST_LIST_ID(p):
	"EC_SEEN_CONST_LIST_ID : "
	list_id = p[-1]

	#ID should belong to a list
	if globalScope.function_directory.list_id_exists(list_id, globalScope.current_block_id):
		globalScope.pending_lists.push(list_id)
		globalScope.pending_operators.push("(")
	else:
		stop_exec("ID '%s' is not a list" % list_id)

#CONSTANT action 10 - Generates quads to access list index
def p_EC_SEEN_CONST_LIST(p):
	"EC_SEEN_CONST_LIST : "
	list_index_type = globalScope.pending_operand_types.pop()

	#List index type should resolve to whole
	if list_index_type == "whole":
		list_id = globalScope.pending_lists.pop()
		list_address = globalScope.function_directory.get_list_address_for_block(list_id, globalScope.current_block_id)
		list_index = globalScope.pending_operands.pop()
		list_size = globalScope.function_directory.get_list_size_for_block(list_id, globalScope.current_block_id)
		list_type = globalScope.function_directory.get_list_type_for_block(list_id, globalScope.current_block_id)	

		globalScope.quad_list.append_quad("op_verify_index", list_index, list_size, "-1")

		result = "*t" + str(globalScope.temp_space)
		globalScope.temp_space = globalScope.temp_space + 1
		globalScope.quad_list.append_quad("op_addition", list_index, list_address, result)
		
		globalScope.pending_operands.push(result)
		globalScope.pending_operand_types.push(list_type)
		globalScope.pending_operators.pop()
	else:
		stop_exec("List index must be a 'whole' value, found a '%s' value instead" % list_index_type)

#ITEM action 1 - Pushes the appropriate operator into the operators stack
def p_EC_SEEN_ITEM_OP(p):
	"EC_SEEN_ITEM_OP : "
	operator = p[-1]

	if operator == "+":
		globalScope.pending_operators.push("op_addition")
	elif operator == "-":
		globalScope.pending_operators.push("op_subtraction")

#ITEM action 2 - Generates quad for the addition or subtraction operation
def p_EC_SEEN_TERM(p):
	"EC_SEEN_TERM : "
	#Checks that the next operator is an addition or subtraction to respect order of operations
	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_addition" or globalScope.pending_operators.peek() == "op_subtraction"):
		create_binary_operation_quad()

#TERM action 1 - Pushes the appropriate operator into the operators stack
def p_EC_SEEN_TERM_OP(p):
	"EC_SEEN_TERM_OP : "
	operator = p[-1]

	if operator == "*":
		globalScope.pending_operators.push("op_multiplication")
	elif operator == "/":
		globalScope.pending_operators.push("op_division")

#TERM action 2 - Generates quad for the multiplication or division operation
def p_EC_SEEN_FACTOR(p):
	"EC_SEEN_FACTOR : "
	#Checks that the next operator is a multplication or division to respect order of operations
	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_multiplication" or globalScope.pending_operators.peek() == "op_division"):
		create_binary_operation_quad()

#EXP action 1 - Pushes the appropriate operator into the operators stack
def p_EC_SEEN_RELOP(p):
	"EC_SEEN_RELOP : "
	operator = p[-1]

	if operator == ">":
		globalScope.pending_operators.push("op_greater")
	elif operator == ">=":
		globalScope.pending_operators.push("op_greater_equal")
	elif operator == "<":
		globalScope.pending_operators.push("op_less")
	elif operator == "<=":
		globalScope.pending_operators.push("op_less_equal")
	elif operator == "==":
		globalScope.pending_operators.push("op_equal")
	elif operator == "!=":
		globalScope.pending_operators.push("op_not_equal")

#EXP action 2 - Generates quad for equality operations
def p_EC_SEEN_RELOP_ITEM(p):
	"EC_SEEN_RELOP_ITEM : "
	#Checks that the next operator is a equality operator to respect order of operations
	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_greater" 
														or globalScope.pending_operators.peek() == "op_greater_equal"
														or globalScope.pending_operators.peek() == "op_less"
														or globalScope.pending_operators.peek() == "op_less_equal"
														or globalScope.pending_operators.peek() == "op_equal"
														or globalScope.pending_operators.peek() == "op_not_equal"):
		create_binary_operation_quad()

#ASSIGN action 1 - Pushes the assignment operator to the operators stack
def p_EC_SEEN_ASSIGN_OP(p):
	"EC_SEEN_ASSIGN_OP : "
	globalScope.pending_operators.push("op_assign")

#ASSIGN action 2 - Generates quad for assignment operations
def p_EC_SEEN_ASSIGN_VALUE(p):
	"EC_SEEN_ASSIGN_VALUE : "
	#Checks that the next operator is an assignment operator to respect order of operations
	if not globalScope.pending_operators.empty() and globalScope.pending_operators.peek() == "op_assign":
			#Value to be assigned
			right_operand = globalScope.pending_operands.pop()
			right_type = globalScope.pending_operand_types.pop()

			#Space where value will be assigned
			left_operand = globalScope.pending_operands.pop()
			left_type = globalScope.pending_operand_types.pop()

			operator = globalScope.pending_operators.pop()

			#Checks if right_operand can be stored in a left_operand container
			result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

			#Assignment should be valid
			if result_type != -1:
				globalScope.quad_list.append_quad(operator, right_operand, "-1", left_operand)

				#free temp operand memory
			else:
				stop_exec("Expression of type '%s' cannot be assigned to ID of type '%s'" % (right_type, left_type))

#CONDITION action 1 - Generates jump if false quad and pushes it into pending jumps stack
def p_EC_SEEN_IF_EXP(p):
	"EC_SEEN_IF_EXP : "
	exp_type = globalScope.pending_operand_types.pop()

	#The expression should resolve to a boolean value
	if exp_type == "boolean":
		result = globalScope.pending_operands.pop()

		globalScope.quad_list.append_quad("op_go_to_f", result, "-1", "pending")

		globalScope.pending_jumps.push(globalScope.quad_list.get_quad_count() - 1)
	else:
		stop_exec("Expected a boolean expression, found a '%s' expression instead" % exp_type)

#CONDITION action 2 - Fills the 'if' pending jump, and generates a quad for the true case
def p_EC_SEEN_ELSE(p):
	"EC_SEEN_ELSE : "
	#Quad for the true case
	globalScope.quad_list.append_quad("op_go_to", "-1", "-1", "-1")

	#Fills the 'if' pending jump
	if_false = globalScope.pending_jumps.pop()
	globalScope.quad_list.set_result(if_false)

	#Pushes jump to the end of the 'else' to the pending jumps stack
	globalScope.pending_jumps.push(globalScope.quad_list.get_quad_count() - 1)

#CONDITION action 3 - Fills the 'else' pending jump, or the 'if' pending jump if there was no 'else'
def p_EC_SEEN_END_IF(p):
	"EC_SEEN_END_IF : "
	end_if = globalScope.pending_jumps.pop()
	globalScope.quad_list.set_result(end_if)

#LOOP action 1 - Pushes starting point of loop to the pending jumps stack
def p_EC_SEEN_DO(p):
	"EC_SEEN_DO : "
	globalScope.pending_jumps.push(globalScope.quad_list.get_quad_count())

#LOOP action 2: - Generates quad to go to the beginning of the loop
def p_EC_SEEN_UNTIL(p):
	"EC_SEEN_UNTIL : "
	exp_type = globalScope.pending_operand_types.pop()

	#The expression should resolve to a boolean value
	if exp_type == "boolean":
		evaluation_result = globalScope.pending_operands.pop()
		loop_start = globalScope.pending_jumps.pop()

		globalScope.quad_list.append_quad("op_go_to_t", evaluation_result, "-1", loop_start)
	else:
		stop_exec("Expected a boolean expression, found a '%s' expression instead" % exp_type)


#WRITE action 1 - Generates quad for the write action
def p_EC_SEEN_WRITE_EXP(p):
	"EC_SEEN_WRITE_EXP : "
	expression_to_print = globalScope.pending_operands.pop()

	globalScope.quad_list.append_quad("op_print", expression_to_print, "-1", "-1")

#READ action 1 - Generates quad for the read action
def p_EC_SEEN_READ_ID(p):
	"EC_SEEN_READ_ID : "
	id_to_read_into = globalScope.pending_operands.pop()

	#The ID that will store whatever is read should exist
	if globalScope.function_directory.primitive_id_exists(id_to_read_into, globalScope.current_block_id):
		globalScope.quad_list.append_quad("op_input", "-1", "-1", id_to_read_into)
	else:
		stop_exec("ID '%s' is not declared" % id_to_read_into)

#EXPRESSION action 1 - Pushes the negation operator into the operators stack
def p_EC_SEEN_NOT(p):
	"EC_SEEN_NOT : "
	globalScope.pending_operators.push("op_negation")

#EXPRESSION action 2 - Pushes the appropriate operator into the operators stack
def p_EC_SEEN_AND_OR(p):
	"EC_SEEN_AND_OR : "
	operator = p[-1]

	if operator == "and":
		globalScope.pending_operators.push("op_and")
	elif operator == "or":
		globalScope.pending_operators.push("op_or")

#EXPRESSION action 3 - Generates quad for logical operations
def p_EC_SEEN_EXPRESSION(p):
	"EC_SEEN_EXPRESSION : "
	#Checks that the next operator is a relational operator to respect order of operations
	if not globalScope.pending_operators.empty() and (globalScope.pending_operators.peek() == "op_and" 
														or globalScope.pending_operators.peek() == "op_or"):
		create_binary_operation_quad()	

	#Checks that the next operator is a negation operator to respect order of operations
	elif not globalScope.pending_operators.empty() and globalScope.pending_operators.peek() == "op_negation":
		right_operand = globalScope.pending_operands.pop()
		right_type = globalScope.pending_operand_types.pop()

		operator = globalScope.pending_operators.pop()

		#Negation only applies to boolean type
		if right_type == "boolean":
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1

			globalScope.quad_list.append_quad(operator, "-1", right_operand, result)

			globalScope.pending_operands.push(result)
			globalScope.pending_operand_types.push('boolean')

			#free temp operand memory
		else:
			stop_exec("Negation operator can only be applied to 'boolean' expression, found '%s' expression" % right_type)
	
#PROGRAM action 1 - Generates jump to starting block and pushes to pending jumps stack
def p_EC_SEEN_START_PROG(p):
	"EC_SEEN_START_PROG : "
	globalScope.quad_list.append_quad("op_go_to", "-1", "-1", "pending")

	globalScope.pending_jumps.push(globalScope.quad_list.get_quad_count() - 1)

#RETURN action 1 - Validates return type
def p_EC_SEEN_RETURN(p):
	"EC_SEEN_RETURN : "
	block_return_type = globalScope.function_directory.get_return_type_for_block(globalScope.current_block_id)

	#blocks should only return when stated in the definition
	if block_return_type != "void":
		return_type = globalScope.pending_operand_types.pop()

		#Validates return value with the block definition
		if return_type == block_return_type:
			return_value = globalScope.pending_operands.pop()
			globalScope.quad_list.append_quad("op_return", return_value, "-1", "-1")
			globalScope.block_returns = True
		else:
			stop_exec("Block '%s' should return a '%s' value, found a '%s' value instead" % (globalScope.current_block_id, block_return_type, return_type))

	else:
		stop_exec("Block '%s' should not return a value" % globalScope.current_block_id)

#CALL action 1 - Validates block return type with no return value
def p_EC_SEEN_CALL_VOID_BLOCK_ID(p):
	"EC_SEEN_CALL_VOID_BLOCK_ID : "
	abstract_seen_block_id(p, False)

#CALL action 2 - Generates quad for ERA and initializes argument counter
def p_EC_SEEN_START_PARAM(p):
	"EC_SEEN_START_PARAM : "
	call_block_id = globalScope.pending_blocks.peek()
	globalScope.quad_list.append_quad("op_era", call_block_id, "-1", "-1")
	globalScope.pending_blocks_argument_counter.push(0)			

#CALL action 3 - Validates argument counter with parameter number
def p_EC_SEEN_PARAM(p):
	"EC_SEEN_PARAM : "
	argument_type = globalScope.pending_operand_types.pop()

	try:
		call_block_id = globalScope.pending_blocks.peek()
		block_argument_counter = globalScope.pending_blocks_argument_counter.pop()
		parameter_type = globalScope.function_directory.get_parameter_type_for_block(call_block_id, block_argument_counter)
	#If the argument counter is greater than the parameter counter
	except IndexError:
		block_parameter_counter = globalScope.function_directory.get_parameter_count_for_block(call_block_id)
		stop_exec("Block '%s' receives %d parameter(s), found %d argument(s) instead" % (call_block_id, block_parameter_counter, block_argument_counter + 1))

	block_argument_counter = block_argument_counter + 1
	globalScope.pending_blocks_argument_counter.push(block_argument_counter)

	#Validates argument type with parameter type
	if argument_type == parameter_type:
		argument = globalScope.pending_operands.pop()
		result = "param" + str(block_argument_counter)
		globalScope.quad_list.append_quad("op_param", argument, "-1", result)
	else:
		stop_exec("Argument #%d of block '%s' should be a '%s' value, found a '%s' value instead" % (block_argument_counter, call_block_id, parameter_type, argument_type))

#CALL action 4 - Generate block call quads for blocks with no return value
def p_EC_SEEN_BLOCK_CALL(p):
	"EC_SEEN_BLOCK_CALL : "
	abstract_seen_block_call(p, False)

#ERROR - Prints message for unexpected tokens
def p_error(p):
	stop_exec("Unexpected token '%s' found" % p.value.split("\n")[0])

#Helper functions for Embedded Actions Code
#Generates quads for block calls
#returns_value is a boolean value that indicates if the block returns a value or not
def abstract_seen_block_call(p, returns_value):
	call_block_id = globalScope.pending_blocks.pop()
	block_parameter_counter = globalScope.function_directory.get_parameter_count_for_block(call_block_id)
	block_argument_counter = globalScope.pending_blocks_argument_counter.pop()

	#Arguments number should match block's parameters number
	if  block_parameter_counter == block_argument_counter:
		call_block_initial_quad = globalScope.function_directory.get_quad_position_block(call_block_id)
		globalScope.quad_list.append_quad("op_go_sub", call_block_id, "-1", call_block_initial_quad)

		#If the block will resolve to a value
		if returns_value:
			result = "t" + str(globalScope.temp_space)
			globalScope.temp_space = globalScope.temp_space + 1
			globalScope.quad_list.append_quad("op_assign", call_block_id, "-1", result)

			globalScope.pending_operands.push(result)
			return_type = globalScope.function_directory.get_return_type_for_block(call_block_id)
			globalScope.pending_operand_types.push(return_type)

	else:
		stop_exec("Block '%s' receives %d parameter(s), found %d argument(s) instead" % (call_block_id, block_parameter_counter, block_argument_counter))

#Validates block return type with usage
#returns_value is a boolean value that indicates if the block returns a value or not
def abstract_seen_block_id(p, returns_value):
	call_block_id = p[-1]
	globalScope.pending_blocks.push(call_block_id)

	#Block should exist
	if globalScope.function_directory.block_id_exists(call_block_id):
		call_block_return_type = globalScope.function_directory.get_return_type_for_block(call_block_id)

		#Validate the return type with usage
		if not returns_value:
			if call_block_return_type != "void":
				stop_exec("Block '%s' returns a '%s' value, but is not being assigned to anything" % (call_block_id, call_block_return_type))
		else:
			if call_block_return_type == "void":
				stop_exec("Block '%s' does not return a value" % call_block_id)
	else:
		stop_exec("Block '%s' does not exist or is declared below block '%s'" % (call_block_id, globalScope.current_block_id))

#Creates a quad for binary operations (arithmetic, and/or)
def create_binary_operation_quad():
	right_operand = globalScope.pending_operands.pop()
	right_type = globalScope.pending_operand_types.pop()

	left_operand = globalScope.pending_operands.pop()
	left_type = globalScope.pending_operand_types.pop()

	operator = globalScope.pending_operators.pop()

	#Checks if operand types are interoperable
	result_type = globalScope.semantic_cube.validate_operation(operator, left_type, right_type)

	#Types should be interoperable
	if result_type != -1:
		result = "t" + str(globalScope.temp_space)
		globalScope.temp_space = globalScope.temp_space + 1

		globalScope.quad_list.append_quad(operator, left_operand, right_operand, result)

		globalScope.pending_operands.push(result)
		globalScope.pending_operand_types.push(result_type)

		#free temp operand memory
	else:
		stop_exec("Expressions of type '%s' and '%s' cannot be combined" % (left_type, right_type))

#Prints an error message and stops the program execution
#message is a string with an appropriate error message
def stop_exec(message):
	sys.exit("Error in line %d: %s" % (globalScope.line_count, message))

#Prints results of compilation when successful
def end_compilation():
	print('Compilation Successful!')
	globalScope.function_directory.print_table()
	print(globalScope.quad_list)

#Build the parser
parser = yacc.yacc()

#If no argument was given, make the user input a file
if(len(sys.argv) < 2):
    fileName = raw_input('Input the name of the file to parse: ')
    fileToParse = open(fileName, "r")
#If an argument was given, read that file
else:
    fileToParse = open(sys.argv[1], "r")

#Read the file sent as argument and parse it
code = fileToParse.read()
parser.parse(code)