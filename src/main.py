import sys
import utils

print("Welcome to Togepi!")
DEBUG = False
if len(sys.argv) > 1 and sys.argv[1] == "debug":
    DEBUG = True

while True:
    command = input(">>> ")
    if command == "exit":
        sys.exit(0)
    else:
        try:
            utils.runCommand(command)
        except Exception as e:
            if DEBUG:
                print(e)
            else:
                print("Invalid command. Type help to learn more.\n")
