##
## initialize support to run cross compiled executables
##
# syntax: init_wine <path1> [<path2> ... [<pathn>]]
# @param  path1..n  pathes for adding to wine executable search path
#
# The function exits the shell script in case of errors
#
# @author Ralf Habacker <ralf.habacker@freenet.de>
# @developed at https://gitlab.freedesktop.org/dbus/dbus
#
init_wine() {
    if ! command -v wineboot >/dev/null; then
        echo "wineboot not found"
        exit 1
    fi

    # clean custom wine prefix if defined
    if test -n "$WINEPREFIX"; then
        if test -d "$WINEPREFIX"; then
            rm -rf "$WINEPREFIX"
        fi
    fi

    # run without X11 display to avoid that wineboot shows dialogs
    wineboot -fi
    winetricks nocrashdialog autostart_winedbg=disabled
}

init_wine_paths() {
    # set paths
    WINEPATH="$@" winetricks set_userpath

    # check if path(s) has been set and break if not
    local o=$(wine cmd /C "echo %PATH%")
    case "$o" in
        (*z:* | *Z:*)
            # OK
            ;;
        (*)
            echo "Failed to add Unix paths '$*' to path: Wine %PATH% = $o" >&2
            exit 1
            ;;
    esac
}

init_vars() {

    if test -z "$ci_runtime"; then
        ci_runtime=shared
    fi
    if test -z "$ci_host"; then
        ci_host=i686-w64-mingw32
    fi

    #export LDFLAGS="-${ci_runtime}-libgcc"
    libgcc_path=
    if [ "$ci_runtime" = "shared" ]; then
        libgcc_path=$(dirname "$("${ci_host}-gcc" -print-libgcc-file-name)")
    fi
}

init_vars
init_wine
init_wine_paths "/usr/$ci_host/sys-root/mingw/bin"${libgcc_path:+";$libgcc_path"}${@:+";$@"}
