import os
import sys
import pwd
import socket
import subprocess

from constructs import *


def myshell(fileIn):
    try:
        with open(fileIn, "r") as file:
            i = 1
            for line in file:
                print("\n\033[1mLine {} contains: \033[0m".format(i) + line)
                execute(line.split())
                i += 1
    except:
        print("File input error")
    raise SystemExit


def get_input(user_host):
    # input is taken in and returned as list of arguments.
    line = input(user_host + "~$ ").strip()
    args = line.split()
    return args


def childprocess(args):
    # child process takes the form; python3 example.py
    try:
        subprocess.call([args[0], args[1]])
    except:
        print("Subprocess was not able to call [" + "] [".join(args) + "]")


def execute(args):
    # try execute the args.
    # otherwise, generate EOF error.
    # output redirection on dir, environ, echo, & help.
    try:
        if len(args) == 0:
            pass

        # help
        elif args[0] == "help" or args[0] == "h":
            help()

        # echo
        elif args[0] == "echo":
            echo(" ".join(args[1:]))

        # exit
        elif args[0] == "exit":
            exit()

        # # redirects or append
        # elif len(args) > 2 and (args[-2] == "->" or args[-2] == "-->"):
        #     redirect(args[:-1], args[-1])

        # # &
        # elif args[-1] == "&":
        #     p = subprocess.Popen(args[:-1])
        #     p.wait()

        # else:
        #     childprocess(args)
    except EOFError as e:
        print("Error while trying to execute" + args)


def main(args):
    if len(args) > 1:
        myshell(args[1])
    os.environ["SHELL"] = "\033[1m" + str(os.getcwd()) + "/myshell\033[0m"
    clear()
    print(f"Type 'help' (or h) for available commands.\n")
    while True:
        user_host = pwd.getpwuid(os.getuid()).pw_name + "@" + socket.gethostname()
        args = get_input(user_host)
        execute(args)


if __name__ == "__main__":
    # batchfile would represent sys.argv
    main(sys.argv)
