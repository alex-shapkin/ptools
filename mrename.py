import os
import sys

from enum import IntEnum


##########################
# Definitions
class RenameArguments(IntEnum):
    WorkingDirectory = 1
    OldName = 2
    NewName = 3
    ValidArgumentsCount = 4


def multiple_rename(directory, old_name, new_name):
    for file in os.listdir(directory):
        if os.path.isdir(file):
            continue

        if file == old_name:
            source = os.path.join(directory, old_name)
            destination = os.path.join(directory, new_name)

            print(source + " ==> " + destination)

            os.rename(source, destination)


def print_help():
    print("Renames files that has different path extensions but the same file name.")
    print("Do not specify path extension when specifying files names.")
    print("Usage: mrename source_directory old_name new_name.")
    

##########################
# Code
arguments_count = len(sys.argv)

if 1 == arguments_count or (2 == arguments_count and sys.argv[1] == "-h"):
    print_help()
    exit(0)

if RenameArguments.ValidArgumentsCount != arguments_count:
    print("Invalid arguments")
    print_help()
    exit(1)

source_directory = sys.argv[RenameArguments.WorkingDirectory]
old_name = sys.argv[RenameArguments.OldName]
new_name = sys.argv[RenameArguments.NewName]

multiple_rename(source_directory, old_name, new_name)
