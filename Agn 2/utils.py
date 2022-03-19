def read_input(input_file) -> list:
    try:
        with open(input_file, "r") as f:
            settings = f.readlines()
            return settings
    except Exception as err:
        print(err)
    raise SystemExit
