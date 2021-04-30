#!/bin/bash

set -e

# update_git.sh: script to manage package maintenance using a git-based
# workflow. Commands are as follows:
#   git2pkg (update package spec file and patches from git)
#   pkg2git (update git (frombundle branch) from the package "bundleofbundles")
#   refresh (refresh spec file from spec file template and "bundlofbundles")
#   ci      (check-in to obs, avoiding some spec file formatting issues)
#   initbundle (Update/Create bundle only)
#
#   (default is git2pkg)

#==============================================================================

clean_up_temp_dirs()
{
echo "Cleaning temporary files before exit"
rm -rf $GIT_DIR
rm -rf $CMP_DIR
rm -rf $BUN_DIR
exit
}

# handle signals gracefully by cleaning the temporary data used before exit
trap clean_up_temp_dirs EXIT

#==============================================================================

check_requirements() {
    RC=0
    if [[ ! -e ./config.sh ]]; then
        echo "ERROR: Missing config.sh configuration script"
        RC=1
    fi
    if [[ ! $(rpm -q git-core) ]]; then
        echo "ERROR: Missing dependency: git-core"
        RC=1
    fi
    if [[ ! $(rpm -q osc) ]]; then
        echo "ERROR: Missing dependency: osc package"
        RC=1
    fi
    if [[ ! $(rpm -q obs-service-format_spec_file) ]]; then
        echo "ERROR: Missing dependency: obs-service-format_spec_file package"
        RC=1
    fi
    ONE_GIG_IN_1K_BLOCKS=1048576
    AVAIL=$(df --output=avail /dev/shm | tail -1)
    if [[ $AVAIL -lt $ONE_GIG_IN_1K_BLOCKS ]]; then
        echo "ERROR: Please provide at least 1GB available space in /dev/shm"
        RC=1
    fi
    if [[ "$RC" = "1" ]]; then
        echo "Script requires the above resources. Please resolve to use this workflow"
        exit
    fi
}

#==============================================================================

usage() {
echo "Usage:"
echo "bash ./git_update.sh <command>"
echo "description: package maintenance using a git-based workflow. Commands:"
echo "  git2pkg (update package spec file and patches from git. Is default)"
echo "  pkg2git (update git (frombundle branch) from the package "bundleofbundles")"
echo "  refresh (refresh spec file from spec file template and "bundlofbundles")"
echo "  ci       (check-in to build service, avoiding some spec file formatting issues)"
echo "  initbundle (Update/Create bundle only)"
echo "(See script for details on doing 'LATEST' workflow)"
check_requirements
}

#==============================================================================

source ./config.sh

# If you're using LATEST, we assume you are an expert so no basic help provided
if [ "$GIT_UPSTREAM_COMMIT_ISH" != "LATEST" ]; then
    if [ "$1" = "" ]; then
        set -- git2pkg
    else
        case $1 in
            help | -H | -h )
                usage
                exit
                ;;
                initbundle | git2pkg |  pkg2git | refresh | ci)
                ;;
            * )
                echo "Unknown command"
                usage
                exit
            ;;
        esac
    fi
fi

check_requirements

# As an aid to bypassing issues with our multibuild package and obs (see code
# below following the osc localrun of osc service localrun format_spec_file),
# provide an automated way to checkin without needing to type so much
if [ "$1" = "ci" ]; then
    osc ci -f -n --noservice
    exit
fi


# TODO: Here we should validate the variables that should be set in config.sh

