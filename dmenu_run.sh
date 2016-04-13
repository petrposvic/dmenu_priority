#!/bin/sh

# i3 launches dmenu_run file located in /usr/local/bin/dmenu_run. Modify it!

# Original
# dmenu_path | dmenu "$@" | ${SHELL:-"/bin/sh"} &

# Debug
# COMMAND=`/bin/sh dmenu_path | dmenu "$@"`
# echo $COMMAND | /home/petr/Workspace/dmenu_priority/dmenu_priority.py | ${SHELL:-"/bin/sh"} &

# Production
dmenu_path | dmenu "$@" | /home/petr/Workspace/dmenu_priority/dmenu_priority.py | ${SHELL:-"/bin/sh"} &
