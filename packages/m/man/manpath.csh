#
# Current manpath
#
if (-x /usr/bin/manpath && ! ${?MANPATHISSET}) then
    set _tmpman=`(unsetenv MANPATH; /usr/bin/manpath -q)`
    if ( ${?MANPATH} ) then
	if (${MANPATH} != ${_tmpman}) then
	    setenv MANPATH "${MANPATH}:${_tmpman}"
	else
	    setenv MANPATH "${_tmpman}"
	endif
    else
        setenv MANPATH "${_tmpman}"
    endif
    setenv MANPATHISSET yes
endif
