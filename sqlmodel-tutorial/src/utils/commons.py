import os
import sys


def exclusion_db():
    try:
        if (os.path.isfile("db.db")):
            os.remove("db.db")
            print("File Deleted successfully\n")
        else:
            print("File does not exist\n")
    except:
        print("Unexpected error:", sys.exc_info()[0], "\n")
