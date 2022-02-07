def redirect_echo(args, command, filename):
    # prints the argument given to the output file.
    # A warning is not printed out to the file.
    content = args.rstrip()
    if command == "->":
        with open(filename, "w+") as f:
            f.write(content)
    else:
        with open(filename, "a+") as f:
            f.write("\n" + content)


def redirect_help(sign, filename):
    # prints the whole content of the help file to the output file.
    f = open("README", "r")
    content = f.read()
    if ">" == sign:
        with open(filename, "w+") as f:
            f.write(content)
    else:
        with open(filename, "a+") as f:
            f.write("\n" + content)
    f.close()


def redirect(command, filename):
    try:
        if "echo" == command[0]:
            redirect_echo(" ".join(command[1:-1]), command[-1], filename)

        elif "help" == command[0]:
            redirect_help(command[-1], filename)

        else:
            print("Output redirect not supported:" + " ".join(command[:-1]))
    except:
        print("Output redirect error: " + command)
