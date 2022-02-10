def echo(args):
    content = ""
    if not args:
        # if no args are given, warn the user.
        content += "The echo command was given no arguments."
    else:
        content += args.rstrip().replace('"', "")
    print(content)
