#!/bin/bash

# List all files, that depend on NEXT_LIST_REGEXP, explicitly or implicitly

cd $1

# Search all py files importing one of the mentioned modules:
make_extra_list() {
    NEWLIST=( $(grep -rl '\(import\|from\).* '"$NEXT_LIST_REGEXP"'\(,\|\.\| \|$\)' .) )
    EXTRA_LIST=( $(IFS=$'\n' ; echo "${EXTRA_LIST[*]}"$'\n'"${NEWLIST[*]}" | sed '/^$/d;s:^\./::' | sort -u) )
    NEWLIST=( "${NEWLIST[@]##*/}" )
    NEXT_LIST_REGEXP="\\(${NEWLIST[*]%.py}\\)"
    NEXT_LIST_REGEXP=${NEXT_LIST_REGEXP// /\\|}
}

# Search all py files that are imported by mentioned modules:
make_deplist() {
    NEWLIST=( $( ( (IFS=$'\n' ; echo "${NEWLIST[*]}"$'\n') ; sed 2>/dev/null -n 's/^from \(.*\) import.*/\1/p;s/^import \([^#]*\).* */\1/p' ${NEWLIST[@]} | sed 's/as .*//g;s/, */\n/g;s/ //g' | sed 's/$/.py/;s/\.py\.py$/.py/') | sort -u) )
}

OLDLIST=( EMPTY )
EXTRA_LIST=()
NEXT_LIST_REGEXP='\(xml\|lxml\)'
ITER=1

until test "${EXTRA_LIST[*]}" = "${OLDLIST[*]}" ; do
    OLDLIST=( "${EXTRA_LIST[@]}" )
    make_extra_list
    #echo "iter $ITER list: ${LIST[*]}"
    let ITER++
done

# We have a complete list of py files dependent on xml or lxml.
# Now we need a list of inx module descriptors.
INX_REGEXP="${EXTRA_LIST[*]//./\\.}"
INX_REGEXP="\\(>${INX_REGEXP// /<\\|>}<\\)"
INX_EXTRA_LIST=( $(grep -l "$INX_REGEXP" *.inx) )

# inx files that do not belong to INX_EXTRA_LIST will be a part of INX_STD_LIST
INX_STD_LIST=()
for FILE in *.inx ; do
    eval 'case $FILE in '"$(IFS='|' ; echo "${INX_EXTRA_LIST[*]}")"') continue;; esac'
    INX_STD_LIST[${#INX_STD_LIST[@]}]=$FILE
done

# Now create list of py files that should belong to std package:
OLDLIST=( EMPTY )
NEWLIST=( $(sed -n 's@.*<dependency type="executable" location="extensions">\(.*\)\.py</dependency>.*@\1.py@p' ${INX_STD_LIST[@]}) )
ITER=1
until test "${NEWLIST[*]}" = "${OLDLIST[*]}" ; do
    OLDLIST=( "${NEWLIST[@]}" )
    make_deplist
    #echo "iter $ITER list: ${LIST[*]}"
    let ITER++
done
STD_LIST=( "${NEWLIST[@]}" )

# Now create list of py files that are required by extra modules:
# (If no std module needs it, then they will belong to extra package.)
OLDLIST=( EMPTY )
NEWLIST=( $(sed -n 's@.*<dependency type="executable" location="extensions">\(.*\)\.py</dependency>.*@\1.py@p' ${INX_EXTRA_LIST[@]}) )
ITER=1
until test "${NEWLIST[*]}" = "${OLDLIST[*]}" ; do
    OLDLIST=( "${NEWLIST[@]}" )
    make_deplist
    #echo "iter $ITER list: ${LIST[*]}"
    let ITER++
done
EXTRADEP_LIST=( ${NEWLIST[@]} )

# And now verify everything and generate final list:
# Now its safe to ignore subdirectory issue - we know where they belong.
RC=0
IFS=$'\n'
exec 3>$OLDPWD/inkscape.lst
echo >&3 "%defattr(-,root,root)"
for FILE in ${INX_STD_LIST[@]} ; do
    echo >&3 $2$FILE
done
exec 4>$OLDPWD/inkscape-extensions-extra.lst
echo >&4 "%defattr(-,root,root)"
for FILE in ${INX_EXTRA_LIST[@]} ; do
    echo >&4 $2$FILE
done
for FILE in *.py ; do
    eval '
	case $FILE in
	    cdr*|dia*|fig*|*gimp*|sk*) continue;;
	    '"$(IFS='|' ; echo "${EXTRA_LIST[*]}")"') echo >&4 $2$FILE; continue;;
	    '"$(IFS='|' ; echo "${STD_LIST[*]}")"') echo >&3 $2$FILE; continue;;
	    '"$(IFS='|' ; echo "${EXTRADEP_LIST[*]}")"') echo >&4 $2$FILE; continue;;
	esac'
	echo "ERROR: Undecided file $FILE"
    RC=1
done

exec 3>&-
exec 4>&-

exit $RC
