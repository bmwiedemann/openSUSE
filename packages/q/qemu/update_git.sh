#!/bin/bash

# update_git.sh: script to manage package maintenance using a git-based
# workflow. Commands are as follows:
#   git2pkg (update package spec file and patches from git)
#   pkg2git (update git (frombundle branch) from the package "bundleofbundles")
#   refresh (refresh spec file from spec file template and "bundlofbundles")
#
#   (default is git2pkg)

# TODO NOTES:

# after ensuring current status of local repo is clean, incl submodules, we checkout master+submodules, then also ensure they're clean, then checkout the commit or tag corresponding to latest / stable-release + submodules (but don't bother to verift that's clean) - so this is a detached HEAD for stable-release and IS master (almost certainly) for LATEST. WOW - is that what we need to be doing!?!?! At least it seems to be working for the cases I've seen!!!!
# initbundle operates from the current checked out state of the local superproject, to get the submodule ids - CORRECT!!!!
# the LATEST processing of cloning the local repo, clones master - but perhaps it doesn't matter? because it adds upstream as a remote and probably gets most things from there? INVESTIGATE!!!!!!!!!!!!!!!!!!!1
# bundle2local checks out master in local repo to ensure we're off the frombundle branch (doesn't seem needed the way the script currently is). It fetches the bundle's head (FETCH_HEAD) REQUIRING that the base commit be present (which it seems to be. Then it creates the frombundle branch, with the current FETCH_HEAD (SAME AS IN BUNDLE, RIGHT?)
# The LATEST's rebase loop checks out the frombundle branch (with force), so we are now OFF of the "correct checkout" that happened at the beginning, it DELETES the GIT_BRANCH (so in this case it DIDN'T MATTER WHAT WAS THERE WHEN SCRIPT STARTED !!!!!!! WARNING !!!!!, branches off of the frombundle branch (w/checkout), then rebases that (which came from bundle) onto the current superproject, or submodule commit id.
# At this point, if the GIT_BRANCH rebased ok, it's ready for making a patchqueue, out of, if the rebase failed, it's time to manually fix that.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# LATEST processing implies updated upstream/master IS the right thing
# HOW do we protect against a bad bundle being created (we do have the build service's tracking of previous files - is that sufficient?
# initbundle - what does it need? Currently we take the default branch in local superproject for the superproject and submodule commit ids, so it needs to be right! (ie which ever branch it is (DECIDE!), make it the RIGHT ONE for this release. It takes the commits from the $GIT_BUNDLE branch of each of superproject and submodule repos, which are beyond above found commits. IT CERTIANLY SEEMS REASONABLE THAT WE WOULD HAVE THE $$GIT_BRANCH BRANCH BE THE DEFAULT AND CORRECT BUT HOW DO WE GUARANTEE THATS OK? GIVEN OUR REQS HERE QEMU_VERSION CAN BE GRABBED HERE IN LOCAL SUPERPROJECT RIGHT AWAY!
# bundle2local - what does it need? This checks out local master just to get off of frombundle (could have been $GIT_BRANCH as well) No other req's
# bundle2spec - what does it need? THIS SHOULD HAVE LATEST SPLIT OUT!!!! We allow this alone, so see what setup it alone needs - for this one particularly, we don't want to REQUIRE local repo. FOR NOW I ASSUME THE RIGHT THING IS CHECKED OUT!
# 
# SEEMS WE SHOULD NOT,NOT,NOT require user to have previously updated, or set local repo a certain way, but for us to enforce it or actually do it
# TODO: confirm local repo present, correct remotes, correct local branches, somehow validate local branch content against remote, ...
# 
# In both cases we DO require the $GIT_BRANCH to exist, and should confirm that the appropriate upstream basis commit is indeed part of that. In the LATEST case, we can treat master as a source for initial current upstream.

set -e

source ./config.sh

declare -A COMMIT_IDS_BY_SUBMODULE_PATH

# Get version info from the packages' tarball - decode and do some checks
BASE_RE="qemu-[[:digit:]]+(\.[[:digit:]]+){2}(-rc[[:digit:]])?"
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

TEMP_CHECK() {

# Validate that all the local repos that we currently have patches in are available
# TEMPORARY REQUIREMENT!
for entry in ${REQUIRED_LOCAL_REPO_MAP[@]}; do
    if [[ -e $(readlink -f ${entry}) ]]; then
        if $(git -C $entry branch| grep -F "$GIT_BRANCH" >/dev/null); then
            :
        else
            echo "Didn't find the $GIT_BRANCH branch in repo at $entry"
            exit
        fi
    else
        echo "ERROR! For now, you need to have these local git repos available:"
        echo ${REQUIRED_LOCAL_REPO_MAP[@]}
        exit
    fi
done
}

