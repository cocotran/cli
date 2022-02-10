from .date_time import get_date_time


def write_to_file(command, filename, content):
    if command == "->":
        with open(filename, "w+") as f:
            f.write(content)
    elif command == "->>":
        with open(filename, "a+") as f:
            f.write("\n" + content)


def redirect_echo(args, command, filename):
    # prints the argument given to the output file.
    # A warning is not printed out to the file.
    content = args.rstrip()
    write_to_file(command, filename, content)


def redirect_help(command, filename):
    content = "Help"
    write_to_file(command, filename, content)


def redirect_datetime(command, filename):
    # prints the datetime to the output file.
    content = get_date_time()
    write_to_file(command, filename, content)


def redirect(command, filename):
    try:
        if command[0] == "echo":
            redirect_echo(" ".join(command[1:-1]), command[-1], filename)

        elif command[0] == "help":
            redirect_help(command[-1], filename)

        elif command[0] == "datetime":
            redirect_datetime(command[-1], filename)

        else:
            print("Output redirect not supported:" + " ".join(command[:-1]))
    except:
        print("Output redirect error: " + command)
