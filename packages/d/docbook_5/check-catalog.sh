#!/bin/bash
# 
# Checks catalog URIs
#
# Dependencies:
#  * xmlstarlet
#
# Copyright 2023 SUSE Linux Products GmbH
# Author: Tom Schraitle 2023

ME=${0##*/}
BUILDROOT=""
ERRORS=()

function usage()
{
cat << EOF
$ME [--buildroot=BUILDROOT] CATALOG_FILE

Checks catalog URIs

Options
  --root             Used when building a package, points
                     to the build root

Arguments
  CATALOG_FILE       XML catalog file with catalog entries

Return codes
   0  everything fine. Celebrate! \o/
  10  catalog file doesn't exist
 100  some catalog error occured
EOF
}

function resolveuri() {
    local catalog="$1"
    local uri="$2"
    xmlcatalog "$catalog" "$uri" 2>/dev/null
}

function xpathfromcatalog() {
    local catalog="$1"
    local xpath="$2"
    local NS="urn:oasis:names:tc:entity:xmlns:xml:catalog"
    xml sel --text -N c=$NS -t -v "$xpath" "$catalog"
}


# -- CLI parsing
ARGS=$(getopt -o h -l help,buildroot: -n "$ME" -- "$@")
eval set -- "$ARGS"
while true; do
  case "$1" in
    --help|-h)
        usage
        exit 0
        ;;
    --buildroot)
       # Ensure that path ends with "/"
       BUILDROOT="${2%/}/"
       shift 2
       ;;
    --) shift ; break ;;
    *) exit_on_error "Wrong parameter: $1" ;;
  esac
done


CATALOG="$1"

if [ ! -e "$CATALOG" ]; then
    printf "Catalog file '$CATALOG' doesn't exist" >/dev/stderr
    exit 10
fi


declare -A TO_CHECK=(
    #-------------
    [5.0/nvdl]="docbook.nvdl"
    [5.0/rng]="docbook.rnc docbook.rng docbookxi.rnc docbookxi.rng"
    [5.0/sch]="docbook.sch"
    [5.0/xsd]="docbook.xsd xlink.xsd  xml.xsd"
    #-------------
    [5.1/nvdl]="docbook.nvdl"
    [5.1/rng]="assembly.rnc assembly.rng dbits.rnc dbits.rng docbook.rnc docbook.rng docbookxi.rnc docbookxi.rng"
    [5.1/sch]="assembly.sch dbits.sch docbook.sch  docbookxi.sch"
    #-------------
    [5.2/nvdl]="assembly.nvdl dbits.nvdl docbook.nvdl"
    [5.2/rng]="assembly.rnc assembly.rng assemblyxi.rnc assemblyxi.rng dbits.rnc dbits.rng dbitsxi.rnc dbitsxi.rng docbook.rnc docbook.rng docbookxi.rnc docbookxi.rng"
    [5.2/sch]="assembly.sch assemblyxi.sch dbits.sch docbook.sch  docbookxi.sch"
    #-------------
)

SYSTEMS=$(xpathfromcatalog "$CATALOG" \
                           "//c:system/@systemId")

# 
for uri in $SYSTEMS; do
    next=$(( "${#ERRORS[@]}" + 1 ))
    result=$(resolveuri "$CATALOG" "$uri")
    if [[ $? -ne 0 ]]; then
        result=""
        ERRORS[next]="$uri"
    else
        result="${BUILDROOT}${result#file://*}"

        if [[ $ret -ne 0 ]]; then
            result=""
            ERRORS[next]="$uri/$file"
        elif [[ ! -e $result ]]; then
            ERRORS[next]="$result"
        fi
    fi
    
done


REWRITESYSTEMS=$(xpathfromcatalog "$CATALOG" \
                                  "//c:rewriteSystem/@systemIdStartString")

for uri in $REWRITESYSTEMS; do
    result=$(resolveuri "$CATALOG" "$uri")
    if [[ $? -ne 0 ]]; then
        result=""
        next=$(( ${#ERRORS[@]} + 1 ))
        ERRORS[next]="$uri"
    fi
    # Check if we have after the release a format
    if [[ $uri =~ ((5\.[0-9])/([^/]+))(/)? ]]; then
        # If we have a match, we have:
        # ${BASH_REMATCH[0]} => the complete match
        # ${BASH_REMATCH[1]} => DocBook version + Format, e.g "5.0/rng"
        # ${BASH_REMATCH[2]} => DocBook version only
        # ${BASH_REMATCH[3]} => Format only
        DBFORMAT=${BASH_REMATCH[1]}
        FORMAT=${BASH_REMATCH[3]}
        FILES="${TO_CHECK[$DBFORMAT]}"

        # Remove "/" at end, if needed:
        uri="${uri%/}"
        # echo "To check $DBFORMAT: $FILES"
        for file in $FILES; do
            echo -en "Checking $uri/$file... =>"
            next=$(( "$len" + 1 ))
            result=$(resolveuri "$CATALOG" "${uri}/$file")
            ret=$?
            result="${BUILDROOT}${result#file://*}"
            # We check the return value and _not_ the result string
            if [[ $ret -ne 0 ]]; then
                result=""
                ERRORS[next]="$uri/$file"
                echo -en " not resolvable\n"
            elif [[ ! -e $result ]]; then
                ERRORS[next]="$result"
                echo -en " doesn't exist\n"
            else
                echo -en " ok\n"
            fi
        done
    fi
done

echo "-----------------------------"
# make them unique:
ERRORS=($(for err in "${ERRORS[@]}"; do echo "${err}"; done | sort -u))
echo "Found ${#ERRORS[@]} errors".

if [ ${#ERRORS[@]} -ne 0 ]; then
    for elem in "${!ERRORS[@]}"; do
        echo "${elem}: ${ERRORS[${elem}]}"
    done
    exit 100
fi
exit 0