import sys, os


def error(message):
    print(f"\n{message}")
    sys.exit(1)

def check_arguments(file, argc, argv):
    if argc != 3:
        error("Usage: python3 doc.py file.docx week_number")
    elif file.split(".")[1] != "docx":
        error("Unsupported file type, please use .docx")
    elif not check_for_file(file):
        error("File does not exist")
    elif int(argv[2]) <= 0:
        error("Week number needs to be a positive integer")
    return True

    # if argc != 3:
    #     error("Usage: python3 doc.py file.docx week_number")
    # elif file.split(".")[1] != "doc":
    #     error("Unsupported file type, please use .docx")
    # elif not check_for_file(file):
    #     error("File does not exist")
    # elif int(argv[2]) <= 0:
    #     error("Week number needs to be a positive integer")
    # return True


def check_for_file(name):
    if os.path.exists(name):
        return True
    return False

def remove_file(file):
    os.remove(file) 