import random

class Compiler_Handler:
    def __init__(self):
        self.runtime = 0
        self.compilation_time = 0
        self.result = []
        self.output = ""
        self.code_js = []
        # if 1 compilation successful
        self.compilation_status = ""


    def compile(self, code_js):
        if self.result:
            while self.result:
                self.result.pop()

        self.code_js = code_js
        self.runtime = '{:.7e}'.format(random.uniform(0, 1))
        self.compilation_time = '{:.7e}'.format(random.uniform(0, 1))
        self.output = "Output from compiler handler"
        self.compilation_status = 1;

        self.result.append(self.code_js[0])
        self.result.append(self.runtime)
        self.result.append(self.compilation_time)
        self.result.append(self.output)
        self.result.append(self.compilation_status)

