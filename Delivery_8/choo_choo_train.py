import sys
import parser
import virtual_machine
import global_scope
import time

#If no argument was given, make the user input a file
if(len(sys.argv) < 2):
    file_name = raw_input('Input the name of the file to run: ')
#If an argument was given, read that file
else:
    file_name = sys.argv[1]
    
#counts execution time
start_time = time.time()

compilation_time = time.time() - start_time

parser.start_compilation(file_name)
virtual_machine.start_execution()

#finished execution
execution_time = time.time() - global_scope.timer_counter - start_time
print compilation_time, "seconds"
print execution_time, "seconds"