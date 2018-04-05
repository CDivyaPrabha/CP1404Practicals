usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
flag = 0
for name in usernames:
    if name == username:
        flag = 1
        break
if flag == 0:
    print("Access denied")
else:
    print("Access granted")
