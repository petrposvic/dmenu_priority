# dmenu priority filter

Priority filter for dmenu. Shows often used commands on top. Needs /usr/bin/python2.7

Modify /usr/local/bin/dmenu_run (or /usr/bin/dmenu_run) file to apply this filter.

Use filter with **merge** parameter before any execution. It merges generated file from dmenu and this filter and
creates new dmenu file where frequently used application are on top. 
```
main.py merge
```

Use filter with **update** parameter after dmenu processing. It increases number of launches for launching application
and updates file for this filter. 
```
main.py update
```

## Example #1
```
#!/bin/sh
cachedir=${XDG_CACHE_HOME:-"$HOME/.cache"}
if [ -d "$cachedir" ]; then
        cache=$cachedir/dmenu_run
else
        cache=$HOME/.dmenu_cache # if no xdg dir, fall back to dotfile in ~
fi

/home/petr/Programy/dmenu_priority/main.py merge

(
        IFS=:
        if stest -dqr -n "$cache" $PATH; then
                stest -flx $PATH | sort -u | tee "$cache" | dmenu "$@"
        else
                dmenu "$@" < "$cache"
        fi
) | /home/petr/Programy/dmenu_priority/main.py update | ${SHELL:-"/bin/sh"} &
```

## Example #2
```
#!/bin/sh
/home/petr/Programy/dmenu_priority/main.py merge
dmenu_path | dmenu "$@" | /home/petr/Programy/dmenu_priority/main.py update | ${SHELL:-"/bin/sh"} &
```

## Troubleshooting

If new installed app is not in dmenu, delete .cache/dmenu_run.

```
rm ~/.cache/dmenu_run
```

It will be re-created after first launch and merged with your priority list after second launch.
