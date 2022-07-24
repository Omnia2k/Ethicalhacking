import os
print ('Cmd applicaation')
while True:
    try:
        command = input('Enter your command : \n')
        if command.lower() == 'exit':
            print ('Bye')
            break
        os.system(command)
     # os.system is a method that is used to execute commands 
     # like subprocess.run
    except:
        command = input()

