#!/bin/sh
#
# Turns on or off the nss-sysinit module db by editing the
# global PKCS #11 congiguration file.
#
# This script can be invoked by the user as super user.
# It is invoked at nss-sysinit post install time with argument on
# and at nss-sysinit pre uninstall with argument off. 
#
usage()
{
  cat <<EOF
Usage: setup-nsssysinit [on|off]
  on  - turns on nsssysinit
  off - turns off nsssysinit
EOF
  exit $1
}

# validate
if test $# -eq 0; then
  usage 1 1>&2
fi

# the system-wide configuration file
p11conf="/etc/pki/nssdb/pkcs11.txt"
# must exist, otherwise report it and exit with failure
if [ ! -f $p11conf ]; then
  echo "Could not find ${p11conf}"
  exit 1
fi

on="1"
case "$1" in
  on | ON )
    cat ${p11conf} | \
     sed -e 's/^library=$/library=libnsssysinit.so/' \
         -e '/^NSS/s/\(Flags=internal\)\(,[^m]\)/\1,moduleDBOnly\2/' > \
    ${p11conf}.on
    mv ${p11conf}.on ${p11conf}
    ;;
  off | OFF )
    if [ ! `grep "^library=libnsssysinit" ${p11conf}` ]; then
      exit 0
    fi
    cat ${p11conf} | \
    sed -e 's/^library=libnsssysinit.so/library=/' \
        -e '/^NSS/s/Flags=internal,moduleDBOnly/Flags=internal/' > \
        ${p11conf}.off
    mv ${p11conf}.off ${p11conf}
    ;;
  * )
    usage 1 1>&2
    ;;
esac