#==============================================================================

initbundle() {
# The bundle tarball has git bundles stored in a directory structure which mimics the
# submodule locations in the containing git repo. Also at that same dir level
# is a file named repo which contains the one line git repo url (with git:// or
# http(s) prefix). The bundles are named as follows:
# "{path/}{git_sha}.{bundle}", where {path/} isn't present for
# the top (qemu) bundle (ie it's for submodules).

SUBMODULE_COMMIT_IDS=($(git -C ${LOCAL_REPO_MAP[0]} submodule status --recursive|awk '{print $1}'))
SUBMODULE_DIRS=($(git -C ${LOCAL_REPO_MAP[0]} submodule status --recursive|awk '{print $2}'))
SUBMODULE_COUNT=${#SUBMODULE_COMMIT_IDS[@]}
# TODO: do this with simply math - ie: use (( ... ))
if [[ "$REPO_COUNT" != "$(expr $SUBMODULE_COUNT + 1)" ]]; then
    echo "ERROR: submodule count doesn't match the REPO_COUNT variable in config.sh file!"
    exit
fi
rm -rf $GIT_DIR
rm -rf $BUNDLE_DIR
mkdir -p $BUNDLE_DIR
for (( i=0; i <$SUBMODULE_COUNT; i++ )); do
    mkdir -p $BUNDLE_DIR/${SUBMODULE_DIRS[$i]}
# what should this file be? for now use an extension of id 
    touch $BUNDLE_DIR/${SUBMODULE_DIRS[$i]}/${SUBMODULE_COMMIT_IDS[$i]}.id
done
if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    GIT_UPSTREAM_COMMIT=$NEW_COMMIT_ISH_FULL
else
# TODO: make this smarter, or change something - works for tag, but not normal commit?
    GIT_UPSTREAM_COMMIT=$(git -C ${LOCAL_REPO_MAP[0]} show-ref -d $GIT_UPSTREAM_COMMIT_ISH|grep -F "^{}"|awk '{print $1}')
fi
touch $BUNDLE_DIR/$GIT_UPSTREAM_COMMIT.id

# Now go through all the submodule local repos that are present and create a bundle file for the patches found there
for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
        SUBDIR=${PATCH_PATH_MAP[$i]}
        GITREPO_COMMIT_ISH=($BUNDLE_DIR/$SUBDIR*.id)
        if [[ $GITREPO_COMMIT_ISH  =~ .*(.{40})[.]id ]]; then
            GITREPO_COMMIT_ISH=${BASH_REMATCH[1]}
            echo "Using $GITREPO_COMMIT_ISH"
            PATCH_RANGE_INDEX=$i
            mkdir -p $GIT_DIR/$SUBDIR
            git -C $GIT_DIR/$SUBDIR init
            git -C $GIT_DIR/$SUBDIR remote add origin file://$(readlink -f \
                ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
            if [[ $(git -C $GIT_DIR/$SUBDIR ls-remote --heads origin $GIT_BRANCH) ]]; then
                git -C $GIT_DIR/$SUBDIR fetch origin $GIT_BRANCH
                if [[ $(git -C $GIT_DIR/$SUBDIR rev-list $GITREPO_COMMIT_ISH..FETCH_HEAD) ]]; then
                    git -C $GIT_DIR/$SUBDIR bundle create $BUNDLE_DIR/$SUBDIR$GITREPO_COMMIT_ISH.bundle $GITREPO_COMMIT_ISH..FETCH_HEAD
#TODO: post-process repo info to avoid un-needed diffs (eg git vs https)
                    git -C $(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]}) remote get-url origin >$BUNDLE_DIR/$SUBDIR/repo
                fi
            fi
        fi
    fi
done
# keep diffs to a minimum - touch bundle files to "something common"
tar --format gnu --xz \
    --numeric-owner \
    --owner=0 \
    --group=0 \
    --mtime="@$(date -r qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz +%s)" \
    --create \
    -f bundles.tar.xz -C $BUNDLE_DIR .
rm -rf $BUNDLE_DIR
rm -rf $GIT_DIR
}

#==============================================================================

