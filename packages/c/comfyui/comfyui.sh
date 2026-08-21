#!/bin/sh
# ComfyUI launcher. Keep models, custom_nodes, input, output, temp, user
# and the sqlite database under a writable per-user directory rather than
# the read-only prefix. Honour an explicit --base-directory / --database-url.

python="@@PYTHON@@"
datadir="@@DATADIR@@"

has_base=0
has_db=0
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
    esac
done

if [ "$has_base" -eq 0 ]; then
    if [ -n "${XDG_DATA_HOME:-}" ]; then
        base=$XDG_DATA_HOME/comfyui
    elif [ -n "${HOME:-}" ]; then
        base=$HOME/.local/share/comfyui
    else
        base=/tmp/comfyui
    fi
    mkdir -p "$base" || exit 1
    set -- --base-directory "$base" "$@"
fi

if [ "$has_db" -eq 0 ]; then
    if [ -z "$base" ]; then
        if [ -n "${XDG_DATA_HOME:-}" ]; then
            base=$XDG_DATA_HOME/comfyui
        elif [ -n "${HOME:-}" ]; then
            base=$HOME/.local/share/comfyui
        else
            base=/tmp/comfyui
        fi
    fi
    mkdir -p "$base/user" || exit 1
    set -- --database-url "sqlite:///$base/user/comfyui.db" "$@"
fi

exec "$python" "$datadir/main.py" "$@"
