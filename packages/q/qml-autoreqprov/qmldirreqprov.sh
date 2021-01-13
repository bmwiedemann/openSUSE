#!/bin/bash
# SPDX-FileCopyrightText: 2020-2021 Fabian Vogt <fabian@ritter-vogt.de>
# SPDX-License-Identifier: GPL-3.0-or-later

set -euo pipefail

provides=
requires=
ret=0

while [ $# -gt 0 ]; do
	case $1 in
	--provides)
		provides=1
		;;
	--requires)
		requires=1
		;;
	*)
		echo "Unknown argument $1" >&2
		exit 1
	esac
	shift
done

declare -A moduleExports
# foundModuleExport Module.Uri.42 69
# In the moduleExports array, it sets the version of Module.Uri.42 to 69, if lower
foundModuleExport() {
	if [ ${moduleExports[$1]:=0} -lt $2 ]; then
		moduleExports[$1]=$2
	fi
}

# Hack: We have to load .so files which need libraries inside the build root
if ! [[ -z "${RPM_BUILD_ROOT:-}" ]]; then
	for path in /{,usr/}lib{,64}; do
		export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-}:${RPM_BUILD_ROOT}${path}"
	done
fi

while read file; do
	if ! [[ $file =~ /qt([5-9])/qml/.*/qmldir$ ]]; then
		continue
	fi

	qtver=${BASH_REMATCH[1]}
	dir="$(dirname "${file}")"
	module="$(awk '/^module/ { print $2; exit }' "$file")"

	if [[ -z "${module}" ]]; then
		echo "$file has no module declaration - ignoring" >&2
		continue
	fi

	if [[ $requires ]]; then
		gawk '$1 == depends && match($2, /^([0-9]+)\.([0-9]+)$/, ver) { printf "qt'${qtver}'qmlimport(%s.%d) >= %d", $2, ver[1], ver[2]; }' "$file"
	fi

	if [[ $provides ]]; then
		# Handle regular (.qml, .js) exports
		while read maj min; do
			foundModuleExport "qt${qtver}qmlimport(${module}.${maj})" "$min"
		done < <(gawk 'match($0, /(singleton )?[^ ] ([0-9]+)\.([0-9]+) [^ ]+\.(qml|js)$/, type) { printf "%d %d\n", type[2], type[3]; }' "$file")

		# Handle plugins
		plugins=()

		while read pluginname location; do
			if [[ -z $location ]]; then
				location="$dir"
			elif [[ $location == /* ]]; then
				location="${RPM_BUILD_ROOT:-}/$location/"
			else
				location="${dir}/$location}/"
			fi

			plugins+=("${location}/${pluginname}")
		done < <(awk '$1 == "plugin" { printf "lib%s.so %s\n", $2, $3; }' "$file")

		if [ ${#plugins[@]} -eq 0 ]; then
			# No plugins?
			continue
		fi

		if ! command -v qmlpluginexports-qt${qtver} &>/dev/null; then
			echo "Module uses plugin, but qmlpluginexports-qt${qtver} not installed!" >&2
			ret=1
			continue
		fi
			
		for plugin in "${plugins[@]}"; do
			# TODO: Get exit status of qmlpluginexports
			while read import min; do
				if [[ $import != *${module}* ]]; then
					echo "Ignoring ${import}" >&2
					continue
				fi
				foundModuleExport "qt${qtver}qmlimport(${import})" "$min"
			done < <(qmlpluginexports-qt${qtver} "$plugin" "$module")
		done
	fi
done

for export in "${!moduleExports[@]}"; do
	echo "${export} = ${moduleExports["$export"]}"
done

exit $ret