bundle2local() {
rm -rf $BUNDLE_DIR
mkdir -p $BUNDLE_DIR
tar xJf bundles.tar.xz -C $BUNDLE_DIR
BUNDLE_FILES=$(find $BUNDLE_DIR -printf "%P\n"|grep "bundle$")

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

    LOCAL_REPO=$(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
    if [ -e $LOCAL_REPO ]; then
        git -C $LOCAL_REPO remote remove bundlerepo || true
	# git won't let you delete a branch we're on - so get onto master temporarily (TODO: is there a better approach?)
        git -C $LOCAL_REPO checkout master -f
        git -C $LOCAL_REPO branch -D frombundle || true
        git -C $LOCAL_REPO remote add bundlerepo $BUNDLE_DIR/$entry 
        git -C $LOCAL_REPO fetch bundlerepo FETCH_HEAD
        git -C $LOCAL_REPO branch frombundle FETCH_HEAD
        git -C $LOCAL_REPO remote remove bundlerepo
    else
        echo "No local repo $LOCAL_REPO corresponding to archived git bundle!"
        exit
    fi
done
rm -rf $BUNDLE_DIR
}

#==============================================================================

redo_tarball_and_rebase_patches() {
rm -rf $GIT_DIR

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CREATE TARBALL, USING FRESH REPO - WE COULD RELY MORE ON LOCAL IF WE WERE MORE CAREFUL
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# TODO: WHAT IS THIS NEXT LINE EVEN DOING FOR US?? (OK, it's initing a repo, what do we rely on there?)
git clone -ls ${LOCAL_REPO_MAP[0]} $GIT_DIR -b master --single-branch &>/dev/null
echo "Please wait..."
(cd $GIT_DIR && git remote add upstream \
git://git.qemu-project.org/qemu.git &>/dev/null)
(cd $GIT_DIR && git remote update upstream &>/dev/null)
(cd $GIT_DIR && git checkout $NEW_COMMIT_ISH &>/dev/null)
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
# REBASE frombundle patches USING COMMIT_IDS_BY_SUBMODULE, ALSO USING OLD ID'S STORED IN OLD BUNDLE 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

mkdir -p $BUNDLE_DIR
tar xJf bundles.tar.xz -C $BUNDLE_DIR
# Now go through all the submodule local repos that are present and create a bundle file for the patches found there
for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
        if $(git -C ${LOCAL_REPO_MAP[$i]} branch | grep -F "frombundle" >/dev/null); then
            SUBDIR=${PATCH_PATH_MAP[$i]}
            GITREPO_COMMIT_ISH=($BUNDLE_DIR/$SUBDIR*.id)
            if [[ $GITREPO_COMMIT_ISH  =~ .*(.{40})[.]id ]]; then
                GITREPO_COMMIT_ISH=${BASH_REMATCH[1]}
            fi
            git -C ${LOCAL_REPO_MAP[$i]} checkout frombundle -f
            git -C ${LOCAL_REPO_MAP[$i]} branch -D $GIT_BRANCH
            git -C ${LOCAL_REPO_MAP[$i]} checkout -b $GIT_BRANCH
            if [[ "$SUBDIR" = "" ]]; then
                SUBDIR=SUPERPROJECT
            fi
            if ! $(git -C ${LOCAL_REPO_MAP[$i]} rebase --onto ${COMMIT_IDS_BY_SUBMODULE_PATH[$SUBDIR]} $GITREPO_COMMIT_ISH  >/dev/null); then
# TODO: record that this one needs manual help!
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
rm -rf $GIT_DIR
rm -rf $CMP_DIR
rm -rf $BUNDLE_DIR
mkdir -p $BUNDLE_DIR

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOW PROCESS BUNDLES INTO COMMITS AND FILL SPEC FILE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tar xJf bundles.tar.xz -C $BUNDLE_DIR
BUNDLE_FILES=$(find $BUNDLE_DIR -printf "%P\n"|grep "bundle$")

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

    mkdir -p $GIT_DIR/$SUBDIR
    git -C $GIT_DIR/$SUBDIR init
    git -C $GIT_DIR/$SUBDIR remote add origin file://$(readlink -f \
        ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]})
    git -C $GIT_DIR/$SUBDIR fetch origin $GIT_BRANCH
    git -C $GIT_DIR/$SUBDIR reset --hard $GITREPO_COMMIT_ISH
    git -C $GIT_DIR/$SUBDIR remote add bundle $BUNDLE_DIR/$entry 
    git -C $GIT_DIR/$SUBDIR fetch bundle FETCH_HEAD
    git -C $GIT_DIR/$SUBDIR format-patch -N --suffix= --no-renames -o $CMP_DIR -k --stat=72 \
        --indent-heuristic --zero-commit --no-signature --full-index \
        --src-prefix=a/$SUBDIR --dst-prefix=b/$SUBDIR \
        --start-number=$(expr $PATCH_RANGE_INDEX \* $PATCH_RANGE) \
        $GITREPO_COMMIT_ISH..FETCH_HEAD > /dev/null
