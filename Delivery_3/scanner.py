import ply.lex as lex

#List of reserved keywords
#keyword : tokenName
reserved = {
    'block' : 'block',
    'starting' : 'starting',
    'receives' : 'receives',
    'returns' : 'block_returns',
    'return' : 'return_statement',    
    'call' : 'call',
    'variable' : 'variable',
    'list' : 'list',
    'of_type' : 'of_type',
    'do' : 'do',
    'until' : 'until',
    'if' : 'if',
    'else' : 'else',
    'input' : 'input',
    'print' : 'print',
    'whole' : 'whole',
    'decimal' : 'decimal',
    'words' : 'words',
    'boolean' : 'boolean',
    'and' : 'op_and',
    'or' : 'op_or',
    'not' : 'op_negation'
}

#Token list
tokens = [
     'colon', 'semicolon', 'comma','curlybraces_open', 'curlybraces_close', 'parenthesis_open', 
     'parenthesis_close', 'squarebracket_open', 'squarebracket_close', 'op_assign', 'op_less', 
     'op_less_equal', 'op_greater', 'op_greater_equal', 'op_equal', 'op_not_equal', 
     'op_addition', 'op_subtraction', 'op_multiplication', 'op_division', 
     'cst_whole', 'cst_decimal', 'cst_words', 'cst_boolean', 'id'] + list(reserved.values())

#Token regular expressions
t_colon = r':'
t_semicolon = r';'
t_comma = r','
t_curlybraces_open = r'{'
t_curlybraces_close = r'}'
t_parenthesis_open = r'\('
t_parenthesis_close = r'\)'
t_squarebracket_open = r'\['
t_squarebracket_close = r'\]'
t_op_less = r'<'
t_op_less_equal = r'<='
t_op_greater = r'>'
t_op_greater_equal = r'>='
t_op_equal = r'=='
t_op_assign = r'='
t_op_not_equal = r'!='
t_op_addition = r'\+'
t_op_subtraction = r'-'
t_op_multiplication = r'\*'
t_op_division = r'\/'
t_ignore  = ' \t'

def t_cst_decimal(t): 
    r'[0-9]+\.[0-9]+([Ee][\+-]?[0-9]+)?'
    t.value = float(t.value)
    return t
def t_cst_whole(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t
def t_cst_words(t): 
    r'\"([^\\\"]|\\.)*\"'
    t.type = reserved.get(t.value, 'cst_words')
    return t
def t_cst_boolean(t):
    r'true|false'
    t.value = bool(t.value)
    return t     
def t_id(t): 
    r'[A-Za-z][A-Za-z0-9]*'
    t.type = reserved.get(t.value, 'id')
    #print(t)
    return t 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)        

lexer = lex.lex()
