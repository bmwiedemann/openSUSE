#! /bin/bash
#set -x

spack_shtyp=bash

help() {
    echo -e "$0 [--help][--csh] lib ...
    Print set commands to set or set LD_LIBRARY_PATH to libraries
    specified as arguments as well as variables holding each library
    directory individually. These are usful when linking applications
    against these libraries.
    The variable names of the latter begin with 'LIB_' followed by
    the upper cased library name."
}

error() {
    echo -e "$1" >&2
}

contains() {
    local a=$1
    shift
    local -a b=($@)
    local i
    for i in ${b[*]}; do
	[ "$i" == "$a" ] && return 0
    done
    return 1
}

path_contains() {
    local a=$1
    local i
    [ -n "$2" ] || return 1
    OFS=$IFS
    IFS=:
    for i in $2; do
	IFS=$OFS
	[ "$i" == "$a" ] && return 0
    done
    return 1
}

print_env() {
    case $spack_shtyp in
	csh)
	    echo "setenv $1 $2" ;;
	bash)
	    if $spack_srcd; then
		eval $1=$2
		export $1
	    else
		echo -e "$1=$2\nexport $1"
	    fi ;;
    esac
}

get_paths()
{
    local -A libpaths includepaths
    local OFS=$IFS
    local ld_exist=$LD_LIBRARY_PATH
    IFS="
"
    local package_list="$1"
    local format=">   {hash:7} {name}{@version}{%compiler}{arch=architecture}"

    local l i
    for l in $(spack find --format "{name}" --paths $package_list); do
	local lib=${l%% *}
	local path=${l##* }
	if contains $lib "${!libpaths[@]}"; then
	    error "$lib matches multiple packages\n  Matching packages:"
	    spack find --format ${format} ${lib} >&2
	    error "  Use a more specific spec (e.g., prepend '/' to the hash)."
	    $spack_srcd || exit 1
	fi
	for i in lib64 lib; do
	    if [ -d $path/$i ]; then
		libpaths[$lib]="$path/$i"
		break
	    fi
	done
	if [ -d $path/include ]; then
	    includepaths[$lib]="$path/include"
	fi
    done
    IFS=$OFS

    local -A libs
    local ld_library_path
    for i in ${!libpaths[@]}; do
	libs[LIB_${i^^*}]="${libpaths[$i]}"
	path_contains ${libpaths[$i]} "${ld_exist}" || \
	    ld_library_path+="${libpaths[$i]}:"
    done
    for i in ${!includepaths[@]}; do
	eval [ "unset" = "\${INC_${i}:-unset}" ] &&
	print_env "INC_${i^^*}" "${includepaths[$i]}"
    done
    for i in ${!libs[@]}; do
	eval [ "unset" = "\${${i}:-unset}" ] && print_env $i "${libs[$i]}"
    done
    [ -n "$ld_library_path" ] && \
	print_env LD_LIBRARY_PATH "${ld_library_path}\$LD_LIBRARY_PATH"
}

spack_srcd=false
(
    [[ -n $ZSH_VERSION && $ZSH_EVAL_CONTEXT =~ :file$ ]] ||
    [[ -n $BASH_VERSION ]] && (return 0 2>/dev/null)
) && spack_srcd=true

while [ -n "$1" ]; do
    case $1 in
	*-help|*-h) help; $spack_srcd || exit 0 ;;
	*-csh|*-tcsh)
	    spack_shtyp=csh ;;
	*) package_list+=" $1" ;;
    esac
    shift
done

get_paths "$package_list"
