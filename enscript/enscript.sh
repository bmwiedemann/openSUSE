#!/bin/bash
#
# enscript.sh:	Workaround for getting enscript handling
#		UTF-8 partly.  Partly means that iconv is
#		used to get the UTF-8 encoding into the
#		natural laint encoding of the base language
#		provided by the enviroment variable LANG.
#
# Author: Werner Fink <werner@suse.de>
#

declare -i err cnt opt isf
declare -a CMDLINE FILES

unset ${!LC_*}
ENC=$(LANG=${LANG%.*} locale charmap 2> /dev/null < /dev/null)
test "$ENC" = "ISO-8859-1"  && ENC=ISO-8859-15
test "${ENC%%_*}" = "ANSI"  && ENC=ISO-8859-1
test "$ENC" = "UTF-8"       && ENC=ISO-8859-1
test "${LANG%.*}" = "en_US" && ENC=ISO-8859-1

case "$@" in
*-X[[:blank:]]UTF-8*|*--encoding=UTF-8*) ;;
*)  case "${ENC%-*}" in
	ISO-8859|KOI8) ;;
	*) exec -a enscript enscript.bin -X $ENC ${1+"$@"} ;;
    esac
    ;;
esac

#
# All long options of enscript
#
LONG="columns:,pages:,file-align:,header:,no-header,truncate-lines,line-numbers::,\
setpagedevice:,escapes::,highlight::,font:,header-font:,print-anyway,fancy-header::,\
no-job-header,highlight-bars:,indent:,filter:,borders,page-prefeed,no-page-prefeed,\
lineprinter,lines-per-page:,mail,media:,copies:,newline:,missing-characters,output:,\
printer:,quiet,silent,landscape,portrait,baselineskip:,statusdict:,title:,tabsize:,\
underlay::,nup:,verbose,version,language:,options:,encoding:,no-formfeed,pass-through,\
color::,continuous-page-numbers,download-font:,extended-return-values,filter-stdin:,\
footer:,h-column-height:,help,help-highlight,highlight-bar-gray:,list-media,margins:,\
non-printable-format:,nup-columnwise,nup-xpad:,nup-ypad:,page-label-format:,ps-level:,\
printer-options:,rotate-even-pages,slice:,style:,swap-even-page-margins,toc,ul-angle:,\
ul-font:,ul-gray:,ul-position:,ul-style:,word-wrap"

#
# All normal options of enscript
#
SHORT="#:,1,2,a:,A:,b:,B,c,C::,d:,D:,e::,E::,f:,F:,g,G,h,H:,i:,I:,j,J:,k,K,l,L:,m,M:,\
o:,O,p:,P:,q,r,R,s:,S:,t:,T:,u::,U:,v,V,w:,W:,X:,z,Z"

#
# We need the file names provided on the command line
# or the information if we read from stdin.
#
# Why sed? Just to get the `=' back instead of ` ' the empty space
# which are inserted by getopt(1) and also the empty space on the
# short options -C, -e, -E, -H, and -u.
#
FILES=($(getopt -o $SHORT -l $LONG -s bash -q -- "$@" | \
    LC_ALL=POSIX sed -r 's|.*[[:blank:]]+--[[:blank:]]?||'
    test ${PIPESTATUS[0]} -eq 0 || exit 1))
let err=$?

if test $err -ne 0 ; then
    # Let enscript do the error message
    exec -a enscript enscript.bin ${1+"$@"}
fi

eval FILES=( "${FILES[@]}" ) 
CMDLINE=("$@")

let isf=0
let opt=0
while ((opt<=${#CMDLINE[@]})) ; do
    arg="${CMDLINE[$opt]}"
    if test $isf -ne 0 ; then
	unset CMDLINE[$opt]
	let isf++
    fi
    if test "$arg" = "${FILES}" ; then
	unset CMDLINE[$opt]
	let isf++
    fi
    let opt++
done

test "${FILES[*]}" = "-" && FILES=()
set -- "${CMDLINE[@]}" "${FILES[@]}"

#
# Just for encoding given on command line:
# allow the user to overwrite autodetection
#
case "$@" in
*-X*|*--encoding=*|*--version*|*--help*|*-V*|*--list-media*)
    exec -a enscript enscript.bin ${1+"$@"}
    ;;
*-I*|*--filter=*)
    exec -a enscript enscript.bin ${1+"$@"}
    ;;
esac

if test ${#FILES[@]} -gt 0 ; then
    #
    # We have real files, maybe with spaces in their path name
    #
    exec -a enscript enscript.bin -X $ENC --filter="[[ \$(file -b '%s' 2>/dev/null) =~ 'UTF-8 Unicode text' ]] && iconv -c -f UTF-8 -t $ENC '%s' || cat '%s'" ${1+"$@"}
fi

#
# Just handle stdin at last but not least
#
tmpfile=$(mktemp /tmp/en_2.XXXXXXXXXX) || exit 1
trap 'rm -f $tmpfile' EXIT SIGTERM SIGQUIT SIGHUP SIGPIPE
cat > $tmpfile
exec 0< $tmpfile
if [[ $(file -b $tmpfile 2>/dev/null) =~ 'UTF-8 Unicode text' ]] ; then
    enscript.bin -X $ENC --filter="iconv -c -f UTF-8 -t $ENC" ${1+"$@"}
else
    enscript.bin -X $ENC ${1+"$@"}
fi
exit $?
