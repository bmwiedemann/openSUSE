#!/bin/bash

# Automatically find Provides and Requires for typelib() gobject-introspection bindings.
# can be started with -R (Requires) and -P (Provides)

# Copyright 2011 by Dominique Leuenberger, Amsterdam, Netherlands (dimstar [at] opensuse.org)
# This file is released under the GPLv2 or later.

function split_name_version {
base=$1
tsymbol=${base%-*}
# Sometimes we get a Requires on Gdk.Settings.foo, because you can directly use imports.gi.Gdk.Settings.Foo in Javascript.
# We know that the symbol in this case is called Gdk, so we cut everything after the . away.
symbol=$(echo $tsymbol | awk -F. '{print $1}')
version=${base#*-}
# In case there is no '-' in the filename, then the split above 'fails' and version == symbol (thus: no version specified)
if [ "$tsymbol" = "$version" ]; then
	unset version
fi
}

function split_name_version2 {
  symbol=$(echo $1 | awk -F: '{sub(/^.*{/, "", $1); print $1}' | sed "s:[' ]::g")
  version=$(echo $1 | awk -F: '{print $2}' | sed "s:[' ]::g")
}

# some javascript code imports gi like this (seen since GNOME 43, e.g. GNOME Maps)
# import 'gi://GeocodeGlib?version=2.0'
function split_name_versionjs_gi_name_version {
  symbol=$(echo $1 | awk -F? '{print $1}')
  version=$(echo $1 | awk -F? '/version=/ {print $2}' | sed 's/version=//')
}

function print_req_prov {
echo -n "typelib($symbol)"
if [ ! -z "$version" ]; then
	echo " = ${version}"
else
	echo ""
fi
}

function find_provides {
while read file; do
	case $file in
		*.typelib)
			split_name_version $(basename $file | sed 's,.typelib$,,')
			print_req_prov
			;;
	esac
done
}

function gresources_requires {
# GNOME is embedding .js files into ELF binaries for faster startup.
# As a result, we need to extract them and re-run the scanner over the
# embedded files.
# We extract all the gresources embedded in ELF binaries and start
# gi-find-deps.sh recusively over the extracted file list.
tmpdir=$(mktemp -d)
for resource in $($gresourcecmd list "$1" 2>/dev/null); do
  mkdir -p $tmpdir/$(dirname $resource)
  $gresourcecmd extract "$1" $resource > $tmpdir/$resource
done
find $tmpdir -type f | sort | sh $0 -R
rm -rf "$tmpdir"
}

function python_requires {
	for module in $(grep -h -P "^\s*from gi\.repository import (\w+)" $1 | sed -e 's:#.*::' -e 's:raise ImportError.*::' -e 's:.*"from gi.repository import .*".*::' | sed -e 's,from gi.repository import,,' -r -e 's:\s+$::g' -e 's:\s+as\s+\w+::g' -e 's:,: :g'); do
		split_name_version $module
		print_req_prov
		# Temporarly disabled... this is not true if the python code is written for python3... And there seems no real 'way' to identify this.
		# echo "python-gobject >= 2.21.4"
	done
	for module in $(grep -h -P -o ".*(gi\.require_version\(['\"][^'\"]+['\"],\s*['\"][^'\"]+['\"]\))" $1 | sed  -e 's:#.*::' -e 's:.*gi.require_version::' -e "s:[()\"' ]::g" -e 's:,:-:'); do
		split_name_version $module
		print_req_prov
	done
        # python glue layers (/gi/overrides) import their typelibs slightly different
	for module in $(grep -h -P -o "=\s+(get_introspection_module\(['\"][^'\"]+['\"]\))" $1 | sed -e 's:#.*::' -e 's:=.*get_introspection_module::' -e "s:[()\"' ]::g"); do
		split_name_version $module
		print_req_prov
	done
}

function javascript_requires {
  # parse the new import style in 3.32
	for module in $(grep -r -h -A2 'const {' $1 | paste -s -d ' ' | grep '} = imports.gi;' | sed 's/imports.gi;.*/imports.gi;/' | awk -F '[{}]' '{print $(NF>1?NF-1:"")}' | tr ',' '\n' | tr -d ' ' | awk -F ':' '{print $1}'); do
		split_name_version $module
		print_req_prov
	done
  # parse the old import style before 3.32
	for module in $(grep -h -P -o "imports\.gi\.([^\s'\";]+)" $1 | grep -v "imports\.gi\.version" | sed -r -e 's,\s+$,,g' -e 's,imports.gi.,,'); do
		split_name_version $module
		print_req_prov
	done
	for module in $(grep -h -P -o "imports\.gi\.versions.([^\s'\";]+)\s*=\s*['\"].+['\"]" $1 | \
		sed -e 's:imports.gi.versions.::' -e "s:['\"]::g" -e 's:=:-:' -e 's: ::g'); do
		split_name_version $module
		print_req_prov
	done
  # some javascript code imports gi like this (seen since GNOME 43, e.g. GNOME Maps)
  # import 'gi://GeocodeGlib?version=2.0'
        for module in $(grep -h -P -o "['\"]gi://([^'\"]+)" $1 | sed "s|['\"]gi://||"); do
                split_name_versionjs_gi_name_version $module
                print_req_prov
        done
    # This is, at the moment, specifically for Polari where a "const { Foo, Bar } = imports.gi;" is used.
	for module in $(grep -h -E -o "\{ \w+(: \w+|, \w+)+ \} = imports.gi;" $1 | \
        sed -r -e '0,/\w+:\s\w+/ s/:\s\w+//g' -e 's: = imports.gi;:: ; s:\{ :: ; s: \}:: ; s/,//g'); do
		split_name_version $module
		print_req_prov
	done
	# Remember files which contain a pkg.require() call
	if pcre2grep -M "pkg.require\\(([^;])*" $1 > /dev/null; then
		# the file contains a pkg.require(..) list... let's remember th is file for the in-depth scanner
		if [ -n "$jspkg" ]; then
			jspkg=$1:${jspkg}
		else
			jspkg=$1
		fi
	fi
	# remember files which contain exlucde filters used against pkg.require()
	if pcre2grep -M "const RECOGNIZED_MODULE_NAMES =([^;])*" $1 > /dev/null; then
		# the file contains RECOGNIZED_MODULE_NAMES list. We remember the file name for the follow up filtering
		if [ -n "$jspkgfilt" ]; then
			jspkgfilt=$1:${jspkgfilt}
		else
			jspkgfilt=$1
		fi
	fi

}

