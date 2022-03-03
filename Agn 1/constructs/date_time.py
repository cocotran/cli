from datetime import datetime


def print_date_time():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def get_date_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
