#!/bin/ksh

a_sh=$(mktemp ${TMPDIR:-/tmp}/${0##*/}.XXXXXX) || exit 1
trap "rm -f $a_sh" EXIT

(cat > $a_sh) <<-EOF
	#!$SHELL
	check_proc_handle ()
	{
	    handleSoftLimit=$(ulimit -n)
	    echo \$handleSoftLimit > /dev/null
	}
	check_proc_handle
EOF
chmod +x $a_sh

typeset -lui count=${1:-4000}

while ((count-- > 0))
do
    $a_sh
done
