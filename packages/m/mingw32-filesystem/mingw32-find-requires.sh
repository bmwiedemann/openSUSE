#!/bin/bash

# This script reads filenames from STDIN and outputs any relevant provides
# information that needs to be included in the package.
target="mingw32"
host="i686-w64-mingw32"

scan_implibs=
if [ "$1" = "--scan-implibs" ]; then
  scan_implibs=1
  shift
fi

libs_to_exclude=
if [ "$1" = "--exclude" ]; then
  shift
  libs_to_exclude="$1"
  shift
fi

if [ -n "$1" ]; then
   package_name="$1"
fi

[ -z "$OBJDUMP" ] && OBJDUMP="$host-objdump"

# Get the list of files.

filelist=`sed "s/['\"]/\\\&/g"`

libs_to_exclude+="
    advapi32
    cfgmgr32
    comctl32
    comdlg32
    crypt32
    d3d8
    d3d9
    ddraw
    dnsapi
    dsound
    dwmapi
    dxva2
    evr
    gdi32
    gdiplus
    glu32
    glut32
    imm32
    iphlpapi
    kernel32
    ksuser
    mf
    mfplat
    mpr
    mscms
    mscoree
    msimg32
    msvcr71
    msvcr80
    msvcr90
    msvcrt
    mswsock
    netapi32
    odbc32
    ole32
    oleacc
    oleaut32
    opengl32
    psapi
    rpcrt4
    secur32
    setupapi
    shell32
    shlwapi
    user32
    usp10
    version
    wininet
    winmm
    wldap32
    ws2_32
    wsock32
    winhttp
"

exclude_pattern=""
for i in $libs_to_exclude; do
    if [ -z "$exclude_pattern" ]; then
        exclude_pattern="$i"
    else
        exclude_pattern="$exclude_pattern|$i"
    fi
done


dlls=$(echo "$filelist" | grep -v 'config$' | xargs file | grep executable | sed 's,:.*$,,g')
pcs=$(echo "$filelist" | grep '\.pc$')
configs=$(echo "$filelist" | grep 'config$')

for f in $dlls; do
    [ ! -f "$f" ] && continue
    "$OBJDUMP" -p "$f" | grep 'DLL Name' | tr "[:upper:]" "[:lower:]" |
        grep -Eo '[-._\+[:alnum:]]+\.dll' |
        grep -Ev "$exclude_pattern" |
        sed 's/\(.*\)/'"$target"'(\1)/'
done | sort -u

# scan import libraries - all archive files are scanned, not only
# '.dll.a' as some packages do not use the standard extension
# for import libraries
if [ -n "$scan_implibs" ]; then
    implibs=$(echo "$filelist" | grep '\.a$')
    for f in $implibs; do
        [ ! -f "$f" ] && continue
        "$STRINGS" "$f" | grep '\.dll$' |
            tr "[:upper:]" "[:lower:]" |
            grep -Ev "$exclude_pattern" |
            sed 's/\(.*\)/'"$target"'(\1)/'
    done | sort -u
fi

(
for g in $pcs; do
	dirname="${g%/*}"
	PKG_CONFIG_PATH="$dirname" "$host-pkg-config" --print-errors --print-requires "$g" | awk '{ print "'"$target"'(pkg:"$1")", $2, $3 }'
	PKG_CONFIG_PATH="$dirname" "$host-pkg-config" --print-errors --print-requires-private "$g" | grep -Ev "$exclude_pattern" | awk '{ print "'"$target"'(pkg:"$1")", $2, $3 }'
	for h in $(PKG_CONFIG_PATH="$dirname" "$host-pkg-config" --libs-only-l "$g" | sed 's#^\-l##g;s# \-l# #g'); do
		echo "$target(lib:$h)"
	done
done
for k in $configs; do
    for j in $(PKG_CONFIG="$host-pkg-config" "$k" --libs); do
        case "$j" in
            -l*)
                echo "$j" | sed 's#\-l##g' | grep -Ev "$exclude_pattern" | awk '{ print "'"$target"'(lib:"$1")" }'
		;;
        esac
    done
done
) | sort -u
