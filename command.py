def kill(target):
    return "kill " + target


def check(command, target):
    if command == "kill":
        return kill(target)
    else:
        return "unknown command"
    