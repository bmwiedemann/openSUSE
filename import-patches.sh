#!/bin/sh

# Invoke as:
# $ ./import-patches.sh [ --dry-run ] <n> <dir>/00*.patch

usage ()
{
    echo "./import-patches.sh [ --dry-run ] <n> <files>+"
}

dryrun=false
case "$1" in
    -dryrun|-dry-run|--dryrun|--dry-run)
	dryrun=true
	shift
	;;
esac

n="$1"
shift

case $n in
    "")
	echo "Missing <n> argument"
	usage
	exit 1
	;;
    [0-9][0-9]*)
	;;
    *) 
	echo "Need numeric <n> argument"
	usage
	exit 1
	;;
esac

if [ "$n" = "" ]; then
    echo "Missing <n> argument"
    usage
    exit 1
fi

files="$*"

rm -Rf tmp.patches
mkdir tmp.patches

tmp=
for f in $files; do
    dir=$(dirname "$f")
    f=$(basename "$f")
    orig_f="$f"

    # Remove numeric prefix.
    f=$(echo "$f" \
	    | sed 's/^[0-9]*-//')

    # To lowercase.
    f=$(echo "$f" \
	    | tr '[:upper:]' '[:lower:]')

    # Fix patch.patch.
    f=$(echo "$f" \
	     | sed 's/\.patch\.patch/.patch/')
    
    # Copy.
    cp "$dir"/"$orig_f" tmp.patches/"$f"

    # Filter out ChangeLog entries.
    filterdiff -x "*/ChangeLog" tmp.patches/"$f" > tmp.patches/tmp."$f"
    mv tmp.patches/tmp."$f" tmp.patches/"$f"
    
    tmp="$tmp $f"
done
files="$tmp"

i=$n
for f in $files; do
    printf "Patch%-11s%s\n" "$i:" "$f"

    i=$((i + 1))
done

i=$n
for f in $files; do
    echo "%patch$i -p1"

    i=$((i + 1))
done

if $dryrun; then
    exit
fi

for f in $files; do
    mv tmp.patches/"$f" .
    osc add "$f"
done

rmdir tmp.patches
