#
#    /etc/profile.d/zzz-groff.csh
#
#    This script must be executed after setting the LANG variable.

if ( $?LANG ) then

switch ( $LANG )
    case ja*:
    setenv MAN_KEEP_FORMATTING yes
    unsetenv GROFF_NO_SGR
    case zh*:
    setenv MAN_KEEP_FORMATTING yes
    unsetenv GROFF_NO_SGR
    case ko*:
    setenv MAN_KEEP_FORMATTING yes
    unsetenv GROFF_NO_SGR
endsw

endif
