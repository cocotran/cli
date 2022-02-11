import os
import sys
import socket
import re
import threading

from constructs import *

global PATH


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


def executable(args):
    for dir in re.split(':', os.environ['C:\\Users\\danik\\AppData\\Local\\Discord']):
        try:
            os.execv(dir + '/' + args[0], args)
        except FileNotFoundError:
            pass
    print(f"Could not execute '{args[0]}'. Command not found.")
    exit()

def bgprocess(args):
    #Background process 
    
        n = os.fork()
        if n < 0:
            print("Error")
            exit(1)
        elif n == 0:
            executable(args)


def execute(args):
    # try execute the args.
    # otherwise, generate EOF error.
    # output redirection on echo and help.
    t = None

    # NOTE: order of conditional statements is important

    if len(args) == 0:
        pass

    # exit
    elif args[0] == "exit":
        exit()

    # redirects or append
    elif len(args) > 2 and (args[-2] == "->" or args[-2] == "->>"):
        t = threading.Thread(target=redirect, args=(args[:-1], args[-1]))
        t.start()

    # help
    elif args[0] == "help" or args[0] == "h":
        t = threading.Thread(target=help)
        t.start()

    # echo
    elif args[0] == "echo":
        t = threading.Thread(target=echo, args=(" ".join(args[1:]),))
        t.start()

    # datetime
    elif args[0] == "datetime":
        t = threading.Thread(target=print_date_time)
        t.start()

    elif args[0] == "test":
        t = threading.Thread(target=test)
        t.start()

    else:
        try:
            t = threading.Thread(target=executable, args=args)
        except:
            print("Invalid command entered")

    # # &
    if args[-1] == "&":
        pass
    else:
        t.join()
            

def main(args):
    user = ""
    host = ""

    if len(args) > 1:
        settings: list = myshell(args[1])
        user = settings[0].strip()
        host = settings[1].strip()
        PATH = settings[2].strip()
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
