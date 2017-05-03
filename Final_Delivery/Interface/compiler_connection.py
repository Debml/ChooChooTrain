import sys
sys.path.insert(0,'..')

import choo_choo_train
import random


class Compiler_Handler:
    def __init__(self):
        self.result = []
        #index 0
        self.code_js = ""
        #index 1
        self.runtime = 0
        #index 2
        self.compilation_time = 0
        #index 3
        self.output = ""
        # index 4, if 1 compilation successful, 2 comp error, 3 runtime error
        self.compilation_status = 0
        #index 5
        self.block_names = []
        #index 6
        self.compilation_steps = []
        #index 7
        self.runtime_steps = []      
        #index 8
        self.num_vars = []
        #index 9 last output in case of error
        self.last_output = ""
        #index 10 num ar
        self.num_ar = 0
        #index 11 records
        self.records = []
        #index 12 number of ifs per block
        self.num_ifs = []
        #index 13 number of loops per block
        self.num_loops = []
        #index 14
        names_loops_blocks = []
        #index 15 for cycles in runtime per loops
        self.cycles = []
        #index 16
        self.total_vars = 0
        #index 17
        self.total_loops = 0
        #index 18
        self.total_ifs = 0
        #index 19
        self.num_calls_block = []
        #index 20
        self.runtime_per_block = []

        #input vars for sending input
        self.input = ""

    def send_input(self, user_input):
        #only write send_input data to choochootrain
        choo_choo_train.clear_input()
        choo_choo_train.set_input(user_input)

        #continue choo choo execution with new data
        #compilation already done
        choo_choo_train.continue_execution()

        #restart result array
        if self.result:
            while self.result:
                print self.result.pop()

        # get runtime and format
        if (choo_choo_train.attributes.runtime > 0.00001):
            self.runtime = '{:0.5f}'.format(choo_choo_train.attributes.runtime)
        
        else:
            self.runtime = '{:.5e}'.format(choo_choo_train.attributes.runtime)

        #get compile time and format
        if (self.compilation_time == 0):
            self.compilation_time = 0
        
        else:
            self.compilation_time = '{:.7e}'.format(choo_choo_train.attributes.compilationtime)

        #get output
        self.output = choo_choo_train.attributes.output

        #get compilation status
        self.compilation_status = choo_choo_train.attributes.compilationstatus

        #get block names
        self.block_names = choo_choo_train.attributes.block_names

        #get steps runtime
        self.compilation_steps = choo_choo_train.attributes.compilation_steps

        #get compilation steps 
        self.runtime_steps = choo_choo_train.attributes.runtime_steps

        #get num vars per block
        self.num_vars = choo_choo_train.attributes.num_vars

        #get num vars per block
        self.last_output = choo_choo_train.attributes.last_output

        #get ar num
        self.num_ar = choo_choo_train.attributes.num_ar

        #get records
        self.records = choo_choo_train.attributes.records

        #get num ifs
        self.num_ifs = choo_choo_train.attributes.num_ifs

        #get num ifs 
        self.num_loops = choo_choo_train.attributes.num_loops

        #get names of loops
        self.names_loops_blocks = choo_choo_train.attributes.names_loops_blocks

        #get loops executed
        self.cycles = choo_choo_train.attributes.cycles

        #get num ifs 
        self.total_vars = choo_choo_train.attributes.total_vars

        #get names of loops
        self.total_loops = choo_choo_train.attributes.total_loops

        #get loops executed
        self.total_ifs = choo_choo_train.attributes.total_ifs

        #get num of calls
        self.num_calls_block = choo_choo_train.attributes.num_calls_block

        #get loops executed
        self.runtime_per_block = choo_choo_train.attributes.runtime_per_block

        #set result array values
        self.result.append(self.code_js)
        self.result.append(self.runtime)
        self.result.append(self.compilation_time)
        self.result.append(self.output)
        self.result.append(self.compilation_status)
        self.result.append(self.block_names)
        self.result.append(self.compilation_steps)
        self.result.append(self.runtime_steps)
        self.result.append(self.num_vars)
        #index 9
        self.result.append(self.last_output)

        self.result.append(self.num_ar)
        self.result.append(self.records)
        self.result.append(self.num_ifs)
        self.result.append(self.num_loops)
        self.result.append(self.names_loops_blocks)
        self.result.append(self.cycles)
        self.result.append(self.total_vars)
        #index 17
        self.result.append(self.total_loops)
        self.result.append(self.total_ifs)
        self.result.append(self.num_calls_block)
        self.result.append(self.runtime_per_block)

        #clear attribtues for new program run
        choo_choo_train.clear_attributes()

        return self.result

    def build_program_result(self):
        #clear result array
        if self.result:
            while self.result:
                print self.result.pop()

        #compile and run
        choo_choo_train.compile_and_run()

        # get runtime and format
        if (choo_choo_train.attributes.runtime > 0.00001):
            self.runtime = '{:0.5f}'.format(choo_choo_train.attributes.runtime)
        
        else:
            self.runtime = '{:.5e}'.format(choo_choo_train.attributes.runtime)

        #get compile time and format
        if (self.compilation_time == 0):
            self.compilation_time = 0
        
        else:
            self.compilation_time = '{:.7e}'.format(choo_choo_train.attributes.compilationtime)

        #get output
        self.output = choo_choo_train.attributes.output

        #get compilation status
        self.compilation_status = choo_choo_train.attributes.compilationstatus

        #get block names
        self.block_names = choo_choo_train.attributes.block_names

        #get steps runtime
        self.compilation_steps = choo_choo_train.attributes.compilation_steps

        #get compilation steps 
        self.runtime_steps = choo_choo_train.attributes.runtime_steps

        #get num vars per block
        self.num_vars = choo_choo_train.attributes.num_vars

        #get num vars per block
        self.last_output = choo_choo_train.attributes.last_output

        #get ar num
        self.num_ar = choo_choo_train.attributes.num_ar

        #get records
        self.records = choo_choo_train.attributes.records

        #get num ifs
        self.num_ifs = choo_choo_train.attributes.num_ifs

        #get num ifs 
        self.num_loops = choo_choo_train.attributes.num_loops

        #get names of loops
        self.names_loops_blocks = choo_choo_train.attributes.names_loops_blocks

        #get loops executed
        self.cycles = choo_choo_train.attributes.cycles

        #get num ifs 
        self.total_vars = choo_choo_train.attributes.total_vars

        #get names of loops
        self.total_loops = choo_choo_train.attributes.total_loops

        #get loops executed
        self.total_ifs = choo_choo_train.attributes.total_ifs

        #get num of calls
        self.num_calls_block = choo_choo_train.attributes.num_calls_block

        #get loops executed
        self.runtime_per_block = choo_choo_train.attributes.runtime_per_block

        #set result array values
        self.result.append(self.code_js)
        self.result.append(self.runtime)
        self.result.append(self.compilation_time)
        self.result.append(self.output)
        self.result.append(self.compilation_status)
        self.result.append(self.block_names)
        self.result.append(self.compilation_steps)
        self.result.append(self.runtime_steps)
        self.result.append(self.num_vars)
        #index 9
        self.result.append(self.last_output)

        self.result.append(self.num_ar)
        self.result.append(self.records)
        self.result.append(self.num_ifs)
        self.result.append(self.num_loops)
        self.result.append(self.names_loops_blocks)
        self.result.append(self.cycles)
        self.result.append(self.total_vars)
        #index 17
        self.result.append(self.total_loops)
        self.result.append(self.total_ifs)
        self.result.append(self.num_calls_block)
        self.result.append(self.runtime_per_block)

        #clear attribtues for new program run
        choo_choo_train.clear_attributes()
        
    def compile(self, code_js):
        #set code value
        self.code_js = code_js

        #set code to compiler
        choo_choo_train.set_code(self.code_js)

        #build result array
        self.build_program_result()

        return self.result

