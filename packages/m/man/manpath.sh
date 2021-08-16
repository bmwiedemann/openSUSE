#
# Current manpath
#
if test -x /usr/bin/manpath -a -z "$MANPATHISSET"
then
    _tmpenv="$MANPATH"
    unset MANPATH
    _tmpman="$(/usr/bin/manpath -q)"
    if test -n "$_tmpenv" -a "$_tmpenv" != ${_tmpman} ; then
	MANPATH="${_tmpenv}:${_tmpman}"
    else
	MANPATH="${_tmpman}"
    fi
    unset _tmpenv _tmpman
    MANPATHISSET=yes
    export MANPATH MANPATHISSET
fi
