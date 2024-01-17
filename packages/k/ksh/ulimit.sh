#!/usr/bin/ksh

PATH=/bin:/usr/bin:/usr/sbin:/sbin
typeset -lui count=${1:-4000}
typeset -ilu err=0

trap 'echo "[${0##*/}: error count at $err]"' ERR

while ((count-- > 0))
do
    ulimit -s || let err++
    ulimit -n || let err++
    ulimit -q || let err++
done > /dev/null

echo "[${0##*/}: error count at $err]"
((err == 0)) || exit 1
