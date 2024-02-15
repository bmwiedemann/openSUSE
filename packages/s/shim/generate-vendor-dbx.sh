#!/bin/bash

set -e

# random UUID for SUSE
owner=353f0911-0788-451c-aaf7-31688391e8fd

: > vendor-dbx-opensuse.esl
: > vendor-dbx-sles.esl
# vendor dbx file with all certs for testing environment
: > vendor-dbx.esl

for cert in "$@"; do
	esl="${cert##*/}"
	esl="${cert%.crt}.esl"
	cert-to-efi-sig-list -g "$owner" "$cert" "$esl"
	case "$cert" in
		*openSUSE*) cat "$esl" >> "vendor-dbx-opensuse.esl" ;;
		*SLES*) cat "$esl" >> "vendor-dbx-sles.esl" ;;
	esac
	cat "$esl" >> "vendor-dbx.esl"
done
