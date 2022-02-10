import os
import sys
import socket
import subprocess

from constructs import *


def myshell(input_file) -> list:
    try:
        with open(input_file, "r") as f:
            settings = f.readlines()
            if len(settings) != 3:
                print("Invalid input file")
                raise SystemExit
            return settings
    except Exception as err:
        print(err)
    raise SystemExit


def get_input(user_host):
    # input is taken in and returned as list of arguments.
    line = input(user_host + ":~$ ").strip()
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
    # output redirection on echo and help.
    try:
        # NOTE: order of conditional statements is important

        if len(args) == 0:
            pass

        # exit
        elif args[0] == "exit":
            exit()

        # redirects or append
        elif len(args) > 2 and (args[-2] == "->" or args[-2] == "->>"):
            redirect(args[:-1], args[-1])

        # help
        elif args[0] == "help" or args[0] == "h":
            help()

        # echo
        elif args[0] == "echo":
            echo(" ".join(args[1:]))

        # datetime
        elif args[0] == "datetime":
            print_date_time()

        # # &
        # elif args[-1] == "&":
        #     p = subprocess.Popen(args[:-1])
        #     p.wait()

        # else:
        #     childprocess(args)
    except EOFError as e:
        print("Error while trying to execute" + args)


def main(args):
    user = ""
    host = ""
    path = ""

    if len(args) > 1:
        settings: list = myshell(args[1])
        user = settings[0].strip()
        host = settings[1].strip()
        path = settings[2].strip()
    else:
        try:
            import pwd

            user = pwd.getpwuid(os.getuid()).pw_name
        except:
            user = os.getenv("username") if os.getenv("username") != "" else "user"
        finally:
            host = socket.gethostname()

    clear()
    print(f"Type 'help' (or h) for available commands.\n")
    while True:
        args = get_input(user + "@" + host)
        execute(args)


if __name__ == "__main__":
    main(sys.argv)
