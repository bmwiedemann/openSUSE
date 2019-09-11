#!/usr/bin/ksh

PATH=/bin:/usr/bin:/usr/sbin:/sbin

getSampleInterval() { return 0; }
typeset -lui count=${1:-4000}
typeset -ilu leak=0

typeset -a curstate=(0 0 0)
typeset -a oldstate=(0 0 0)

vm()
{
    typeset size
    typeset key unit result=""
    while read key size unit; do
	case "$key" in
	VmSize*) result=${result:+"$result "}$size ;;
	VmRSS*)  result=${result:+"$result "}$size ;;
        VmData*) result=${result:+"$result "}$size ;;
	esac
    done < /proc/$$/status
    echo $result
}

lessequal()
{
    typeset -i ret=0
    ((${curstate[0]} > ${oldstate[0]})) && let ret=1
    ((${curstate[1]} > ${oldstate[1]})) && let ret=1
    ((${curstate[2]} > ${oldstate[2]})) && let ret=1
    return $ret
}

oldstate=($(vm))
while ((count-- > 0))
do
    interval=$(getSampleInterval)

    curstate=($(vm))
    lessequal || let leak++
    oldstate=(${curstate[@]})

done

echo "[${0##*/}: leak count at $leak]"
((leak < 20)) || exit 1
