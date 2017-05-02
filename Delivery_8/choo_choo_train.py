import sys
import constants
import parser
import virtual_machine
import global_scope
import time
from structures import Dictionary

class attributes:  
    #index 0*
    code = ""
    #index 1*
    runtime = 0
    #index 2*
    compilationtime = 0
    #index 3*
    output = ""
    #index 4*
    compilationstatus = 0
    #index 5*
    block_names = []
    #index 6*
    compilation_steps = []
    #index 7*
    runtime_steps = []
    #index 8*
    num_vars = []
    #index 9*
    last_output = ""
    #index 10*
    num_ar = 0
    #index 11*
    records = []
    #index 12*
    num_ifs = []
    #index 13*
    num_loops = []
    #index 14*
    names_loops_blocks = []
    #index 15*
    cycles = []
    #index 16
    total_vars = 0
    #index 17
    total_loops = 0
    #index 18
    total_ifs = 0
    #index 19
    num_calls_block = []
    #index 20
    runtime_per_block = []

def set_code(code):
    attributes.code = code

def compile_and_run():
    #counts execution time
    start_time = time.time()

    #set attributes for index 0
    code = attributes.code

    #compile code
    try:
        parser.start_compilation(code)
    except constants.ChooChooSyntaxError as error:
        sys.exit(error.message)

    #get compile time
    compilation_time = time.time() - start_time

    #r_status returns 0 if there is a runtime error
    r_status = virtual_machine.start_execution()

    #finished execution
    execution_time = time.time() - global_scope.timer_counter - compilation_time - start_time

    #set attributes for index 3
    attributes.output = global_scope.output_builder

    #set attributes for index 1 from compiler
    attributes.runtime = global_scope.code_review.total_run_time

    #set attributes for index 2 from here
    attributes.compilationtime = compilation_time

    #set attributes for index 4
    if(r_status == 0):
        #some runtime error occurred, return default values and error code
        attributes.compilationstatus = 0

    else:
        #runtime complete
        attributes.compilationstatus = 1

    #set attributes for index 9
    attributes.last_output = global_scope.last_output

    #set attributes for index 10 and 11
    attributes.num_ar = global_scope.code_review.max_num_ar
    attributes.records = global_scope.code_review.num_ar_on_call

    #get attributes for index 16
    attributes.total_vars = global_scope.code_review.total_variable_counter
    #get attributes for index 17
    attributes.total_vars = global_scope.code_review.total_loop_counter
    #get attributes for index 18
    attributes.total_vars = global_scope.code_review.total_if_counter

    """attributes that need construction must first be constructed
    to different arrays from the block data retreived at code review
    """
    #get block data
    block_data = Dictionary()
    block_data = global_scope.code_review.block_data.get_instance()

    print block_data.keys()

    #get attributes for index 5/block names
    for key, block_values in block_data.items():
        #found one block
        attributes.block_names.append(key)
        #value 0 is quads in compilation
        attributes.compilation_steps.append(block_values[0])
        #value 1 is variable counter
        attributes.num_vars.append(block_values[1])
        #value 2 is compiled loops (num of loops)
        attributes.num_loops.append(block_values[2])
        #value 3 is executed quead counter
        attributes.runtime_steps.append(block_values[3])
        #value 4 is num calls to block
        attributes.num_calls_block.append(block_values[4])
        #value 5 is for executed loops
        for loop, cycle_num in block_values[5].get_instance().items():
            attributes.names_loops_blocks.append(key + " Loop " + str(loop))
            attributes.cycles.append(cycle_num)

        #value 6 is for if counter
        attributes.num_ifs.append(block_values[6])
        #value 7 is for runtime of block
        attributes.runtime_per_block.append(block_values[7])

    """DUMMY VALUES FOR TESTING PAGE
            
    #get attributes for index 5
    attributes.block_names = ["Block1","Block2","Block3","Block4"]
    CHECK

    #get attributes for index 6
    attributes.compilation_steps = [10, 23, 14, 37]
    CHECK

    #get attributes for index 7
    attributes.runtime_steps = [13, 23, 44, 17]
    CHECK

    #get attributes for index 8
    attributes.num_vars = [2, 2, 7, 1]
    CHECK

    #get attrbiutes for index 12
    attributes.num_ifs = [2,2,0,1]
    CHECK

    #get attrbiutes for index 13
    attributes.num_loops = [1,2,2,3]
    CHECK

    #get attributes for index 14
    attributes.names_loops_blocks = ["Block12 - Loop1","Block13 - Loop1","BlockHello - Loop1","BlockHello - Loop2", "BlockHello - Loop3"]

    #get attributes for index 15
    attributes.cycles = [5,7,12,10,3]

    #get attributes for index 19
    attributes.num_calls_block = [1304,1200,1231,2345]
    CHECK

    #get attributes for index 20
    attributes.runtime_per_block = [.0031,.0132,.000453,.00134]
    CHECK
    """

    print compilation_time, "seconds"
    print execution_time, "seconds"
    print attributes.runtime, "seconds"

