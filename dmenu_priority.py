#!/usr/bin/python2.7

import sys

command = sys.stdin.readlines()[0].strip()

'''if len(sys.argv) != 2:
    print("error")
    exit(1)

command = str(sys.argv[1])'''
f1 = "/home/petr/.cache/dmenu_run"
f2 = "/home/petr/.cache/dmenu_count"


def parse_cmd(cmd):
    i = cmd.index(" ") + 1
    return [
        cmd[:i].strip(),
        cmd[i:].strip()
    ]


def uniq_list(old_list):
    new_list = []
    for item in old_list:
        if item not in new_list:
            if not item.endswith("\n"):
                item += "\n"
            new_list.append(item)
    return new_list


def update_count(cmd):
    ret = []
    file_count = open(f2, "r")
    lines = file_count.readlines()
    file_count.close()

    file_count = open(f2, "w")
    for i, val in enumerate(lines):
        data = parse_cmd(val)
        if cmd == data[1]:
            updated = str(int(data[0]) + 1) + " " + data[1] + "\n"
            file_count.write(updated)
            ret.append(updated)
        else:
            file_count.write(val)
            ret.append(val)

    # Sort by first word (numeric)
    ret.sort(key=lambda tup: int(parse_cmd(tup)[0]), reverse=True)

    l = []
    for i, val in enumerate(ret):
        data = parse_cmd(val)
        l.append(data[1])

    if cmd not in l:
        l.append(cmd)
        file_count.write("1 " + cmd + "\n")

    file_count.close()

    return l


if __name__ == "__main__":
    file_cmd = open(f1, "r")

    counts = update_count(command)
    commands = file_cmd.readlines()
    with open(f1, "w") as f:
        f.writelines(uniq_list(counts + commands))

    file_cmd.close()
    print(command + "\n")
