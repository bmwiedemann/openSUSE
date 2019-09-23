#!/bin/sh
#
# In the current package's specfile, updates a block delimited
# by "# BEGIN" / "# END" lines to contain BuildRequires: lines
# for each rubygem rpm (or rpm matching a given pattern) which
# has been built by the project.
#
# This gives us project-build-time dependency checking without the
# performance impact that specifying BuildRequires lines within
# each gem would cause.  For more information, see:
#
#   http://en.opensuse.org/openSUSE:Packaging_Ruby#Compensating_for_lack_of_BuildRequires
#
# Usage:
# ------
#
# 1. Ensure you have an "all-rubygems-good" package or similar
#    in your project.  If in doubt, copy the one from
#    devel:languages:ruby:extensions.
#
# 2. cd to a working copy
#
# If you're feeling lazy, you are probably fine skipping the next two
# steps.
#
# 3. Run this script with the -l option and make sure you understand
#    any differences between each repository/arch combination in the
#    numbers of matching gems found.
#
# 4. If you don't, run with -l REPO ARCH to compare individual lists
#    of matching gems.
#
# 5. If you want a BuildRequires: list of matching gems from *all*
#    repo/arch combinations, run again with no arguments.
#
#      OR
#
#    If you want a BuildRequires: list of matching gems from a specific
#    repo/arch combinations, run again with REPO ARCH as arguments.
#
# 6. osc diff to review the changes to the spec file, then osc commit.

me=`basename $0`

DEFAULT_PATTERN="rubygem-"

main () {
    parse_opts "$@"

    if [ -z "$project" ]; then
        project=$( osc info | sed -ne '/^Project name: / { s///; p }' )
        if [ -z "$project" ]; then
            echo "Couldn't establish build service project name." >&2
            echo "Are you inside a package working directory?" >&2
            exit 1
        fi
    fi
    echo "Project: $project"

    case "$project" in
        home:*:branches:*)
            cat <<EOF >&2

WARNING: you are running this in a branch.

You probably need to specify the parent project via -P,
otherwise you may not get the dependencies you want.

EOF
            ;;
    esac            

    specfile=$( ls -1 *.spec )
    if ! [ -f "$specfile" ]; then
        echo "Couldn't find spec file." >&2
        echo "Are you inside a package working directory?" >&2
        exit 1
    fi

    if [ -n "$list" ]; then
        if [ -n "$repo" ]; then
            get_buildrequires_lines "$repo" "$arch"
        else
            list_matches
        fi
    else
        if [ -n "$repo" ]; then
            get_buildrequires_lines "$repo" "$arch" | update_spec
        else
            find_all_matches | update_spec
        fi
    fi
}

usage () {
    # Call as: usage [EXITCODE] [USAGE MESSAGE]
    case "$1" in
        [0-9])
            exit_code="$1"
            shift
            ;;
        *)
            exit_code=1
            ;;
    esac
    if [ -n "$1" ]; then
        echo "$*" >&2
        echo
    fi

    cat <<EOF >&2
Usage: $me [options] [REPOSITORY ARCH]
Options:
  -h, --help         Show this help and exit
  -l, --list         List matching rpms for the given repository / arch.
                     If no repository specified, show counts of matching
                     rpms per repository / arch.
  -P, --project=PROJ Retrieve rpm lists from PROJ, not the current project.
  -p, --pattern=PAT  Set the pattern to match rpms by [$DEFAULT_PATTERN]
EOF
    exit "$exit_code"
}

parse_opts () {
    list=
    project=
    pattern="$DEFAULT_PATTERN"

    while [ $# != 0 ]; do
        case "$1" in
            -h|--help)
                usage 0
                ;;
            -l|--list)
                list=y
                shift
                ;;
            -p|--pattern)
                pattern="$2"
                shift 2
                ;;
            -P|--project)
                project="$2"
                shift 2
                ;;
            -*)
                usage "Unrecognised option: $1"
                ;;
            *)
                break
                ;;
        esac
    done

    if [ $# = 1 ]; then
        usage "Insufficient arguments."
    fi

    if [ $# -gt 2 ]; then
        usage "Too many arguments."
    fi

    repo="$1"
    arch="$2"
}

get_buildrequires_lines () {
    repo="$1" arch="$2"
    osc api "/build/$project/$repo/$arch/_repository" | \
        grep "binary .*filename=\"$pattern" | \
        sed -e 's,.*  <binary filename=",,; s,\.rpm".*,,; s,^,BuildRequires: ,' | \
        grep -v debuginfo
}

list_matches () {
    echo
    echo "Matching rpms per repository/arch:"
    echo
    osc repos | while read repo arch; do
        count=$( get_buildrequires_lines "$repo" "$arch" | wc -l )
        printf "%-17s %-8s %d\n" "$repo" "$arch" "$count"
    done
    echo
}

find_all_matches () {
    osc repos "$project" | while read repo arch; do
        echo "Obtaining BuildRequires from $repo $arch ..." >&2
        get_buildrequires_lines "$repo" "$arch"
    done | sort -u
}

edit_spec () {
    sed -n -e '1,/BEGIN/p' $specfile
    echo "# Automatically generated by $0"
    echo "# on `date`"
    echo "# See http://en.opensuse.org/openSUSE:Packaging_Ruby#Compensating_for_lack_of_BuildRequires"
    cat
    sed -n -e '/END/,$p' $specfile
}

update_spec () {
    if edit_spec > $specfile.new; then
        mv $specfile.new $specfile
        echo "Updated spec: $specfile"
    else
        echo "Failed to generate new spec file contents; aborting." >&2
        exit 1
    fi
}

main "$@"
