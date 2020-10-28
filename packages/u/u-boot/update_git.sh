#!/bin/bash
#
# Instead of a quilt workflow, we use a git tree that contains
# all the commits on top of a stable tarball.
#
# When updating this package, just either update the git tree
# below (use rebase!) or change the tree path and use your own
#
# That way we can easily rebase against the next stable release
# when it comes.

set -e

GIT_TREE=git://github.com/openSUSE/u-boot.git
GIT_LOCAL_TREE=~/git/u-boot-opensuse
GIT_BRANCH=tumbleweed-2020.10
GIT_UPSTREAM_TAG=v2020.10
GIT_DIR=/dev/shm/u-boot-factory-git-dir
CMP_DIR=/dev/shm/u-boot-factory-cmp-dir

rm -rf $GIT_DIR
rm -rf $CMP_DIR

if [ -d "$GIT_LOCAL_TREE" ] || [ -L "$GIT_LOCAL_TREE" ]; then
    echo "Processing $GIT_BRANCH branch of local git tree, using tag:" \
         "$GIT_UPSTREAM_TAG"
    if ! (cd $GIT_LOCAL_TREE && git show-branch $GIT_BRANCH &>/dev/null); then
        echo "Error: Branch $GIT_BRANCH not found - please create a remote" \
             "tracking branch of origin/$GIT_BRANCH"
        exit
    fi
    git clone -ls $GIT_LOCAL_TREE $GIT_DIR -b $GIT_BRANCH
    if ! (cd $GIT_LOCAL_TREE && git remote show upstream &>/dev/null); then
        echo "Remote for upstream git tree not found. Next time add remote" \
             "named upstream for git://git.denx.de/u-boot.git and update"
        (cd $GIT_DIR && git remote add upstream git://git.denx.de/u-boot.git)
        (cd $GIT_DIR && git remote update)
   fi
else
    echo "Processing $GIT_BRANCH branch of remote git tree, using tag:" \
         "$GIT_UPSTREAM_TAG"
    echo "(For much faster processing, consider establishing a local git tree" \
         "at $GIT_LOCAL_TREE)"
    git clone $GIT_TREE $GIT_DIR -b $GIT_BRANCH
    (cd $GIT_DIR && git remote add upstream git://git.denx.de/u-boot.git)
    (cd $GIT_DIR && git remote update)
fi
(cd $GIT_DIR && git format-patch -N $GIT_UPSTREAM_TAG --suffix= -o $CMP_DIR >/dev/null)
UBOOT_VERSION=$(egrep '^VERSION = ' $GIT_DIR/Makefile | cut -d ' ' -f 3)
UBOOT_PATCHLEVEL=$(egrep '^PATCHLEVEL = ' $GIT_DIR/Makefile | cut -d ' ' -f 3)
UBOOT_SUBLEVEL=$(egrep '^SUBLEVEL = ' $GIT_DIR/Makefile | cut -d ' ' -f 3)
UBOOT_EXTRAVERSION=$(egrep '^EXTRAVERSION = ' $GIT_DIR/Makefile | cut -d ' ' -f 3)
UBOOT_VERSION="${UBOOT_VERSION}.${UBOOT_PATCHLEVEL}"
if [ -n "${UBOOT_SUBLEVEL}" ]; then
    UBOOT_VERSION="${UBOOT_VERSION}.${UBOOT_SUBLEVEL}"
fi
UBOOT_VERSION="${UBOOT_VERSION}${UBOOT_EXTRAVERSION}"
echo "U-Boot version: $UBOOT_VERSION"

rm -rf $GIT_DIR

(
    CHANGED_COUNT=0
    UNCHANGED_COUNT=0
    DELETED_COUNT=0
    ADDED_COUNT=0

    shopt -s nullglob

# Process patches to eliminate useless differences: limit file names to 40 chars
# before extension and remove git signature. ('32' below gets us past dir prefix)
    for i in $CMP_DIR/*; do
        # format-patch may append a signature, which per default contains the git version
        # wipe everything starting from the signature tag
        sed '/^-- $/Q' $i > $CMP_DIR/${i:32:40}.patch
        rm $i
    done

    for i in 0???-*.patch; do
        if [ -e $CMP_DIR/$i ]; then
            if cmp -s $CMP_DIR/$i $i; then
                rm $CMP_DIR/$i
                let UNCHANGED_COUNT+=1
            else
                mv $CMP_DIR/$i .
                let CHANGED_COUNT+=1
            fi
        else
            osc rm --force $i
            let DELETED_COUNT+=1
            echo "  ${i##*/}" >> u-boot.changes.deleted
        fi
    done

    for i in $CMP_DIR/*; do
        mv $i .
        osc add ${i##*/}
        let ADDED_COUNT+=1
        echo "  ${i##*/}" >> u-boot.changes.added
    done

    # Factory requires all deleted and added patches to be mentioned
    if [ -e u-boot.changes.deleted ] || [ -e u-boot.changes.added ]; then
        echo "Patch queue updated from ${GIT_TREE} ${GIT_BRANCH}" > u-boot.changes.proposed
    fi
    if [ -e u-boot.changes.deleted ]; then
        echo "* Patches dropped:" >> u-boot.changes.proposed
        cat u-boot.changes.deleted  >> u-boot.changes.proposed
    fi
    if [ -e u-boot.changes.added ]; then
        echo "* Patches added:" >> u-boot.changes.proposed
        cat u-boot.changes.added  >> u-boot.changes.proposed
    fi
    if [ -e u-boot.changes.proposed ]; then
        osc vc --file=u-boot.changes.proposed u-boot
        rm -f u-boot.changes.proposed
    fi
    if [ -e u-boot.changes.deleted ]; then
        rm -f u-boot.changes.deleted
    fi
    if [ -e u-boot.changes.added ]; then
        rm -f u-boot.changes.added
    fi
    echo "git patch summary"
    echo "  unchanged: $UNCHANGED_COUNT"
    echo "    changed: $CHANGED_COUNT"
    echo "    deleted: $DELETED_COUNT"
    echo "      added: $ADDED_COUNT"
)

rm -rf $CMP_DIR

echo "Updating patch list"
# Handle patch list automatically in spec file
patch_list=`ls 0*.patch`
# Remove current patches from spec file
sed -i '/# Patches: start/,/# Patches: end/  {//!d}' u-boot.spec
# Add patches to spec file
for file in $patch_list; do
  i=`echo $file | awk -F'[-.]' '{print $1}'`
  sed -i "/# Patches: end/i Patch$i:      $file" u-boot.spec
done


osc service localrun format_spec_file

echo "Please update version in u-boot.spec, if needed"
