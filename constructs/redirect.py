def redirect(command, filename):
    # main overwrite that will deal with dir, environ, echo & help
    # the redirect will have parameters for the sign ( > or >> )
    # and parameter for the filename.
    try:
        if "dir" == command[0]:
            # redirect(command, sign, filename)
            redirect_dir("".join(command[1:-1]), command[-1], filename)

        elif "environ" == command[0]:
            # redirect(sign, filename)
            redirect_environ(command[-1], filename)

        elif "echo" == command[0]:
            # redirect(command, sign, filename)
            redirect_echo(" ".join(command[1:-1]), command[-1], filename)

        elif "help" == command[0]:
            # redirect(sign, filename)
            redirect_help(command[-1], filename)
        else:
            print("Output redirection unavailable for *" + " ".join(command[:-1]) + "*")
    except:
        print("Error while trying to execute" + command)


def redirect_dir(args, sign, filename):
    # lists the contents of the directory to the output file.
    if not args:
        args = "."
    content = "-----------------\n"
    for line in os.listdir(args):
        content += line + "\n"
    content += "-----------------"
    if ">" == sign:
        with open(filename, "w+") as f:
            f.write(content)
    else:
        with open(filename, "a+") as f:
            f.write("\n" + content)


def redirect_environ(sign, filename):
    # lists the environ strings to the output file.
    environ = os.environ
    content = ""
    for k, v in environ.items():
        content += k + "=" + v + "\n"
    if ">" == sign:
        with open(filename, "w+") as f:
            f.write(content)
    else:
        with open(filename, "a+") as f:
            f.write("\n" + content)


def redirect_echo(args, sign, filename):
    # prints the argument given to the output file.
    # A warning is not printed out to the file.
    # instead, a blank space is printed.
    content = args.rstrip()
    if ">" == sign:
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