done

rm -rf $GIT_DIR
rm -rf $BUNDLE_DIR

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
    if [[ "$NUMBERED_PATCHES" = "0" ]]; then
        for i in [0-9]*.patch; do
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
    else
        CHECK_PREFIX="00"
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
    if [ "$FIVE_DIGIT_POTENTIAL" = "0" ]; then
        NUMBERED_PATCH_RE="^[[:digit:]]{4}-.*[.]patch$"
    else
        NUMBERED_PATCH_RE="^[[:digit:]]{5}-.*[.]patch$"
    fi
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

    for package in qemu; do
        while IFS= read -r line; do
            if [ "$line" = "PATCH_FILES" ]; then
                for i in [0-9]*-*.patch; do
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
                for i in [0-9]*-*.patch; do
		    S=$(grep "^Include-If: " $i) || true
                    NUM=${i%%-*}
                    if [ "$S" != "" ]; then
			echo "${S:12}"
                        echo "%patch$NUM -p1"
                        echo "%endif"
                    else
                        echo "%patch$NUM -p1"
                    fi
                done
            elif [ "$line" = "INSERT_VERSIONING" ]; then
                echo "%define qemuver $QEMU_VERSION$VERSION_EXTRA"
                echo "%define srcver  $SOURCE_VERSION$VERSION_EXTRA"
                echo "%define sbver   $SEABIOS_VERSION"
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
        rm -f [0-9]*-*.patch
    fi
    if [ -e qemu.changes.deleted ]; then
        rm -f qemu.changes.deleted
    fi
    if [ -e qemu.changes.added ]; then
        rm -f qemu.changes.added
    fi
# Decide if there is a better way to handle the no change case:
#    if [[ "0" = "$(expr $CHANGED_COUNT + $DELETED_COUNT + $ADDED_COUNT)" ]]; then
#        osc revert bundles.tar.xz
#    fi
    echo "git patch summary"
    echo "  unchanged: $UNCHANGED_COUNT"
    echo "    changed: $CHANGED_COUNT"
    echo "    deleted: $DELETED_COUNT"
    echo "      added: $ADDED_COUNT"
)

rm -rf $CMP_DIR
rm -rf checkdir

osc service localrun format_spec_file
}

#==============================================================================

usage() {
echo "Usage:"
echo "bash ./git_update.sh <command>"
echo "description: package maintenance using a git-based workflow. Commands:"
echo "  git2pkg (update package spec file and patches from git. Is default)"
echo "  pkg2git (update git (frombundle branch) from the package "bundleofbundles")"
echo "  refresh (refresh spec file from spec file template and "bundlofbundles")"
echo "(See script for details on doing 'LATEST' workflow)"
}

#==============================================================================

explain_setup() {
echo "Currently we require local git repos at these locations:"
echo "${REQUIRED_LOCAL_REPO_MAP[@]}"
echo "Where each has as it's remote the uri: https://github.com/opensuse/*.git"
echo "and where * is replaced by the qemu-whatever, and the remote is named origin"
echo "and the qemu or qemu submodule repos as remotes named upstream"
}

#==============================================================================

if [[ ! -e $(readlink -f ${LOCAL_REPO_MAP[0]}) ]]; then
    echo "ERROR: Local QEMU related git repos not found. Please follow these setup instructions:"
    explain_setup
    exit
fi
# There are some req's on needing a recent git, and a recent osc (double chk the osc part - I guess it's related to the osc service )

# get the current state of the git superproject
# TODO: This sends output to stdout which we don't want to see
git -C ${LOCAL_REPO_MAP[0]} status --untracked-files=no --branch --porcelain=2 \
    | awk '{print "var"NR"="$3}'
# $var1 is the current commit
# $var2 is the current branch or 'detached', if not on a branch
# $var3 is the current upstream branch (if set), as in eg 'origin/opensuse-5.0'
# $var4 is not of use to us

