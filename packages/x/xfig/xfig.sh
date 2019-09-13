#!/bin/bash
#
# Reset UTF-8 charmaping to a more xfig compatible one
#
for lc in LANG LC_CTYPE LC_NUMERIC LC_TIME LC_COLLATE	\
	  LC_MONETARY LC_MESSAGES LC_PAPER LC_NAME	\
	  LC_ADDRESS LC_TELEPHONE LC_MEASUREMENT	\
	  LC_IDENTIFICATION LC_ALL
do
    eval val="\$$lc"
    test -n "$val" || continue
    case "$val" in
	*.UTF-8)    eval $lc=\${val%[.@]*} ;;
    esac
done
unset ret val
exec -a $0 @@BINDIR@@/xfig.bin ${1+"$@"}