function javascript_pkg_filter {
# For now this is a dummy function based on gnome-weather information
#for file in $jspkgfilt; do
#	FILTER=($(pcre2grep -M "const RECOGNIZED_MODULE_NAMES =([^;])*" $file | grep -o "'.*'" | sed "s:'::g"))
#done
  FILTER=('Lang' 'Mainloop' 'Signals' 'System' 'Params')
}

function javascript_pkg_requires {
# javascript files were found which specify pkg.require('..': '..'[,'..': '']); list
# This is used in some apps in order to have a 'centralized' point to specify all package dependencies.
# once we reach this function, we already know which file(s) contain the pkg.require(..) list.
oldIFS=$IFS
IFS=:
for file in "$jspkg"; do
	IFS=$'\n'
	PKGS=$(pcre2grep -M "pkg.require\\(([^;])*" $file | grep -o -E "'?.*'?: '.*'")
	for pkg in $PKGS; do
		split_name_version2 $pkg
		found=0
		for (( i=0 ; i<${#FILTER[@]} ; i++ )); do
			if [ "$symbol" = "${FILTER[$i]}" ]; then
				found=1
			fi
		done
		if [ $found -eq 0 ]; then
			print_req_prov
		fi
	done
	IFS=:
done
IFS=$oldIFS

}

function typelib_requires {
	split_name_version $(basename $1 | sed 's,.typelib$,,')
	oldIFS=$IFS
	IFS=$'\n'
	for req in $(g-ir-inspect --print-shlibs --print-typelibs $symbol --version $version); do
		case $req in
			typelib:*)
				module=${req#typelib: }
				split_name_version $module
				print_req_prov
				;;
			shlib:*)
				echo "${req#shlib: }${shlib_64}"
				;;
		esac
	done
	IFS=$oldIFS
}

function find_requires {
# Currently, we detect:
# - in python:
#   . from gi.repository import foo [Unversioned requirement of 'foo']
#   . from gi.repository import foo-1.0 [versioned requirement]
#   . gi.require_version('Gtk', '3.0') (To specify a version.. there is still an import needed)
#   . And we do not stumble over:
#     from gi.repository import foo as _bar
#     from gi.repository import foo, bar
# - in JS:
#   . imports.gi.foo; [unversioned requirement of 'foo']
#   . imports.gi.foo-1.0; [versioned requirement of 'foo']
#   . imports.gi.versions.Gtk = '3.0';
#   . const { foo, bar } = imports.gi;
#   . The imports can be listed on one line, and we catch them.

while read file; do
	case $file in
		*.js)
			javascript_requires "$file"
			;;
		*.py)
			python_requires "$file"
			;;
		*.typelib)
			typelib_requires "$file"
			;;
		*.gresource)
			gresources_requires "$file"
			;;
		*)
			case $(file -b $file) in
				*[Pp]ython*script*)
					python_requires "$file"
					;;
				*JavaScript*source*)
		                        javascript_requires "$file"
					;;
				*ELF*)
					gresources_requires "$file"
					;;
			esac
			;;
	esac
done
# The pkg filter is a place holder. This should read the filter from the javascript files.
#if [ -n "$jspkgfilt" ]; then
javascript_pkg_filter
#fi
# in case the javascript parser above detected files which specify pkg.require, we enter the more in-depth scanning scheme for those files.
if [ -n "$jspkg" ]; then
	javascript_pkg_requires
fi
}

function inList() {
  for word in $1; do
    [[ "$word" = "$2" ]] && return 0
  done
  return 1
}

# Confer with /usr/lib/rpm/platforms
x64bitarch="aarch64 loongarch64 mips64 mips64el mips64r6 mips64r6el ppc64 ppc64le riscv64 s390x sparc64 x86_64"

for path in \
	$(for tlpath in \
	$(find ${RPM_BUILD_ROOT}/usr/lib64 ${RPM_BUILD_ROOT}/usr/lib /usr/lib64 /usr/lib -name '*.typelib' 2>/dev/null); do
        	dirname $tlpath; done | sort --unique ); do
	export GI_TYPELIB_PATH=$GI_TYPELIB_PATH:$path
done

if which gresource >/dev/null 2>&1; then
  gresourcecmd=$(which gresource 2>/dev/null)
else
  grsourcecmd="false"
fi

if inList "$x64bitarch" "${HOSTTYPE}"; then
	shlib_64="()(64bit)"
fi
case $1 in
	-P)	
		find_provides
		;;
	-R)
		find_requires
		;;
esac

