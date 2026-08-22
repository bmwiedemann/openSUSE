#!/bin/sh
# ComfyUI launcher. Keep models, custom_nodes, input, output, temp, user
# and the sqlite database under a writable per-user directory rather than
# the read-only prefix. Honour an explicit --base-directory / --database-url.

python="@@PYTHON@@"
datadir="@@DATADIR@@"

has_base=0
has_db=0
query_only=0
base=""
prev=""
for arg in "$@"; do
    if [ "$prev" = "--base-directory" ]; then
        base=$arg
        prev=""
        continue
    fi
    case $arg in
        --base-directory=*)
            base=${arg#--base-directory=}
            has_base=1
            ;;
        --base-directory)
            has_base=1
            prev=--base-directory
            ;;
        --database-url|--database-url=*)
            has_db=1
            ;;
        -h|--help|--version|--list-feature-flags)
            query_only=1
            ;;
    esac
done

if [ -z "$base" ]; then
    if [ -n "${XDG_DATA_HOME:-}" ]; then
        base=$XDG_DATA_HOME/comfyui
    elif [ -n "${HOME:-}" ]; then
        base=$HOME/.local/share/comfyui
    else
        base=/tmp/comfyui
    fi
fi

# main.py exits inside argparse for the query-only flags, so the launcher
# must not create anything either.
if [ "$query_only" -eq 0 ]; then
    if [ "$has_base" -eq 0 ]; then
        mkdir -p "$base" || exit 1
    fi
    if [ "$has_db" -eq 0 ]; then
        mkdir -p "$base/user" || exit 1
    fi
fi

if [ "$has_base" -eq 0 ]; then
    set -- --base-directory "$base" "$@"
fi

if [ "$has_db" -eq 0 ]; then
    set -- --database-url "sqlite:///$base/user/comfyui.db" "$@"
fi

# A base directory relocates custom_nodes into the per-user tree and hides
# the nodes shipped in the read-only package. Register the packaged
# directory as an additional search path so both are loaded. Appended
# rather than prepended: the option takes nargs='+' and would otherwise
# swallow a following bare argument. Removing the file disables the extra
# path instead of aborting the server.
if [ -f "$datadir/comfyui-packaged-paths.yaml" ]; then
    set -- "$@" --extra-model-paths-config "$datadir/comfyui-packaged-paths.yaml"
fi

exec "$python" "$datadir/main.py" "$@"