# TODO: What checks should be different between LATEST and non-LATEST?
# If we don't actually patch from the submodule repo, we shouldn't care about what's in the local one
# Does non-LATEST really require master?
echo "WARNING: Script using local git repos. Some operations may be time consuming..."
#TODO: Most of these checks are not necessary
for (( i=0; i <$REPO_COUNT; i++ )); do
    if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
	if [[ -d ${LOCAL_REPO_MAP[$i]}/.git/rebase-merge  || \
            -d ${LOCAL_REPO_MAP[$i]}/.git/rebase-apply ]]; then
            echo "ERROR! Rebase appears to be in progress in ${LOCAL_REPO_MAP[$i]}. Please resolve"
            exit
        fi
# !! Does this presume the branch as indicated in config is the current branch? (I believe that's been my modus operandi to date, so perhaps THAT should be enforced at this point?)
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
        if ! git -C ${LOCAL_REPO_MAP[$i]} checkout master --recurse-submodules -f &> /dev/null; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(cannot check out master, incl. it's submodules)"
            exit
        fi
        if ! git -C ${LOCAL_REPO_MAP[$i]} submodule update --init --recursive &> /dev/null; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(cannot init and update master submodules)"
            exit
        fi
	if [ "$(git -C ${LOCAL_REPO_MAP[$i]} status --porcelain)" ]; then
            echo "Please clean up state of local repo ${LOCAL_REPO_MAP[$i]} before using script"
            echo "(ensure git status --porcelain produces no output)"
            exit
        fi
    fi
done
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
    git -C ${LOCAL_REPO_MAP[0]} checkout $NEW_COMMIT_ISH_FULL --recurse-submodules -f &> /dev/null
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
    WRITE_LOG=0
    echo "Processing LATEST upstream changes"
    echo "(If SUCCESS is not printed upon completion, see /tmp/latest.log for issues)"
    TEMP_CHECK
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
        redo_tarball_and_rebase_patches &> /tmp/latest.log
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
        initbundle &>> /tmp/latest.log
    fi
    bundle2spec &>> /tmp/latest.log
    echo "SUCCESS"
    tail -9 /tmp/latest.log
else # not LATEST
    if [ ! "$GIT_UPSTREAM_COMMIT_ISH" = "v$OLD_SOURCE_VERSION_AND_EXTRA" ]; then
        echo "Tarball name (which we decode) doesn't correspond to the \$GIT_UPSTREAM_COMMIT_ISH in config.sh"
       exit
    fi
    git -C ${LOCAL_REPO_MAP[0]} checkout $GIT_UPSTREAM_COMMIT_ISH --recurse-submodules -f &> /dev/null
    NEW_COMMIT_ISH=
    SOURCE_VERSION=$OLD_SOURCE_VERSION_AND_EXTRA
    QEMU_VERSION=$(tar JxfO qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz qemu-$SOURCE_VERSION/VERSION)
    if [ ! "$QEMU_VERSION" = "$OLD_SOURCE_VERSION_AND_EXTRA" ]; then
            echo "Tarball name (which we decode) doesn't correspond to the VERSION file contained therein"
            exit
    fi
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    GIT_BRANCH=opensuse-$MAJOR_VERSION.$MINOR_VERSION
    WRITE_LOG=1
    if [ "$1" = "" ]; then
        set -- git2pkg
    fi
    case  $1 in
        initbundle )
            initbundle
            ;;
        git2pkg )
            echo "Updating the package using the $GIT_BRANCH branch of the local repos."
            echo "(If SUCCESS is not printed upon completion, see /tmp/git2pkg.log for issues)"
            TEMP_CHECK
            initbundle &> /tmp/git2pkg.log
            bundle2spec &>> /tmp/git2pkg.log
            echo "SUCCESS"
            tail -9 /tmp/git2pkg.log
            ;;
        pkg2git )
            echo "Exporting the package's git bundles to the local repo's frombundle branches..." 
            echo "(If SUCCESS is not printed upon completion, see /tmp/pkg2git.log for issues)"
            TEMP_CHECK
            bundle2local &> /tmp/pkg2git.log
            echo "SUCCESS"
            echo "To modify package patches, use the frombundle branch as the basis for updating"
            echo "the $GIT_BRANCH branch with the new patch queue."
            echo "Then export the changes back to the package using update_git.sh git2pkg"
            ;;
        refresh )
            echo "Updating the spec file and patches from the spec file template and the bundle"
            echo "of bundles (bundles.tar.xz)"
            echo "(If SUCCESS is not printed upon completion, see /tmp/refresh.log for issues)"
            TEMP_CHECK
            bundle2spec &> /tmp/refresh.log
            echo "SUCCESS"
            tail -9 /tmp/refresh.log
            ;;
        * )
            echo "Unknown command"
            usage
            ;;
        help )
            usage
	    ;;
    esac
fi
exit

