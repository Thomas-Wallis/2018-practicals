def main():
    user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    name = input("Please enter your name here: ")
    if name in user_names:
        print("Access granted")
    else:
        print("Access denied")


main()