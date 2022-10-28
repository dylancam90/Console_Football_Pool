import sys, os


def error(message):
    print(f"\n{message}")
    sys.exit(1)

def check_arguments(file, argc, argv):
    if argc != 3:
        error("Usage: python3 xls_to_csv.py excel_file.xlsx week_number")
    elif file.split(".")[1] != "xlsx":
        error("Unsupported file type, please use .xlsx")
    elif not check_for_file(file):
        error("File does not exist")
    elif int(argv[2]) <= 0:
        error("Week number needs to be a positive integer")
    return True


def check_for_file(name):
    if os.path.exists(name):
        return True
    return False