from lexer import lexer
from interpretor import interpret

while True:
    line = input(">> ")
    if line == 'exit':
        break 
    interpret(lexer(line))
