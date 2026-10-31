#!/bin/sh
# Generate RPM Supplements: modalias(...) lines for the ratbagd subpackage
# from libratbag's data/devices/*.device files.
# Usage: generate-ratbag-supplements.sh TARBALL [PATCH...] [TREEDIR...]
#   TARBALL   upstream tarball; scanned via tar without unpacking
#   PATCH     device backport patch; added (+DeviceMatch=) lines scanned
#   TREEDIR   unpacked tree; TREEDIR/data/devices/*.device scanned
# Prints one 'Supplements:' line per USB ID (uppercase, sorted, deduped).
# Fails loudly on unreadable input, malformed IDs, or an empty result.
set -eu

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT
raw="$tmpdir/raw"
: > "$raw"

for src in "$@"; do
	[ -e "$src" ] || continue
	if [ -d "$src" ]; then
		sed -n 's/^DeviceMatch=//p' "$src"/data/devices/*.device >> "$raw"
	elif [ "${src%.tar.xz}" != "$src" ] || [ "${src%.tar.gz}" != "$src" ] || [ "${src%.tar}" != "$src" ]; then
		tar -xOf "$src" --wildcards '*/data/devices/*.device' | sed -n 's/^DeviceMatch=//p' >> "$raw"
	else
		sed -n '/^+++/!s/^+.*DeviceMatch=//p' "$src" >> "$raw"
	fi
done

ids=$(tr ';' '\n' < "$raw" | tr -d '\r' | grep -i '^usb:' | sed 's/^[Uu][Ss][Bb]://' | tr 'a-f' 'A-F' | sort -u)
[ -n "$ids" ] || { echo "generate-ratbag-supplements.sh: no USB IDs found" >&2; exit 1; }

printf '%s\n' "$ids" | while IFS= read -r id; do
	case "$id" in
		[0-9A-F][0-9A-F][0-9A-F][0-9A-F]:[0-9A-F][0-9A-F][0-9A-F][0-9A-F])
			printf 'Supplements:    modalias(usb:v%sp%sd*dc*dsc*dp*ic*isc*ip*in*)\n' \
				"${id%%:*}" "${id##*:}" ;;
		*)
			echo "generate-ratbag-supplements.sh: malformed USB ID '$id'" >&2
			exit 1 ;;
	esac
done
