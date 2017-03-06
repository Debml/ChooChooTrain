import ply.lex as lex

#regEx : tokenName
reserved = {
    'block' : 'block',
    'main' : 'main',
    'receives' : 'receives',
    'returns' : 'returns',
    'return' : 'ret',    
    'call' : 'call',
    'variable' : 'variable',
    'of type' : 'ofType',
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
}

tokens = [
     'colon', 'semicolon', 'comma','cb_open', 'cb_close', 'par_open', 'par_close', 'sb_open', 
     'sb_close', 'assignOp', 'relOp', 'binaryOp', 'negationOp', 'plusOp', 'minusOp', 'multiplicationOp', 
     'divisionOp', 'cst_whole', 'cst_decimal',  'cst_words', 'cst_boolean', 'id'] + list(reserved.values())

#Token regular expressions
t_ignore  = ' \t'
t_colon = r':'
t_semicolon = r';' 
t_comma = r','
t_cb_open = r'{'
t_cb_close = r'}'
t_par_open = r'\('
t_par_close = r'\)'
t_sb_open = r'['
t_sb_close = r']'
t_assignOp = r'='
t_relOp = r'<|<=|>|>=|==|!='
t_binaryOp = r'and|or'
t_negationOp = r'not'
t_plusOp = r'\+'
t_minusOp = r'-'
t_multiplicationOp = r'\*'
t_divisionOp = r'\/'
def t_cst_whole(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t
def t_cst_decimal(t): 
    r'[0-9]+\.[0-9]+([Ee][\+-]?[0-9]+)?'
    t.value = float(t.value)
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
    t.type = reserved.get(t.value, 'ID')
    return t 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)        

lexer = lex.lex()