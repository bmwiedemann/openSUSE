#!/bin/bash

# Extract list of variables supported by su/runuser.
#
# If you edit this file, you will probably need to edit
# shadow-login_defs-check.sh from shadow sources in a similar way.

set -o errexit

echo -n "Checking login.defs variables in util-linux... " >&2
(
	grep -rh getlogindefs . |
		sed -n 's/^.*getlogindefs[a-z_]*("\([A-Z0-9_]*\)".*$/\1/p'
	grep -rh logindefs_setenv . |
		sed -n 's/^.*logindefs_setenv*("[A-Z0-9_]*", "\([A-Z0-9_]*\)".*$/\1/p'
) | LC_ALL=C sort -u >util-linux-login_defs-vars.lst

if test $(sha1sum util-linux-login_defs-vars.lst | sed 's/ .*$//') != 713b442bf6d16353b7f74538ece165b424f90932 ; then

	echo "does not match!" >&2
	echo "Checksum is: $(sha1sum util-linux-login_defs-vars.lst | sed 's/ .*$//')" >&2

cat >&2 <<EOF

You have to perform following steps:

Check whether the error is false positive (script failed to extract
variables) or true positive (variable list changed).

If it is false positive:
- Fix this script.
- The same fix is needed in shadow package in shadow-login_defs-check.sh.

If it is true positive:

- Check-out shadow package and call shadow-login_defs-check.sh. If it
  fails, check the output.
- Update shadow shadow-login_defs-util-linux.patch, if needed.
- Verify that the new variable is included in FOREIGNDEFS in lib/getdef.c.
  If not, add it to shadow-login_defs-util-linux.patch and send the chunk
  to the upstream.
- If shadow-login_defs-util-linux.patch was updated, update
  login_defs-support-for-util-linux symbol version in both shadow and
  util-linux spec files accordingly.
- Update checksum in this script.
- Possibly update su.default with these new list of su/runuser specific
  variables:
EOF
	echo -n "  " >&2
	(
		grep -rh getlogindefs login-utils/su-common.c |
			sed -n 's/^.*getlogindefs[a-z_]*("\([A-Z0-9_]*\)".*$/\1/p'
		grep -rh logindefs_setenv  login-utils/su-common.c |
			sed -n 's/^.*logindefs_setenv*("[A-Z0-9_]*", "\([A-Z0-9_]*\)".*$/\1/p'
	) | LC_ALL=C sort -u | tr '\n' ' ' | sed 's/ /, /g;s/, $//' >&2
	echo -e '\n' >&2

	exit 1
else
	echo "OK" >&2
fi
