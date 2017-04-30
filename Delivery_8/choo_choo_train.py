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
    #index 10 
    num_ar = 0
    #index 11
    records = []


def set_code(code):
    attributes.code = code

def compile_and_run():
    #counts execution time
    start_time = time.time()

    compilation_time = time.time() - start_time

    #set attributes for index 0
    code = attributes.code

    #filep = open("/Users/pescalante/Desktop/Tec/Universidad/8Semestre/Compiladores/ChooChooTrain Proyecto/ChooChooTrain/Delivery_8/test_cases/test_hello.txt","r")
    #code = filep.read()

    parser.start_compilation(code)
    r_status = virtual_machine.start_execution()

    #finished execution
    execution_time = time.time() - global_scope.timer_counter - start_time

    #set attributes for index 3
    attributes.output = global_scope.output_builder
    #set attributes for index 1
    attributes.runtime = execution_time
    #set attributes for index 2
    attributes.compilationtime = compilation_time

    #some runtime error occurred
    #set attributes for index 4
    if(r_status == 0):
        attributes.compilationstatus = 0

    else:
        attributes.compilationstatus = 1

    #set attributes for index 9
    attributes.last_output = global_scope.last_output

    #set attributes for index 10 and 11
    attributes.num_ar = global_scope.code_review.max_num_ar
    attributes.records = global_scope.code_review.num_ar_on_call

    print compilation_time, "seconds"
    print execution_time, "seconds"
