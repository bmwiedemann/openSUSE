#!/bin/bash

# Extract list of variables supported by su/runuser.
#
# If you edit this file, you will probably need to edit
# shadow-login_defs-check.sh from shadow sources in a similar way.

set -o errexit

echo -n "Checking login.defs variables in pam... " >&2
grep -rh LOGIN_DEFS . |
	sed -n 's/^.*search_key *([A-Za-z_]*, *[A-Z_]*LOGIN_DEFS, *"\([A-Z0-9_]*\)").*$/\1/p' |
	LC_ALL=C sort -u >pam-login_defs-vars.lst

if test $(sha1sum pam-login_defs-vars.lst | sed 's/ .*$//') != 3c6e0020c31609690b69ef391654df930b74151d ; then

	echo "does not match!" >&2
	echo "Checksum is: $(sha1sum pam-login_defs-vars.lst | sed 's/ .*$//')" >&2

cat >&2 <<EOF

You have to perform following steps:

Check whether the error is false positive (script failed to extract
variables) or true positive (variable list changed).

If it is false positive:
- Fix this script.
- The same fix is needed in shadow package in shadow-login_defs-check.sh.

If it is true positive:
- Check-out shadow package and call shadow-login_defs-check.sh.
- Compare its output shadow-login_defs-check-pam.lst with
  pam-login_defs-vars.lst in the pam build directory.
- Update shadow encryption_method_nis.patch, if needed.
- If encryption_method_nis.patch was updated, update
  login_defs-support-for-pam symbol version in both shadow and
  pam spec files accordingly.
- Update checksum in this script.

EOF

	exit 1
else
	echo "OK" >&2
fi
