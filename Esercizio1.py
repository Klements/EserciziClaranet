import os
import sys
import argparse
from collections import defaultdict

def count_shebang (directory):
    #Defining the dictionary
    shebang_dict = defaultdict(int)

    #Iteration on everything in the specified directory
    for entry in os.listdir(directory):
        entry_path= os.path.join(directory, entry)

        #Check if the specified path is a file and is executable
        if os.path.isfile(entry_path) and os.access(entry_path, os.X_OK):
            #If so, open the file and check if it starts with the shebang
            try:
                file = open(entry_path, "r")
                first_line = file.readline().strip()

                if first_line.startswith("#!"):
                    shebang_dict[first_line] += 1
            except:
                continue

    return shebang_dict

def main():
    parser = argparse.ArgumentParser(
        prog='ExeByShebang',
        description='It count the numer of executable files and groups them by directory'
    )
    parser.add_argument("directory", help="Directory path to analyse")
    args = parser.parse_args()

    print(f"ExeCounter {args.directory}")

    #If specified path doesn't exist terminate execution
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} directory doesn't exist")
        sys.exit(1)

    shebang_list = count_shebang(args.directory)

    #Ordering the list by the numer of items
    for shebang, count in sorted(shebang_list.items(), key=lambda item: -item[1]):
        print(f"{count} {shebang}")


if __name__ == "__main__":
    main()
