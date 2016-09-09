#!/usr/bin/python2.7
import sys
import os

FILE_COUNT = "/home/petr/.cache/dmenu_count"
FILE_RUN = "/home/petr/.cache/dmenu_run"


def clean():
    if os.path.isfile(FILE_COUNT):
        print("Remove file {0}".format(FILE_COUNT))
        os.remove(FILE_COUNT)
    if os.path.isfile(FILE_RUN):
        print("Remove file {0}".format(FILE_RUN))
        os.remove(FILE_RUN)


def merge():
    commands = []

    if not os.path.isfile(FILE_RUN):
        return

    # Read all used commands
    with open(FILE_COUNT, "r") as f:
        for cmd in f.readlines():
            i = cmd.find(" ") + 1
            if i > 0:
                commands.append(cmd[:i].strip() + '\n')

    # Read all system commands
    with open(FILE_RUN, "r") as f:
        for command in f.readlines():
            if command not in commands:
                commands.append(command)

    with open(FILE_RUN, "w") as f:
        f.writelines(commands)


def update(command):
    commands = []

    # Move up or add command
    with open(FILE_COUNT, "r") as f:

        # Add new command at bottom if i doesn't exist in command list
        new = True

        for cmd in f.readlines():
            i = cmd.find(" ") + 1
            if i == 1:
                continue

            key = cmd[:i].strip()
            val = cmd[i:].strip()

            if key == command:
                val = str(int(val) + 1)
                new = False

            commands.append((
                key, val
            ))

        if new:
            commands.append((
                command, "1"
            ))

    commands.sort(key=lambda x: int(x[1]), reverse=True)
    with open(FILE_COUNT, "w") as f:
        for cmd in commands:
            f.write(str(cmd[0]) + ' ' + str(cmd[1]) + '\n')

    print(command + '\n')

if __name__ == "__main__":

    if len(sys.argv) != 2:
        exit(1)

    op = sys.argv[1]
    if op == "clean":
        clean()
        exit(0)

    # Create file if it doesn't exist
    if not os.path.isfile(FILE_COUNT):
        with open(FILE_COUNT, "w"):
            pass

    # Note: FILE_RUN should be created by dmenu

    if op == "merge":
        merge()
    elif op == "update":
        readlines = sys.stdin.readlines()
        if len(readlines) > 0:
            cmd = readlines[0].strip()
            update(cmd)
