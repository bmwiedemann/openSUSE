# Adapted from https://raw.githubusercontent.com/openSUSE/scout/master/handlers/bin/command_not_found_bash
# under MIT license

command_not_found_handle() {
    #FIXME: locales
    #export TEXTDOMAINDIR=/usr/share/locale
    #export TEXTDOMAIN=command-not-found
    local cnf_bin=${COMMAND_NOT_FOUND_BIN:-/usr/bin/cnf}

    local cmd state rest
    local -i pid ppid pgrp session tty_nr tpgid

    # do not run when inside Midnight Commander or within a Pipe
    if test -n "$MC_SID" -o ! -t 1 ; then
        eval 'echo $"$1: command not found" >&2'
        return 127
    fi

    # do not run when within a subshell
    read pid cmd state ppid pgrp session tty_nr tpgid rest  < /proc/self/stat
    if test $$ -eq $tpgid ; then
        eval 'echo $"$1: command not found" >&2'
        return 127
    fi

    # TODO: to enable a way how to enable the cnf prompt only?
    # call command-not-found directly
    test -x "${cnf_bin}" && "${cnf_bin}" "$1"

    return 127
}
