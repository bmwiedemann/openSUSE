#!/bin/bash

# update_git.sh: script to manage package maintenance using a git-based
# workflow. Commands are as follows:
#   git2pkg (update package spec file and patches from git)
#   pkg2git (update git (frombundle branch) from the package "bundleofbundles")
#   refresh (refresh spec file from spec file template and "bundlofbundles")
#
#   (default is git2pkg)

set -e

source ./config.sh

declare -A COMMIT_IDS_BY_SUBMODULE_PATH

TEMP_CHECK() {
# TEMPORARY! FOR NOW WE REQUIRE THESE LOCALLY TO DO WORK ON PACKAGE
REQUIRED_LOCAL_REPO_MAP=(
    ~/git/qemu-opensuse
    ~/git/qemu-seabios
    ~/git/qemu-ipxe
    ~/git/qemu-sgabios
    ~/git/qemu-skiboot
    ~/git/qemu-keycodemapdb
)

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
    GIT_UPSTREAM_COMMIT=$(cd ${LOCAL_REPO_MAP[0]} && git rev-parse upstream/master)
else
# (I need to make this smarter, or change something - works for tag, but not normal commit?):
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
            git -C $(readlink -f ${LOCAL_REPO_MAP[$PATCH_RANGE_INDEX]}) remote get-url origin >$BUNDLE_DIR/$SUBDIR/repo
            if [[ $(git -C $GIT_DIR/$SUBDIR ls-remote --heads origin $GIT_BRANCH) ]]; then
                git -C $GIT_DIR/$SUBDIR fetch origin $GIT_BRANCH
                if [[ $(git -C $GIT_DIR/$SUBDIR rev-list $GITREPO_COMMIT_ISH..FETCH_HEAD) ]]; then
                    git -C $GIT_DIR/$SUBDIR bundle create $BUNDLE_DIR/$SUBDIR$GITREPO_COMMIT_ISH.bundle $GITREPO_COMMIT_ISH..FETCH_HEAD || true
                fi
            fi
        fi
    fi
done
tar cJvf bundles.tar.xz -C $BUNDLE_DIR .
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
# TODO: Detect if it's there before trying to remove!
        git -C $LOCAL_REPO remote remove bundlerepo || true
# git won't let you delete this branch if it's the current branch (returns 1) HOW TO HANDLE?
# detect this case, and ask user to switch to another branch? or do it for them - switch to master killing any "state" for this branch
        git -C $LOCAL_REPO checkout master -f
        git -C $LOCAL_REPO branch -D frombundle || true
        git -C $LOCAL_REPO remote add bundlerepo $BUNDLE_DIR/$entry 
# in next, the head may be FETCH_HEAD or HEAD depending on how we created:
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

bundle2spec() {
rm -rf $GIT_DIR
rm -rf $CMP_DIR
rm -rf $BUNDLE_DIR
rm -f checkpatch.log
rm -f checkthese
# there's probably a better place for the next: (only needed due to development failures?)
rm -rf checkdir

if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    for (( i=0; i <$REPO_COUNT; i++ )); do
        if [[ -e $(readlink -f ${LOCAL_REPO_MAP[$i]}) ]]; then
            git -C ${LOCAL_REPO_MAP[$i]} remote update upstream &> /dev/null
        fi
    done
#TODO: do we really want to checkout here? the code which gets the latest submodule commits doesnt rely on this !!! IN FACT master here isn't for latest upstream - that is the upstream branch!
#    git -C ${LOCAL_REPO_MAP[0]} checkout master --recurse-submodules -f
# TODO: THE FOLLOWING NEEDS HELP
    QEMU_VERSION=$(git -C ${LOCAL_REPO_MAP[0]} show origin:VERSION)
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    if [ "$NEXT_RELEASE_IS_MAJOR" = "0" ]; then
        GIT_BRANCH=opensuse-$MAJOR_VERSION.$[$MINOR_VERSION+1]
    else
        GIT_BRANCH=opensuse-$[$MAJOR_VERSION+1].0
    fi
fi

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
# It's ok for either of these to be empty when using "LATEST"
OLD_SOURCE_VERSION_AND_EXTRA=$(echo $QEMU_TARBALL 2>/dev/null | head --bytes=-8\
    | cut --bytes=6-)
VERSION_EXTRA=$(echo $OLD_SOURCE_VERSION_AND_EXTRA|awk -F+ '{if ($2) print \
    "+"$2}')
if [ "$OLD_SOURCE_VERSION_AND_EXTRA" = "" ]; then
    echo "Warning: No tarball found"
fi

# TODO: (repo file not yet done)
if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DO TARBALL, GETTING ALL FROM UPSTREAM DIRECTLY
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if [[ $QEMU_TARBALL =~ $BASE_RE$EXTRA_RE$SUFFIX_RE ]]; then
        OLD_COMMIT_ISH=${BASH_REMATCH[3]}
    else
        #Assume release (or release candidate) tarball with equivalent tag:
        OLD_COMMIT_ISH=$(cd ${LOCAL_REPO_MAP[0]} && git rev-list --abbrev-commit \
            --abbrev=9 -1 v$OLD_SOURCE_VERSION_AND_EXTRA)
    fi
    if [ ${#QEMU_TARBALL_SIG[@]} -ne 0 ]; then
        echo "INFO: Ignoring signature file: $QEMU_TARBALL_SIG"
        QEMU_TARBALL_SIG=
    fi
# TODO: HERE WE REFERENCE MASTER - NEEDS FIXING
    NEW_COMMIT_ISH_FULL=$(cd ${LOCAL_REPO_MAP[0]} && git rev-parse upstream/master)
    NEW_COMMIT_ISH=$(cd ${LOCAL_REPO_MAP[0]} && git rev-parse --short=9 \
        upstream/master)
    NOW_SECONDS=$(date +%s)

# TODO: HERE WE REFERENCE MASTER - NEEDS FIXING
    git clone -ls ${LOCAL_REPO_MAP[0]} $GIT_DIR -b master --single-branch &>/dev/null
    if  [ "$OLD_COMMIT_ISH" != "$NEW_COMMIT_ISH" ]; then
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
    fi
    QEMU_VERSION=$(cat $GIT_DIR/VERSION)
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    X=$(echo $QEMU_VERSION|awk -F. '{print $3}')
    # 0 = release, 50 = development cycle, 90..99 equate to release candidates
    if [ "$X" != "0" -a "$X" != "50" ]; then
        if [ "$NEXT_RELEASE_IS_MAJOR" = "0" ]; then
            SOURCE_VERSION=$MAJOR_VERSION.$[$MINOR_VERSION+1].0-rc$[X-90]
        else
            SOURCE_VERSION=$[$MAJOR_VERSION+1].0.0-rc$[X-90]
        fi
    else
        SOURCE_VERSION=$MAJOR_VERSION.$MINOR_VERSION.$X
    fi
    if [ "$OLD_COMMIT_ISH" != "$NEW_COMMIT_ISH" ]; then
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
# OK GET THE SUBMODULE COMMIT ID'S FROM THIS NEWLY MINTED QEMU CHECKOUT! WE'LL USE THAT WHEN WE REBASE OUR PATCHES
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !! We (perhaps temporarily) do MORE recursive submodules, since we are tracking ALL in these scripts, while upstream doesn't include all in tarball currently 
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
        mkdir -p $BUNDLE_DIR
        tar xJf bundles.tar.xz -C $BUNDLE_DIR
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# REBASE frombundle patches USING COMMIT_IDS_BY_SUBMODULE, ALSO USING OLD ID'S STORED IN OLD BUNDLE 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
                    fi
                fi
            fi
        done
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# CREATE BUNDLE FROM $GIT_BRANCH branch
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        initbundle
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# GET BUNDLE PATCHES FROM BUNDLE_DIR
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    fi
    rm -rf $GIT_DIR
    # We're done with GIT_UPSTREAM_COMMIT_ISH carrying the special value LATEST
    GIT_UPSTREAM_COMMIT_ISH=$NEW_COMMIT_ISH
    WRITE_LOG=0
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DONE WITH LATEST WORK
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
else # not based on LATEST upstream master, rather any upstream commitish
    if [ "$OLD_SOURCE_VERSION_AND_EXTRA" = "" ]; then
        echo "Failure: tarball required which corresponds to commitish:" \
            "$GIT_UPSTREAM_COMMITISH"
        exit
    fi
    if [ -d "${LOCAL_REPO_MAP[0]}" ]; then
        echo "Processing local git tree branch: master, using commitish:"\
            "$GIT_UPSTREAM_COMMIT_ISH"
        if ! (cd ${LOCAL_REPO_MAP[0]} && git show-branch master &>/dev/null)
        then
            echo "Error: Branch master not found - please create a remote"\
                "tracking branch of origin/master"
            exit
        fi
# ( THIS ISNT WORKING - IS OLD HISTORY:)
    else
        echo "Processing $GIT_BRANCH branch of remote git tree, using"\
            "commitish: $GIT_UPSTREAM_COMMIT_ISH"
        echo "(For fast processing, consider establishing a local git tree"\
            "at ${LOCAL_REPO_MAP[0]})"
    fi
    SOURCE_VERSION=$OLD_SOURCE_VERSION_AND_EXTRA
    QEMU_VERSION=$(tar JxfO qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz qemu-$SOURCE_VERSION/VERSION)
    NEW_COMMIT_ISH=
    WRITE_LOG=1
fi
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOW PROCESS BUNDLES INTO COMMITS AND FILL SPEC FILE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
            if [[ $BASENAME =~ [[:digit:]]{4}-.* ]]; then
                BASENAME=0$BASENAME
            fi
	fi
        if [[ "$NUMBERED_PATCHES" = "0" ]]; then
	    KEEP_COUNT=40+4+$FIVE_DIGIT_POTENTIAL+1
        else
	    KEEP_COUNT=40
	fi
        tail -n +2 $i > $CMP_DIR/${BASENAME:0:$KEEP_COUNT}.patch
	rm $i
    done
    if [[ "$NUMBERED_PATCHES" = "0" ]]; then
        for i in [0-9]*.patch; do
            osc rm --force $i
        done
        # we need to make sure that w/out the numbered prefixes, the patchnames are all unique
        mkdir checkdir
        for i in $CMP_DIR/*; do
            BASENAME=$(basename $i)
	    FINALNAME=${BASENAME:4+$FIVE_DIGIT_POTENTIAL+1:40+1+5}
	    if [[ -e checkdir/$FINALNAME ]]; then
	        echo "ERROR! Patch name $FINALNAME is not unique! Please modify patch subject to achieve uniqueness"
	        exit 1
            fi
	    cp $i checkdir/$FINALNAME
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
        if [ -e $BASENAME ]; then
            if cmp -s $i $BASENAME; then
                touch --reference=$BASENAME $i
                rm $BASENAME
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
	if [[ $i =~ $NUMBERED_PATCH_RE ]]; then
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
        # Patches changed, so update the version using current time 
        VERSION_EXTRA=+git.$NOW_SECONDS.$OLD_COMMIT_ISH
        osc mv qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz \
            qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz
        osc add qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz
    fi

    echo "QEMU version file: $QEMU_VERSION"
    echo "QEMU source version: $SOURCE_VERSION"
    echo "QEMU version extra: $VERSION_EXTRA"

    SEABIOS_VERSION=$(tar JxfO qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz \
        qemu-$SOURCE_VERSION/roms/seabios/.version | cut -d '-' -f 2)

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
            elif [ "$line" = "QEMU_VERSION" ]; then
                echo "%define qemuver $QEMU_VERSION$VERSION_EXTRA"
                echo "%define srcver  $SOURCE_VERSION$VERSION_EXTRA"
                echo "Version:        %qemuver"
            elif [[ "$line" =~ ^Source: ]]; then
                echo "$line"
                if [ ${#QEMU_TARBALL_SIG[@]} -eq 1 ]; then
                    # We assume the signature file corresponds - just add .sig
                    echo "$line.sig"|sed 's/^Source:  /Source99:/'
                fi
            elif [ "$line" = "SEABIOS_VERSION" ]; then
                echo "Version:        $SEABIOS_VERSION"
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
            if [ -e qemu.changes.deleted ] || [ -e qemu.changes.added ]; then
                echo "Patch queue updated from ${GIT_TREE} ${GIT_BRANCH}" > \
                    $package.changes.proposed
            fi
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
    echo "bash ./git_update.sh <command>
    echo description: package maintenance using a git-based workflow. Commands:"
    echo "  git2pkg (update package spec file and patches from git. Is default)"
    echo "  pkg2git (update git (frombundle branch) from the package "bundleofbundles")"
    echo "  refresh (refresh spec file from spec file template and "bundlofbundles")"
}

#==============================================================================

# LATEST processing currently doesn't expect cmdline params, so do it here, up front
if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    echo "Processing latest upstream changes"
    echo "(If SUCCESS is not printed upon completion, see /tmp/latest.log for issues)"
    TEMP_CHECK
    bundle2spec &> /tmp/latest.log
    echo "SUCCESS"
    tail -9 /tmp/latest.log
    exit
fi

if [ "$1" = "" ]; then
    set -- git2pkg
fi
case  $1 in
    initbundle )
        initbundle
        ;;
    git2pkg )
        echo "Updating the package from the $GIT_BRANCH branch of the local repos."
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
