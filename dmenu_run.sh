#!/bin/sh

# Original
# dmenu_path | dmenu "$@" | ${SHELL:-"/bin/sh"} &

# Debug
# COMMAND=`/bin/sh dmenu_path | dmenu "$@"`
# echo $COMMAND | /home/petr/Workspace/dmenu_priority/dmenu_priority.py | ${SHELL:-"/bin/sh"} &

# Production
dmenu_path | dmenu "$@" | /home/petr/Workspace/dmenu_priority/dmenu_priority.py | ${SHELL:-"/bin/sh"} &
