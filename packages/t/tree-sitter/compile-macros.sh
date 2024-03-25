#!/bin/sh
# SPDX-License-Identifier: GPL-2.0
# SPDX-FileCopyrightText: 2024 Björn Bidar
# based of compile-macros.sh  from python-rpm-macros
mkdir -p macros

### Lua: generate automagic from macros.in and macros.lua
(
    # copy macros.in up to LUA-MACROS
    sed -n -e '1,/^### LUA-MACROS ###$/p' macros.in

    # include "functions.lua", without empty lines, as %_treesitter_definitions
    echo "%_treesitter_definitions %{lua:"
    sed -n -r \
        -e 's/\\/\\\\/g' \
        -e '/^.+$/p' \
        functions.lua
    echo "}"

    INFUNC=0
    INMULTILINE_MACRO=0
    # brute line-by-line read of macros.lua
    IFS=""
    while read -r line; do
        if [ $INFUNC = 0 ] ; then
            if [ $INMULTILINE_MACRO = 1 ]  ;then
                if echo "$line" | grep -qE '^.*\]\]' ; then
                    INMULTILINE_MACRO=0
                fi
                echo "# $line"
            elif echo "$line" | grep -qE -- '--\[\[' ; then
                INMULTILINE_MACRO=1
                echo "# $line"
            elif echo "$line" | grep -qE -- '^--' ; then
                echo "# $line"
            elif echo "$line" | grep -q '^function '; then
                # entering top-level Lua function
                INFUNC=1;
                echo "$line" | sed -r -e 's/^function (.*)\((.*)\)$/%\1(\2) %{lua: \\/'
            else
                # outside function, copy
                # (usually this is newline)
                echo "$line"
            fi
        else
            if [ "$line" = "end" ]; then
                # leaving top-level Lua function
                INFUNC=0;
                echo '}'
            elif [ $INFUNC = 1 ]; then
                # inside function
                # double backslashes and add backslash to end of line
                echo "$line" | sed -e 's/\\/\\\\/g' -e 's/$/\\/'
            fi
        fi
    done < macros.lua

    # copy rest of macros.in
    sed -n -e '/^### LUA-MACROS ###$/,$p' macros.in
) > macros/050-automagic


### final step: cat macros/*, but with files separated by additional newlines
sed -e '$s/$/\n/' -s macros/* > macros.treesitter
