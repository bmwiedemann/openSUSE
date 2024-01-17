#!/bin/bash

for man in uucp.1 uux.1 uustat.1 uuname.1 uulog.1 uuto.1 uupick.1   \
	   cu.1 uucico.8 uuxqt.8 uuchk.1 uuconv.1 uusched.8
do
     test -e $man && continue
     touch .#$man
     (	echo NAME
	echo "${man%.[0-9]} - "
	echo SYNOPSIS
	info -f ./uucp.info "Invoking ${man%.[0-9]}" | tail -n +5 ) | \
     rman -n ${man%.[0-9]} -s ${man#*.} -K -f roff > $man
     echo $man
done

