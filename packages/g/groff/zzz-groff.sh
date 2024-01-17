#
#    /etc/profile.d/zzz-groff.sh
#
#    This script must be executed after setting the LANG variable.

case "${LANGUAGE-${LC_ALL-${LC_MESSAGES-${LANG}}}}" in
    ja*|zh*|ko*)
        unset GROFF_NO_SGR
        export MAN_KEEP_FORMATTING=yes
    ;;
esac