REPO_COUNT=${#PATCH_PATH_MAP[@]}
if [[ "$REPO_COUNT" != "${#LOCAL_REPO_MAP[@]}" ]]; then
    echo "PATCH_PATH_MAP and LOCAL_REPO_MAP array sizes do not agree - please fix"
    exit
fi

check_requirements

# Zero based numbering, so we subtract 1 here:
if (( (REPO_COUNT * PATCH_RANGE) - 1 > 9999 )); then
    if [[ "$OVERRIDE_FIVE_DIGIT_NUMBERING" = "1" ]]; then
        FIVE_DIGIT_POTENTIAL=0
    else
        FIVE_DIGIT_POTENTIAL=1
    fi
else
    FIVE_DIGIT_POTENTIAL=0
fi

declare -A COMMIT_IDS_BY_SUBMODULE_PATH

# Get version info from the packages' tarball - decode and do some checks
BASE_RE="qemu-[[:digit:]]+(\.[[:digit:]]+){2,3}(-rc[[:digit:]])?"
EXTRA_RE="\+git\.[[:digit:]]+\.([[:xdigit:]]+)"
SUFFIX_RE="\.tar\.xz"
SIG_SUFFIX_RE="\.tar\.xz\.sig"
QEMU_TARBALL=($(find -maxdepth 1 -type f -regextype posix-extended -regex \
    "\./$BASE_RE($EXTRA_RE)?$SUFFIX_RE" -printf "%f "))
QEMU_TARBALL_SIG=($(find -maxdepth 1 -type f -regextype posix-extended -regex \
    "\./$BASE_RE($EXTRA_RE)?$SIG_SUFFIX_RE" -printf "%f "))

if [ ${#QEMU_TARBALL[@]} -gt 1 ]; then
    echo "Multiple qemu tarballs detected. Please clean up"
    exit
fi
if [ ${#QEMU_TARBALL_SIG[@]} -gt 1 ]; then
    echo "Multiple qemu tarballs signature files detected. Please clean up"
    exit
fi
OLD_SOURCE_VERSION_AND_EXTRA=$(echo $QEMU_TARBALL 2>/dev/null | head --bytes=-8\
    | cut --bytes=6-)
VERSION_EXTRA=$(echo $OLD_SOURCE_VERSION_AND_EXTRA|awk -F+ '{if ($2) print \
    "+"$2}')
if [ "$OLD_SOURCE_VERSION_AND_EXTRA" = "" ]; then
    echo "ERROR: No tarball found!"
    exit
fi

#==============================================================================

initbundle() {
# The bundle tarball has git bundles stored in a directory structure which mimics the
# submodule locations in the containing git repo. Also at that same dir level
# is a file named repo which contains the one line git repo url (with git:// or
# http(s) prefix). The bundles are named as follows:
# "{path/}{git_sha}.{bundle}", where {path/} isn't present for
# the top (qemu) bundle (ie it's for submodules).

find $GIT_DIR -mindepth 1 -delete
find $BUN_DIR -mindepth 1 -delete
if [[ -e ${LOCAL_REPO_MAP[$i]}/.git/shallow ]]; then
    if [[ -e bundles.tar.xz ]]; then
        tar --extract --xz -f bundles.tar.xz -C $BUN_DIR .
    else
        echo "ERROR: Superproject at ${LOCAL_REPO_MAP[$i]} is shallow (so we assume submodules aren't"
        echo "recursively checked out), and there is not an existing bundle-of-bundles file, so we cannot"
        echo "correctly initialize the packages bundle-of-bundles. Please fully initilize git superproject"
        echo "before doing initbundle"
        exit
    fi
else
#TODO: Is there a better way to do this (we don't want the old bundle commit id's relied on HERE for LATEST)
    if [[ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]]; then
        rm bundles.tar.xz
     fi
    if [[ -e bundles.tar.xz ]]; then
        tar --extract --xz -f bundles.tar.xz -C $BUN_DIR .
    else
        SUBMODULE_COMMIT_IDS=($(git -C ${LOCAL_REPO_MAP[0]} submodule status --recursive| cut -c 2- | awk '{print $1}'))
        SUBMODULE_DIRS=($(git -C ${LOCAL_REPO_MAP[0]} submodule status --recursive| cut -c 2- |awk '{print $2}'))
        SUBMODULE_COUNT=${#SUBMODULE_COMMIT_IDS[@]}
        # TODO: do this with simply math - ie: use (( ... ))
        if [[ "$REPO_COUNT" != "$(expr $SUBMODULE_COUNT + 1)" ]]; then
            echo "ERROR: submodule count doesn't match what's in config.sh"
            exit
        fi
        for (( i=0; i <$SUBMODULE_COUNT; i++ )); do
            mkdir -p $BUN_DIR/${SUBMODULE_DIRS[$i]}
            touch $BUN_DIR/${SUBMODULE_DIRS[$i]}/${SUBMODULE_COMMIT_IDS[$i]}.id
        done
        if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
            GIT_UPSTREAM_COMMIT=$NEW_COMMIT_ISH_FULL
        else
        # TODO: make this smarter, or change something - works for tag, but not normal commit?
            GIT_UPSTREAM_COMMIT=$(git -C ${LOCAL_REPO_MAP[0]} show-ref -d $GIT_UPSTREAM_COMMIT_ISH|grep -F "^{}"|awk '{print $1}')
	    if [[ "$GIT_UPSTREAM_COMMIT" = "" ]]; then
               GIT_UPSTREAM_COMMIT=$(git -C ${LOCAL_REPO_MAP[0]} show-ref -d $GIT_UPSTREAM_COMMIT_ISH||awk '{print $1}')
            fi
	    if [[ "$GIT_UPSTREAM_COMMIT" = "" ]]; then
                echo "ERROR: Failed to get commit id for $GIT_UPSTREAM_COMMIT_ISH"
		exit
            fi
        fi
        touch $BUN_DIR/$GIT_UPSTREAM_COMMIT.id
    fi
fi

# Now go through all the submodule local repos that are present with a $GIT_BRANCH and create a bundle file for the patches found
for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
        SUBDIR=${PATCH_PATH_MAP[$i]}
        GITREPO_COMMIT_ISH=($BUN_DIR/$SUBDIR*.id)
        if [[ $GITREPO_COMMIT_ISH  =~ .*(.{40})[.]id ]]; then
            GITREPO_COMMIT_ISH=${BASH_REMATCH[1]}
            echo "Using $GITREPO_COMMIT_ISH"
            PATCH_RANGE_INDEX=$i
            mkdir -p $GIT_DIR/$SUBDIR
            git -C $GIT_DIR/$SUBDIR -c init.defaultBranch=$GIT_BRANCH init
            git -C $GIT_DIR/$SUBDIR remote add origin file://$(readlink -f \
                ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
            if [[ $(git -C $GIT_DIR/$SUBDIR ls-remote --heads origin $GIT_BRANCH) ]]; then
                git -C $GIT_DIR/$SUBDIR fetch --update-shallow origin $GIT_BRANCH
                if [[ $(git -C $GIT_DIR/$SUBDIR rev-list $GITREPO_COMMIT_ISH..FETCH_HEAD) ]]; then
                    git -C $GIT_DIR/$SUBDIR bundle create $BUN_DIR/$SUBDIR$GITREPO_COMMIT_ISH.bundle $GITREPO_COMMIT_ISH..FETCH_HEAD
#TODO: post-process repo info to avoid un-needed diffs (eg git vs https)
                    git -C $(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]}) remote get-url origin >$BUN_DIR/$SUBDIR/repo
                fi
            fi
        fi
    fi
done
# parameters chosen to allow bundle tarball exact reproducibility
tar --format gnu --xz \
    --sort=name \
    --numeric-owner \
    --owner=0 \
    --group=0 \
    --mtime="@$(date -r qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz +%s)" \
    --create \
    -f bundles.tar.xz -C $BUN_DIR .
    find $BUN_DIR -mindepth 1 -delete
    find $GIT_DIR -mindepth 1 -delete
}

#==============================================================================

bundle2local() {
	find $BUN_DIR -mindepth 1 -delete
tar xJf bundles.tar.xz -C $BUN_DIR
ID_FILES=$(find $BUN_DIR -printf "%P\n"|grep "id$")

for entry in ${ID_FILES[@]}; do
    if [[ $entry =~ ^(.*)[/]*([a-f0-9]{40})[.]id$ ]]; then
        SUBDIR=${BASH_REMATCH[1]}
        GITREPO_COMMIT_ISH=${BASH_REMATCH[2]}
    else
        echo "ERROR! BAD BUNDLE CONTENT!"
        exit
    fi
    for (( i=0; i <$REPO_COUNT; i++ )); do
        if [[ "$SUBDIR" = "${PATCH_PATH_MAP[$i]}" ]]; then
            PATCH_RANGE_INDEX=$i
            break
        fi
    done
    if [[ "$i" = "REPO_COUNT" ]]; then
        echo "ERROR! BUNDLE SUBPROJECT $SUBDIR NOT MENTIONED IN config.sh! Fix!"
        exit
    fi

    LOCAL_REPO=$(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
    if [ -e $LOCAL_REPO ]; then
        git -C $LOCAL_REPO remote remove bundlerepo || true
        if [ -e $BUN_DIR/$SUBDIR/$GITREPO_COMMIT_ISH.bundle ]; then
            git -C $LOCAL_REPO remote add bundlerepo $BUN_DIR/$SUBDIR/$GITREPO_COMMIT_ISH.bundle
            git -C $LOCAL_REPO fetch bundlerepo FETCH_HEAD
            git -C $LOCAL_REPO branch -f frombundle FETCH_HEAD
            git -C $LOCAL_REPO remote remove bundlerepo
        else
            # It's problematic to leave "stale" frombundle branches around
            git -C $LOCAL_REPO branch -D frombundle || true
        fi
    else
        if [ -e $BUN_DIR/$SUBDIR/$GITREPO_COMMIT_ISH.bundle ]; then
            # TODO: We should be able to handle this case with some more coding, but for now...
            echo "No local repo $LOCAL_REPO available to process git bundle!"
            if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
                echo "The above is FATAL when doing LATEST processing - please fix"
                exit
            else
                echo "Moving on..."
            fi
        fi
    fi
done
find $BUN_DIR -mindepth 1 -delete
}

#==============================================================================

redo_tarball_and_rebase_patches() {
	find $GIT_DIR -mindepth 1 -delete

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CREATE TARBALL, USING FRESH REPO - WE COULD RELY MORE ON LOCAL IF WE WERE MORE CAREFUL
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# TODO: WHAT IS THIS NEXT LINE EVEN DOING FOR US?? (OK, it's initing a repo, what do we rely on there?)
# Here, the branch doesn't really matter, and we're not relying on a master branch - we're just making sure we are grabbing latest from upstream
# (while using a clone of "something close" as a way to quickly get most objects available as quickly as possible)
git clone -ls ${LOCAL_REPO_MAP[0]} -b $GIT_BRANCH --single-branch $GIT_DIR &>/dev/null
echo "Please wait..."
(cd $GIT_DIR && git remote add upstream \
$UPSTREAM_GIT_REPO &>/dev/null)
(cd $GIT_DIR && git remote update upstream &>/dev/null)
(cd $GIT_DIR && git reset --hard --recurse-submodules $NEW_COMMIT_ISH &>/dev/null)
# As an alternative, we could add a --recurse-submodules to the checkout instead here as well, right?
#UPSTREAM DOESNT DO THIS (time takes 17 minutes!):
#        (cd $GIT_DIR && git submodule update --init --recursive &>/dev/null)
#INSTEAD THESE NEXT TWO LINES ARE WHAT IS DONE (these take 9 minutes and 3 minutes respectively):
(cd $GIT_DIR && git submodule update --init &>/dev/null)
(cd $GIT_DIR/roms/edk2 && git submodule update --init &>/dev/null)
VERSION_EXTRA=+git.$NOW_SECONDS.$NEW_COMMIT_ISH
if (cd ${LOCAL_REPO_MAP[0]} && git describe --exact-match $NEW_COMMIT_ISH \
    &>/dev/null); then
    if [ "$X" = "50" ]; then
        echo "Ignoring non-standard tag"
    else
# there is no VERSION_EXTRA
        VERSION_EXTRA=
    fi
fi
(cd $GIT_DIR/roms/seabios && git describe --tags --long --dirty > \
    .version)
(cd $GIT_DIR/roms/skiboot && ./make_version.sh > .version)
echo "Almost there..."
tar --exclude=.git --transform "s,$GIT_DIR,qemu-$SOURCE_VERSION," \
    -Pcf qemu-$SOURCE_VERSION$VERSION_EXTRA.tar $GIT_DIR
osc rm --force qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz &>/dev/null ||\
    true
osc rm --force qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz.sig \
    &>/dev/null || true
unset QEMU_TARBALL_SIG
xz -T 0 qemu-$SOURCE_VERSION$VERSION_EXTRA.tar
osc add qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GET THE SUBMODULE COMMIT ID'S FROM THIS NEWLY MINTED QEMU CHECKOUT. WE'LL USE THAT WHEN WE REBASE OUR PATCHES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !! We (perhaps temporarily) do MORE recursive submodules, since we are tracking ALL in these scripts, while upstream doesn't include all in tarball currently 
# !!! THIS IS AT LEAST PARTLY REDUNDANT WITH THE update --init DONE ABOUT 30 LINES AGO
(cd $GIT_DIR && git submodule update --init --recursive &>/dev/null)
SUBMODULE_COMMIT_IDS=($(git -C $GIT_DIR submodule status --recursive|awk '{print $1}'))
SUBMODULE_DIRS=($(git -C $GIT_DIR submodule status --recursive|awk '{print $2}'))
SUBMODULE_COUNT=${#SUBMODULE_COMMIT_IDS[@]}
# TODO: do this with simply math - ie: use (( ... ))
if [[ "$REPO_COUNT" != "$(expr $SUBMODULE_COUNT + 1)" ]]; then
    echo "ERROR: submodule count doesn't match the REPO_COUNT variable in config.sh file!"
    exit
fi
# We have the submodule commits, but not in the PATCH ORDER which our config.sh has (see $PATCH_PATH_MAP)
for (( i=0; i <$REPO_COUNT-1; i++ )); do
    COMMIT_IDS_BY_SUBMODULE_PATH[${SUBMODULE_DIRS[$i]}/]=${SUBMODULE_COMMIT_IDS[$i]}
done
COMMIT_IDS_BY_SUBMODULE_PATH[SUPERPROJECT]=$NEW_COMMIT_ISH_FULL

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOVE BUNDLE COMMITS OVER TO LOCAL frombundle BRANCH
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

bundle2local 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# REBASE $GIT_BRANCH's on latest COMMIT_IDS_FROM_SUBMODULE_PATH, after reseting branch to frombundle branch
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
        if $(git -C ${LOCAL_REPO_MAP[$i]} branch | grep -F "frombundle" >/dev/null); then
            SUBDIR=${PATCH_PATH_MAP[$i]}
            git -C ${LOCAL_REPO_MAP[$i]} checkout -B $GIT_BRANCH frombundle
            if [[ "$SUBDIR" = "" ]]; then
                SUBDIR=SUPERPROJECT
            fi
            if ! $(git -C ${LOCAL_REPO_MAP[$i]} rebase ${COMMIT_IDS_BY_SUBMODULE_PATH[$SUBDIR]} >/dev/null); then
                echo "Rebase of ${LOCAL_REPO_MAP[$i]}, branch $GIT_BRANCH needs manual help"
                REBASE_FAILS="${LOCAL_REPO_MAP[$i]} $REBASE_FAILS"
            fi
        fi
    fi
done
}

#==============================================================================

bundle2spec() {
rm -f checkpatch.log
rm -f checkthese
rm -rf checkdir
rm -rf savedir
find $GIT_DIR -mindepth 1 -delete
find $CMP_DIR -mindepth 1 -delete
find $BUN_DIR -mindepth 1 -delete
mkdir savedir

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Handle case of casual user missing local repos.
# To support this, we must grok the spec file's
# list of patches for "reuse" in case we don't
# have local repo to use for extracting bundle
# contents. (here we assume the existing bundle
# would then still correspond to the patches
# listed in spec file for that repo)
# WARNING:
# The following groking expects the patch section
# to be as this script lays it out, not modified!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
declare -a PATCHES_BY_SUBMODULE_PATH
IN_PATCH_SECTION=0
INDEX=$REPO_COUNT # "invalid" since zero based index of objects < one based count of objects
while IFS= read -r line; do
    if [[ "$line" = "# Patches applied in base project:" ]]; then
        IN_PATCH_SECTION=1
        INDEX=0 # base project is 0 by definition
        continue
    fi
    if [[ "$line" =~ ^..Patches.applied.in.(.*)/:$ ]]; then
        REPO="${BASH_REMATCH[1]}/"
        IN_PATCH_SECTION=1
        for (( i=0; i <$REPO_COUNT; i++ )); do
            if [[ "$REPO" = "${PATCH_PATH_MAP[$i]}" ]]; then
                if [[ "$INDEX" != "$REPO_COUNT" ]]; then
                    PATCHES_BY_SUBMODULE_PATH[$INDEX]=$ACCUMULATED_PATCHES
                    unset ACCUMULATED_PATCHES
                fi
                INDEX=$i
                break
            fi
        done
        if [[ "$INDEX" = "$REPO_COUNT" ]]; then
            echo "ERROR: Failure groking spec file for patches!"
            exit
        fi
        continue
    fi
    if [[ "$IN_PATCH_SECTION" = "0" ]]; then
        continue
    fi
    if [[ "$line" =~ ^$ ]]; then
        PATCHES_BY_SUBMODULE_PATH[$INDEX]=$ACCUMULATED_PATCHES
        break;
    fi
    if [[ "$line" =~ ^Patch[0-9]*:[\ ]*(.*)$ ]]; then
        PATCH="${BASH_REMATCH[1]}"
        #echo "Patch is $PATCH"
        ACCUMULATED_PATCHES="$ACCUMULATED_PATCHES $PATCH"
        continue
    fi
    echo "ERROR: Failure groking spec file for patches!"
    exit
done < $PKG.spec

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CONVERT BUNDLES INTO COMMITS AND FILL SPEC FILE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tar xJf bundles.tar.xz -C $BUN_DIR
BUNDLE_FILES=$(find $BUN_DIR -printf "%P\n"|grep "bundle$")

for entry in ${BUNDLE_FILES[@]}; do
    if [[ $entry =~ ^(.*)[/]*([a-f0-9]{40})[.]bundle$ ]]; then
        SUBDIR=${BASH_REMATCH[1]}
        GITREPO_COMMIT_ISH=${BASH_REMATCH[2]}
    else
        echo "ERROR! BAD BUNDLE CONTENT!"
        exit
    fi
    for (( i=0; i <$REPO_COUNT; i++ )); do
        if [[ "$SUBDIR" = "${PATCH_PATH_MAP[$i]}" ]]; then
            PATCH_RANGE_INDEX=$i
            break
        fi
    done

    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]}) ]]; then
        mkdir -p $GIT_DIR/$SUBDIR
        git -C $GIT_DIR/$SUBDIR -c init.defaultBranch=$GIT_BRANCH init
        git -C $GIT_DIR/$SUBDIR remote add origin file://$(readlink -f \
            ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
        # This tag reference, was added to resolve $GITREPO_COMMIT_ISH, which is tag as commit-id
        # Since origin may be shallow, we need to use the --update-shallow option
        git -C $GIT_DIR/$SUBDIR fetch --update-shallow origin $GIT_BRANCH
        git -C $GIT_DIR/$SUBDIR remote add bundle $BUN_DIR/$entry 
        git -C $GIT_DIR/$SUBDIR fetch bundle FETCH_HEAD
        git -C $GIT_DIR/$SUBDIR format-patch -N --suffix= --no-renames -o $CMP_DIR -k --stat=72 \
            --indent-heuristic --zero-commit --no-signature --full-index \
            --src-prefix=a/$SUBDIR --dst-prefix=b/$SUBDIR \
            --start-number=$(expr $PATCH_RANGE_INDEX \* $PATCH_RANGE) \
            $GITREPO_COMMIT_ISH..FETCH_HEAD > /dev/null
        PATCHES_BY_SUBMODULE_PATH[$PATCH_RANGE_INDEX]=""
    else
# TODO: This doesn't handle numbered patches yet
        COUNTER=$(expr $PATCH_RANGE_INDEX \* $PATCH_RANGE)
        for patchname in ${PATCHES_BY_SUBMODULE_PATH[$PATCH_RANGE_INDEX]}; do
            VALUE="0000"$COUNTER
            if [ "$FIVE_DIGIT_POTENTIAL" = "1" ]; then
                PREFIX=$(echo $VALUE|tail -c 6)
            else
                PREFIX=$(echo $VALUE|tail -c 5)
            fi
            if [[ "$NUMBERED_PATCHES" = "0" ]]; then
                cp $patchname savedir/$PREFIX-$patchname
            else
                cp $patchname savedir/$patchname
            fi
            let COUNTER+=1
        done
    fi
done

find $GIT_DIR -mindepth 1 -delete
find $BUN_DIR -mindepth 1 -delete

(
    CHANGED_COUNT=0
    UNCHANGED_COUNT=0
    DELETED_COUNT=0
    ADDED_COUNT=0
    TOTAL_COUNT=0

    shopt -s nullglob

    for i in $CMP_DIR/*; do
# index line isn't consistent, so cut full index to normal line length
        sed -E -i 's/(^index [a-f0-9]{28})[a-f0-9]{12}([.][.][a-f0-9]{28})[a-f0-9]{12}( [0-9]{6}$)/\1\2\3/' $i
        BASENAME=$(basename $i)
        if [ "$FIVE_DIGIT_POTENTIAL" = "1" ]; then
            if [[ "$BASENAME" =~ ^[[:digit:]]{5}.* ]]; then
                :
            else
                BASENAME=0"$BASENAME"
            fi
        fi
        if [[ "$NUMBERED_PATCHES" = "0" ]]; then
            KEEP_COUNT=40+4+$FIVE_DIGIT_POTENTIAL+1
        else
            KEEP_COUNT=40
        fi
        tail -n +2 $i > $CMP_DIR/"${BASENAME:0:$KEEP_COUNT}".patch
        rm $i
    done
    cp savedir/* $CMP_DIR/ || true
    rm -rf savedir
# 4 digit xxxx-name used in the dest (remember that if 5 digit potential, then if not now 5 digit, add a 0 in front)

    if [[ "$NUMBERED_PATCHES" = "0" ]]; then
        for i in [0-9][0-9][0-9][0-9]*-*.patch; do
            osc rm --force "$i"
        done
# make sure that w/out the numbered prefixes, the patchnames are all unique
        mkdir checkdir
        for i in $CMP_DIR/*; do
            BASENAME=$(basename $i)
            FINALNAME="${BASENAME:4+$FIVE_DIGIT_POTENTIAL+1:40+1+5}"
            if [[ -e checkdir/"$FINALNAME" ]]; then
                echo "ERROR! Patch name $FINALNAME is not unique! Please modify patch subject to achieve uniqueness"
                exit 1
            fi
            cp $i checkdir/"$FINALNAME"
        done
        CHECK_DIR=checkdir
        cp $CMP_DIR/*.patch .
    else
        CHECK_DIR=$CMP_DIR
    fi
    if [ "$FIVE_DIGIT_POTENTIAL" = "0" ]; then
        CHECK_PREFIX="0"
        NUMBERED_PATCH_RE="^[[:digit:]]{4}-.*[.]patch$"
    else
        CHECK_PREFIX="00"
        NUMBERED_PATCH_RE="^[[:digit:]]{5}-.*[.]patch$"
    fi
    for i in $CHECK_DIR/*; do
        BASENAME=$(basename $i)
        if [ -e "$BASENAME" ]; then
            if cmp -s "$i" "$BASENAME"; then
                touch --reference="$BASENAME" "$i"
                rm "$BASENAME"
                let UNCHANGED_COUNT+=1
            else
                if [ "${BASENAME:0:1+$FIVE_DIGIT_POTENTIAL}" = "$CHECK_PREFIX" ]; then
                    echo "$BASENAME" >> checkthese
                fi
                rm $BASENAME
                let CHANGED_COUNT+=1
                let TOTAL_COUNT+=1
            fi
        else
            echo "  $BASENAME" >> qemu.changes.added
            if [ "${BASENAME:0:1+$FIVE_DIGIT_POTENTIAL}" = "$CHECK_PREFIX" ]; then
                echo "$BASENAME" >> checkthese
            fi
            let ADDED_COUNT+=1
            let TOTAL_COUNT+=1
        fi
    done
    for i in *.patch; do
        if [[ "$i" =~ $NUMBERED_PATCH_RE ]]; then
            if [[ "$NUMBERED_PATCHES" = "1" ]]; then
                osc rm --force $i
                echo "  $i" >> qemu.changes.deleted
                let DELETED_COUNT+=1
                let TOTAL_COUNT+=1
            fi
        else
            osc rm --force $i
            echo "  $i" >> qemu.changes.deleted
            let DELETED_COUNT+=1
            let TOTAL_COUNT+=1
        fi
    done
    mv $CHECK_DIR/* .
    if [ -e qemu.changes.added ]; then
        xargs osc add < qemu.changes.added
    fi

    if [[ -e checkthese ]]; then
        tar Jxf qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz \
        qemu-$SOURCE_VERSION/scripts/checkpatch.pl --strip-components=2
        for i in $(cat checkthese); do
            ./checkpatch.pl --no-tree --terse --no-summary --summary-file \
            --patch $i >> checkpatch.log || true
        done
    fi
    rm -f checkthese
    rm -f checkpatch.pl
    if [ -s checkpatch.log ]; then
        echo "WARNING: Issues reported by qemu patch checker. Please handle" \
            "ERROR items now:"
        cat checkpatch.log
    fi
    rm -f checkpatch.log
    if [ "$TOTAL_COUNT" != "0" -a "$VERSION_EXTRA" != "" -a "$OLD_COMMIT_ISH" =\
        "$NEW_COMMIT_ISH" ]; then
# Only patches changed: update the version using current timestamp
        VERSION_EXTRA=+git.$NOW_SECONDS.$OLD_COMMIT_ISH
        osc mv qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz \
            qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz
        osc add qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz
    fi

    echo "QEMU version file: $QEMU_VERSION"
    echo "QEMU source version: $SOURCE_VERSION"
    echo "QEMU version extra: $VERSION_EXTRA"

# get rid of "rel-" prefix to the seabios version - keep any trailing git info, such as: "-44-g88ab0c1"
    SEABIOS_VERSION=${SEABIOS_VERSION:-$(tar JxfO qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz \
        qemu-$SOURCE_VERSION/roms/seabios/.version | cut -c5- | tr '-' '_')}

    for package in $PKG; do
        while IFS= read -r line; do
            if [ "$line" = "PATCH_FILES" ]; then
# Here (and other places below) we try to get ONLY the numbered patches, but it's possible some ACTUAL patch name actually starts with multiple digits, but EXTREMELY unlikely
# TODO: do this better!
                for i in [0-9][0-9][0-9][0-9]*-*.patch; do
                    NUM=${i%%-*}
                    DIV=$((10#$NUM/$PATCH_RANGE))
                    REM=$((10#$NUM%$PATCH_RANGE))
                    if [[ "$REM" = "0" ]]; then
                        if [[ "$DIV" = "0" ]]; then
                            echo "# Patches applied in base project:"
                        else
                            echo "# Patches applied in ${PATCH_PATH_MAP[$DIV]}:"
                        fi
                    fi
                    if [[ "$FIVE_DIGIT_POTENTIAL" != "0" ]]; then
                        if [[ "$NUMBERED_PATCHES" = "0" ]]; then
                            PATCH_NUMBER=${i%%-*}
                            echo -e "Patch$NUM:     ${i:${#PATCH_NUMBER}+1:40+1+5}"
                        else
                            echo -e "Patch$NUM:     $i"
                        fi
                    else
                        if [[ "$NUMBERED_PATCHES" = "0" ]]; then
                            PATCH_NUMBER=${i%%-*}
                            echo -e "Patch$NUM:      ${i:${#PATCH_NUMBER}+1:40+1+5}"
                        else
                            echo -e "Patch$NUM:      $i"
                        fi
                    fi
                done
            elif [ "$line" = "PATCH_EXEC" ]; then
                unset PREV_S
                for i in [0-9][0-9][0-9][0-9]*-*.patch; do
                    S=$(grep "^Include-If: " $i) || true
                    NUM=${i%%-*}
                    if [ "$PREV_S" != "" -a "$PREV_S" != "$S" ]; then
                        echo "%endif"
                    fi
                    if [ "$S" != "" -a "$S" != "$PREV_S" ]; then
                        echo "${S:12}"
                    fi
                    echo "%patch$NUM -p1"
                    PREV_S=$S
                done
                if [ "$PREV_S" != "" ]; then
                    echo "%endif"
                fi
            elif [ "$line" = "INSERT_VERSIONING" ]; then
                echo "%define qemuver $QEMU_VERSION$VERSION_EXTRA"
                echo "%define srcver  $SOURCE_VERSION$VERSION_EXTRA"
                # For SLE11, where seabios isn't in the qemu tarball:
                if [[ "$SEABIOS_VERSION" != "" ]]; then
                    echo "%define sbver   $SEABIOS_VERSION"
                fi
            elif [[ "$line" =~ ^Source: ]]; then
                echo "$line"
                if [ ${#QEMU_TARBALL_SIG[@]} -eq 1 ]; then
# We assume the signature file corresponds - just add .sig
                    echo "$line.sig"|sed 's/^Source:  /Source99:/'
                fi
            else
                echo "$line"
            fi
        done < $package.spec.in > $CMP_DIR/$package.spec
        if cmp -s $package.spec $CMP_DIR/$package.spec; then
            echo "$package.spec unchanged"
        else
            mv $CMP_DIR/$package.spec $package.spec
            echo "$package.spec regenerated"
            let PACKAGE_CHANGED_COUNT+=1
        fi

        if [ "$WRITE_LOG" = "1" ]; then
# Factory requires all deleted and added patches to be mentioned
            if [ -e qemu.changes.deleted ]; then
                echo "* Patches dropped:" >> $package.changes.proposed
                cat qemu.changes.deleted  >> $package.changes.proposed
            fi
            if [ -e qemu.changes.added ]; then
                echo "* Patches added:" >> $package.changes.proposed
                cat qemu.changes.added  >> $package.changes.proposed
            fi
            if [ -e $package.changes.proposed ]; then
                osc vc --file=$package.changes.proposed $package
                rm -f $package.changes.proposed
            fi
        fi
    done
    if [[ "$NUMBERED_PATCHES" = "0" ]]; then
        rm -f [0-9][0-9][0-9][0-9]*-*.patch
    fi
    if [ -e qemu.changes.deleted ]; then
        rm -f qemu.changes.deleted
    fi
    if [ -e qemu.changes.added ]; then
        rm -f qemu.changes.added
    fi
    echo "git patch summary"
    echo "  unchanged: $UNCHANGED_COUNT"
    echo "    changed: $CHANGED_COUNT"
    echo "    deleted: $DELETED_COUNT"
    echo "      added: $ADDED_COUNT"
)

find $CMP_DIR -mindepth 1 -delete
rm -rf checkdir

osc service localrun format_spec_file || true
# Repair what I feel is incorrect modification of the package name in the header.
# Be aware that when checking into build service you should use --noservice, since we've
# already run this and --noservice will prevent the modification from happening at checkin
# time.
sed -i 's/^# spec file for package '$PKG'%{name_suffix}$/# spec file for package '$PKG'/g' $PKG.spec
sed -i 's/^# spec file for package '$PKG'-linux-user$/# spec file for package '$PKG'/g' $PKG.spec
}

#==============================================================================

setup_common_vars() {
if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    QEMU_VERSION=$(git -C ${LOCAL_REPO_MAP[0]} show upstream/master:VERSION)
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    X=$(echo $QEMU_VERSION|awk -F. '{print $3}')
# 0 = release, 50 = development cycle, 90..99 equate to release candidates
    if [ "$X" != "0" -a "$X" != "50" ]; then
        if [ "$NEXT_RELEASE_IS_MAJOR" = "0" ]; then
            SOURCE_VERSION=$MAJOR_VERSION.$[$MINOR_VERSION+1].0-rc$[X-90]
            GIT_BRANCH=opensuse-$MAJOR_VERSION.$[$MINOR_VERSION+1]
        else
            SOURCE_VERSION=$[$MAJOR_VERSION+1].0.0-rc$[X-90]
            GIT_BRANCH=opensuse-$[$MAJOR_VERSION+1].0
        fi
    else
        SOURCE_VERSION=$MAJOR_VERSION.$MINOR_VERSION.$X
        if [ "$X" = "0"  ]; then
            GIT_BRANCH=opensuse-$MAJOR_VERSION.$[$MINOR_VERSION]
        else
            if [ "$NEXT_RELEASE_IS_MAJOR" = "0" ]; then
                GIT_BRANCH=opensuse-$MAJOR_VERSION.$[$MINOR_VERSION+1]
            else
                GIT_BRANCH=opensuse-$[MAJOR_VERSION+1].0
            fi
        fi
    fi
else
    SOURCE_VERSION=$OLD_SOURCE_VERSION_AND_EXTRA
    QEMU_VERSION=$(tar JxfO qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz qemu-$SOURCE_VERSION/VERSION)
    if [ ! "$QEMU_VERSION" = "$OLD_SOURCE_VERSION_AND_EXTRA" ]; then
        echo "Tarball name (which we decode) doesn't correspond to the VERSION file contained therein"
        exit
    fi
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    GIT_BRANCH=opensuse-$MAJOR_VERSION.$MINOR_VERSION
fi
}

#==============================================================================

if [[ ! -e $(readlink -f ${LOCAL_REPO_MAP[0]}) ]]; then
    echo "No local repo found at ${LOCAL_REPO_MAP[0]}"
    if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
        echo "Using LATEST config.sh setting is an expert mode. Set up local repos accordingly"
        exit
    fi
    read -p "Would you like me to set that up for you? (Y/N)" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Got an affirmative answer, proceeding..."
        setup_common_vars
        git -c init.defaultBranch=$GIT_BRANCH init ${LOCAL_REPO_MAP[0]}
        git -C ${LOCAL_REPO_MAP[0]} remote add origin $PACKAGE_MAIN_GIT_REPO &>/dev/null
        git -C ${LOCAL_REPO_MAP[0]} fetch origin +refs/tags/initial:refs/tags/initial --no-tags
        git -C ${LOCAL_REPO_MAP[0]} reset --hard --recurse-submodules initial
#TODO: The next is not actually used - get rid of when we decide for sure it won't get used
        GIT_UPSTREAM_COMMIT=$(git -C ${LOCAL_REPO_MAP[0]} ls-remote origin |grep -F "$GIT_UPSTREAM_COMMIT_ISH^{}"|awk '{print $1}')
# Here we've changed to use *COMMIT_ISH, not *_COMMIT - is that an issue?
        git -C ${LOCAL_REPO_MAP[0]} fetch --depth=1 origin +refs/tags/$GIT_UPSTREAM_COMMIT_ISH:refs/tags/$GIT_UPSTREAM_COMMIT_ISH --no-tags
        git -C ${LOCAL_REPO_MAP[0]} remote add upstream $UPSTREAM_GIT_REPO &>/dev/null
        bundle2local
        git -C ${LOCAL_REPO_MAP[0]} checkout -B $GIT_BRANCH frombundle
        echo "We set up a shallow local repo of the package's git superproject at"
        echo "${LOCAL_REPO_MAP[0]}, and initialized it from the bundle."
        echo "(no options processed)"
        echo "If you wish to make the repo complete for all qemu packaging work,"
        echo "unshallow it first with git fetch --unshallow origin --all, then get"
        echo "the submodules updated with git submodule update --init --recursive"
        echo "Be aware that this downloads a LOT of data (that's why we didn't just"
        echo "do that automatically. Then you may also fetch other branches from the"
        echo "origin remote, and get the latest upstream patches from the upstream"
        echo "remote. Refer to config.sh for submodule repos locations you can set"
        echo "up to also work on patches for the superproject's submodules."
        exit
    else
        echo "Script requires qemu superproject local git repo. Please provide in"
        echo "order to use this script."
    fi
        exit
fi
# TODO: Perhaps useful: get the current state of the git superproject
# The following sends output to stdout which we don't want to see
#git -C ${LOCAL_REPO_MAP[0]} status --untracked-files=no --branch --porcelain=2 \
#    | awk '{print "var"NR"="$3}'
# $var1 is the current commit
# $var2 is the current branch or 'detached', if not on a branch
# $var3 is the current upstream branch (if set), as in eg 'origin/opensuse-5.0'
# $var4 is not of use to us

if [ "$GIT_UPSTREAM_COMMIT_ISH" != "LATEST" ]; then
    if [ ! "$GIT_UPSTREAM_COMMIT_ISH" = "v$OLD_SOURCE_VERSION_AND_EXTRA" ]; then
        echo "Tarball name (which we decode) doesn't correspond to the \$GIT_UPSTREAM_COMMIT_ISH in config.sh"
       exit
    fi
    setup_common_vars
fi
# TODO: What checks should be different between LATEST and non-LATEST?
echo "ALERT: Script using local git repos. Some operations may be time consuming..."
# TODO: Some of these checks are perhaps not necessary
for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
        if [[ -e ${LOCAL_REPO_MAP[$i]}/.git/shallow ]]; then
            echo "${LOCAL_REPO_MAP[$i]} is shallow, skipping checks"
            continue
        fi
        if [[ -d ${LOCAL_REPO_MAP[$i]}/.git/rebase-merge  || \
            -d ${LOCAL_REPO_MAP[$i]}/.git/rebase-apply ]]; then
            echo "ERROR! Rebase appears to be in progress in ${LOCAL_REPO_MAP[$i]}. Please resolve"
            exit
        fi
        # TODO: We've not even verified what branch we're on here - so this is a bit misguided!
        if ! git -C ${LOCAL_REPO_MAP[$i]} submodule update --init --recursive &> /dev/null; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(ensure git submodule update --init --recursive is successful)"
            exit
        fi
        if [ "$(git -C ${LOCAL_REPO_MAP[$i]} status --porcelain)" ]; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(ensure git status --porcelain produces no output)"
            exit
        fi
	# TODO: See about doing the following better (also see what needs to happen for LATEST)
        if [ "$GIT_UPSTREAM_COMMIT_ISH" != "LATEST" ]; then
            if $(git -C ${LOCAL_REPO_MAP[$i]} branch --remote | grep -F "origin/$GIT_BRANCH" >/dev/null); then
                if ! $(git -C ${LOCAL_REPO_MAP[$i]} branch | grep -F "$GIT_BRANCH" >/dev/null); then
                    echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
                    echo "(cannot find branch $GIT_BRANCH, please create a tracking branch of remote origin/$GIT_BRANCH)"
                    exit
                fi
                if ! git -C ${LOCAL_REPO_MAP[$i]} checkout $GIT_BRANCH --recurse-submodules -f &> /dev/null; then
                    echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
                    echo "(cannot check out $GIT_BRANCH, incl. it's submodules)"
                    exit
                fi
            fi
        fi
        # This does additional setup now that we've possibly grabbed additional submodules
        if ! git -C ${LOCAL_REPO_MAP[$i]} submodule update --init --recursive &> /dev/null; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(cannot init and update current branch submodules)"
            exit
        fi
        if [ "$(git -C ${LOCAL_REPO_MAP[$i]} status --porcelain)" ]; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(ensure git status --porcelain produces no output)"
            exit
        fi
    fi
done

# cleanup directories from any previous failed run:
rm -rf /dev/shm/qemu-???????-git-dir
rm -rf /dev/shm/qemu-???????-cmp-dir
rm -rf /dev/shm/qemu-???????-bun-dir
# Temporary directories used in this script
GIT_DIR=$(mktemp -d /dev/shm/qemu-XXXXXXX-git-dir)
CMP_DIR=$(mktemp -d /dev/shm/qemu-XXXXXXX-cmp-dir)
BUN_DIR=$(mktemp -d /dev/shm/qemu-XXXXXXX-bun-dir)

if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    if [ "$1" = "continue" ]; then
        CONTINUE_AFTER_REBASE=1
    else
        if [ "$1" = "pause" ]; then
            PAUSE_BEFORE_BUNDLE_CREATION=1
        else
           if [ "$1" ]; then
               echo "ERROR: unrecognized option '$1'. Script in LATEST mode only recognizes 'pause' and 'continue' options"
               exit
           fi
        fi
    fi
    for (( i=0; i <$REPO_COUNT; i++ )); do
        if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
            git -C ${LOCAL_REPO_MAP[$i]} remote update upstream &> /dev/null
        fi
    done
    NEW_COMMIT_ISH_FULL=$(cd ${LOCAL_REPO_MAP[0]} && git rev-parse upstream/master)
    NEW_COMMIT_ISH=${NEW_COMMIT_ISH_FULL:0:8}
    setup_common_vars
    WRITE_LOG=0
    echo "Processing LATEST upstream changes"
    echo "(If SUCCESS is not printed upon completion, see ~/latest.log for issues)"
    if [[ $QEMU_TARBALL =~ $BASE_RE$EXTRA_RE$SUFFIX_RE ]]; then
        OLD_COMMIT_ISH=${BASH_REMATCH[3]}
    else
        #Assume release (or release candidate) tarball with equivalent tag:
        OLD_COMMIT_ISH=$(cd ${LOCAL_REPO_MAP[0]} && git rev-list --abbrev-commit \
            --abbrev=8 -1 v$OLD_SOURCE_VERSION_AND_EXTRA)
    fi
    if [ ${#QEMU_TARBALL_SIG[@]} -ne 0 ]; then
        echo "INFO: Ignoring signature file: $QEMU_TARBALL_SIG"
        QEMU_TARBALL_SIG=
    fi
    NOW_SECONDS=$(date +%s)
    if  [ "$OLD_COMMIT_ISH" != "$NEW_COMMIT_ISH" ]; then
        if [ "$CONTINUE_AFTER_REBASE" = "1" ]; then
            echo "continue after rebase selected but tarball is out of date. Continuing not possible."
            echo "If desired, save your rebase work (eg, branch $GIT_BRANCH), because otherwise it will"
            echo "be lost. Then run script again without the continue option"
            exit
        fi
        redo_tarball_and_rebase_patches &> ~/latest.log # This includes a bundle2local
        if [[ "$REBASE_FAILS" ]]; then
            echo "ERROR! Rebase of the $GIT_BRANCH branch failed in the following local git repos:"
            echo $REBASE_FAILS
            echo "Manually resolve all these rebases, then finish the workflow by passing 'continue' to script"
            if [[ "$PAUSE_BEFORE_BUNDLE_CREATION" = "1" ]]; then
                echo "Feel free to also do the work now occasioned by the selected 'pause' option"
            fi
            exit
        fi
        CONTINUE_AFTER_REBASE=1
    fi
    if [[ "$PAUSE_BEFORE_BUNDLE_CREATION" = "1" ]]; then
        echo "As requested, pausing before re-creating bundle of bundles for additional patch or specfile work"
        echo "(using current 'ready to go' $GIT_BRANCH branch of local repos to produce patches.)"
        echo "When changes are complete, finish the workflow by passing 'continue' to script"
        exit
    fi
    if [ "$CONTINUE_AFTER_REBASE" = "1" ]; then
        initbundle &>> ~/latest.log
    fi
    bundle2spec &>> ~/latest.log
    echo "SUCCESS"
    tail -9 ~/latest.log
else # not LATEST
    NEW_COMMIT_ISH=
    WRITE_LOG=1
    case  $1 in
        initbundle )
            echo "Updating/creating the bundle using the $GIT_BRANCH branch of the local repos."
            echo "(If SUCCESS is not printed upon completion, see ~/initbundle.log for issues)"
            initbundle &> ~/initbundle.log
            echo "SUCCESS"
            ;;
        git2pkg )
            echo "Updating the package using the $GIT_BRANCH branch of the local repos."
            echo "(If SUCCESS is not printed upon completion, see ~/git2pkg.log for issues)"
            initbundle &> ~/git2pkg.log
            bundle2spec &>> ~/git2pkg.log
            echo "SUCCESS"
            tail -9 ~/git2pkg.log
            ;;
        pkg2git )
            echo "Exporting the package's git bundles to the local repo's frombundle branches..." 
            echo "(If SUCCESS is not printed upon completion, see ~/pkg2git.log for issues)"
            bundle2local &> ~/pkg2git.log
            echo "SUCCESS"
            echo "To modify package patches, use the frombundle branch as the basis for updating"
            echo "the $GIT_BRANCH branch with the new patch queue."
            echo "Then export the changes back to the package using update_git.sh git2pkg"
            ;;
        refresh )
            echo "Updating the spec file and patches from the spec file template and the bundle"
            echo "of bundles (bundles.tar.xz)"
            echo "(If SUCCESS is not printed upon completion, see ~/refresh.log for issues)"
            bundle2spec &> ~/refresh.log
            echo "SUCCESS"
            tail -9 ~/refresh.log
            ;;
    esac
fi
exit
