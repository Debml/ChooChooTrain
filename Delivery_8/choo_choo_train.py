import sys
import parser
import virtual_machine
import global_scope
import time

class attributes:  
    #index 0
    code = ""
    #index 1
    runtime = 0
    #index 2
    compilationtime = 0
    #index 3
    output = ""
    #index 4
    compilationstatus = 0
    #index 5
    block_names = []
    #index 6
    compilation_steps = []
    #index 7
    runtime_steps = []
    #index 8
    num_vars = []
    #index 9
    last_output = ""

def set_code(code):
    attributes.code = code

def compile_and_run():
    #counts execution time
    start_time = time.time()

    compilation_time = time.time() - start_time

    code = attributes.code
    #filep = open("/Users/pescalante/Desktop/Tec/Universidad/8Semestre/Compiladores/ChooChooTrain Proyecto/ChooChooTrain/Delivery_8/test_cases/test_hello.txt","r")
    #code = filep.read()

    parser.start_compilation(code)
    r_status = virtual_machine.start_execution()

    #finished execution
    execution_time = time.time() - global_scope.timer_counter - start_time

    #set attributes
    attributes.output = global_scope.output_builder
    attributes.runtime = execution_time
    attributes.compilationtime = compilation_time

    #some runtime error occurred
    if(r_status == 0):
        attributes.compilationstatus = 0

    else:
        attributes.compilationstatus = 1

    attributes.last_output = global_scope.last_output

    print compilation_time, "seconds"
    print execution_time, "seconds"
