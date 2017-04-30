import sys
sys.path.insert(0,'..')

import choo_choo_train
import random


class Compiler_Handler:
    def __init__(self):
        self.runtime = 0
        self.compilation_time = 0
        self.result = []
        self.output = ""
        self.code_js = ""
        # if 1 compilation successful, 2 comp error, 3 runtime error
        self.compilation_status = 0
        #index 5
        self.block_names = []
        #index 6
        self.runtime_steps = []
        #index 7
        self.compilation_steps = []
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


    def compile(self, code_js):
        if self.result:
            while self.result:
                self.result.pop()

        self.code_js = code_js

        #set code to compiler
        choo_choo_train.set_code(self.code_js)

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

        self.result.append(self.code_js)
        self.result.append(self.runtime)
        self.result.append(self.compilation_time)
        self.result.append(self.output)
        self.result.append(self.compilation_status)
        self.result.append(self.block_names)
        self.result.append(self.compilation_steps)
        self.result.append(self.runtime_steps)
        self.result.append(self.num_vars)
        self.result.append(self.last_output)
        self.result.append(self.num_ar)
        self.result.append(self.records)
        self.result.append(self.num_ifs)

        return self.result

