import os


def kill(target):
    if target != "":
        return "Killed " + target + "!"
    else:
        return "I hope you're not talking to me"


def hello(target):
    if target != "":
        return "My name is not " + target + "."
    else:
        return "Hello!"


def parse_input(input):
    input = input.split()
    try:
        return input[0], input[1]
    except:
        return input[0], ""
        

def check(input):
    print(input)
    command, target = parse_input(input)
    if command == "hello":
        return hello(target)
    elif command == "kill":
        return kill(target)
    else:
        return "unknown command or target"
        
    