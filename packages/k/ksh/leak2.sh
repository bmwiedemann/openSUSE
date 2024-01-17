#!/usr/bin/ksh

foo=0
LoopCountForMEMSAP=0
bla=234
typeset -lui count=${1:-4000}
typeset -lui leak=0

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

fusub()
{
    datum=`date +%S`
    interval=$((10 - datum%10))
}

fvsub()
{
    datum=$(date +%S)
    interval=$((10 - datum%10))
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
    foo=$((foo+1))

    if ((count%2 == 0)) ; then
	datum=`fusub`
    else
	datum=$(fvsub)
    fi

    curstate=($(vm))
    lessequal || let leak++
    oldstate=(${curstate[@]})

done

echo "[${0##*/}: leak count at $leak]"
((leak < 60)) || exit 1
