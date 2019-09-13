#!/bin/bash
#
# Instead of a quilt workflow, we use a git tree that contains
# all the commits on top of a qemu source tarball.
#
# When updating this package, just either update the git tree
# below (use rebase!) or change the tree path and use your own
#
# That way we can easily rebase against the next stable release
# when it comes.

set -e

# The next few VARIABLES may be edited (or uncommented) as required:

# Here is where we manage the patchqueue on top of what comes from upstream
GIT_LOCAL_TREE=~/git/qemu-opensuse
# The commit upon which our patchqueue gets rebased. The special value LATEST
# may be used to "automatically" track the upstream development tree in the
# master branch
GIT_UPSTREAM_COMMIT_ISH=v4.0.0
if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    echo "Using LATEST upstream commit as base for tarball and patch queue"
    GIT_BRANCH=master
fi
# otherwise we specify the branch to use, eg:
# WARNING: If transitioning from using LATEST to not, MANUALLY re-set the
# tarball present
GIT_BRANCH=opensuse-4.0
# This is used for the automated development branch tracking
NEXT_RELEASE_IS_MAJOR=1

# The shared openSUSE specific git repo, on which $GIT_LOCAL_TREE is based
GIT_TREE=git://github.com/openSUSE/qemu.git

# Temporary directories used by this script
GIT_DIR=/dev/shm/qemu-factory-git-dir
CMP_DIR=/dev/shm/qemu-factory-cmp-dir

rm -rf $GIT_DIR
rm -rf $CMP_DIR
rm -f checkpatch.log

if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    # This is just a safety valve in case the above gets edited wrong:
    if ! [ "$GIT_BRANCH" = "master" ]; then
        echo "LATEST implies master branch, please fix configuration"
        exit
    fi
    (cd $GIT_LOCAL_TREE && git remote update upstream)
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

if [ "$GIT_UPSTREAM_COMMIT_ISH" = "LATEST" ]; then
    if [[ $QEMU_TARBALL =~ $BASE_RE$EXTRA_RE$SUFFIX_RE ]]; then
        OLD_COMMIT_ISH=${BASH_REMATCH[3]}
    else
        #Assume release (or release candidate) tarball with equivalent tag:
        OLD_COMMIT_ISH=$(cd $GIT_LOCAL_TREE && git rev-list --abbrev-commit \
            --abbrev=9 -1 v$OLD_SOURCE_VERSION_AND_EXTRA)
    fi
    if [ ${#QEMU_TARBALL_SIG[@]} -ne 0 ]; then
        echo "INFO: Ignoring signature file: $QEMU_TARBALL_SIG"
        QEMU_TARBALL_SIG=
    fi
    NEW_COMMIT_ISH=$(cd $GIT_LOCAL_TREE && git rev-parse --short=9 \
        upstream/$GIT_BRANCH)
    NOW_SECONDS=$(date +%s)

    git clone -ls $GIT_LOCAL_TREE $GIT_DIR -b $GIT_BRANCH &>/dev/null
    if  [ "$OLD_COMMIT_ISH" != "$NEW_COMMIT_ISH" ]; then
        echo "Please wait..."
        (cd $GIT_DIR && git remote add upstream \
        git://git.qemu-project.org/qemu.git &>/dev/null)
        (cd $GIT_DIR && git remote update upstream &>/dev/null)
        (cd $GIT_DIR && git checkout $NEW_COMMIT_ISH &>/dev/null)
        # TODO: starting patch number for submodules are as follows:
        # 1100: roms/seabios
        # 1200: roms/ipxe
        # 1300: roms/sgabios
        # 1400: roms/SLOF
        # 1500: roms/skiboot
        # 1600: ui/keycodemapdb
        # 1700: roms/openbios
        (cd $GIT_DIR && git submodule update --init --recursive &>/dev/null)
        VERSION_EXTRA=+git.$NOW_SECONDS.$NEW_COMMIT_ISH
    fi
    QEMU_VERSION=$(cat $GIT_DIR/VERSION)
    MAJOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $1}')
    MINOR_VERSION=$(echo $QEMU_VERSION|awk -F. '{print $2}')
    X=$(echo $QEMU_VERSION|awk -F. '{print $3}')
    # 0 = release, 50 = development cycle, 90..99 equate to release candidates
    if [ "$X" != "0" -a "$X" != "50" ]; then
        if [ "$NEXT_RELEASE_IS_MAJOR" == "0" ]; then
            SOURCE_VERSION=$MAJOR_VERSION.$[$MINOR_VERSION+1].0-rc$[X-90]
        else
            SOURCE_VERSION=$[$MAJOR_VERSION+1].0.0-rc$[X-90]
        fi
    else
        SOURCE_VERSION=$MAJOR_VERSION.$MINOR_VERSION.$X
    fi
    if  [ "$OLD_COMMIT_ISH" != "$NEW_COMMIT_ISH" ]; then
        if (cd $GIT_LOCAL_TREE && git describe --exact-match $NEW_COMMIT_ISH \
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
        echo "New tarball created. Attempting rebase..."
        if ! (cd $GIT_DIR && git rebase upstream/$GIT_BRANCH $GIT_BRANCH); then
            echo "rebasing master on upstream/master needs human assistance." \
                "Exiting"
            (cd $GIT_DIR && git rebase --abort)
            rm qemu-$SOURCE_VERSION$VERSION_EXTRA.tar 
            exit
        fi
        echo "WARNING: To rebase, master is being checked out"
        if ! (cd $GIT_LOCAL_TREE && git rebase upstream/$GIT_BRANCH \
        $GIT_BRANCH); then
            echo "WARNING: Script error? rebasing master on upstream/master" \
                "succeeded in temp"
            echo "dir but failed in local tree! Please investigate"
            (cd $GIT_LOCAL_TREE && git rebase --abort)
            rm qemu-$SOURCE_VERSION$VERSION_EXTRA.tar 
            exit
        fi
        echo "Rebase successful"
        osc rm --force qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz &>/dev/null ||\
            true
        osc rm --force qemu-$OLD_SOURCE_VERSION_AND_EXTRA.tar.xz.sig \
            &>/dev/null || true
        unset QEMU_TARBALL_SIG
        xz -T 0 qemu-$SOURCE_VERSION$VERSION_EXTRA.tar
        osc add qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz 
    fi
    # We're done with GIT_UPSTREAM_COMMIT_ISH carrying the special value LATEST
    GIT_UPSTREAM_COMMIT_ISH=$NEW_COMMIT_ISH
    WRITE_LOG=0
else # not based on LATEST upstream master, rather any upstream commitish
    if [ "$OLD_SOURCE_VERSION_AND_EXTRA" = "" ]; then
        echo "Failure: tarball required which corresponds to commitish:" \
            "$GIT_UPSTREAM_COMMITISH"
        exit
    fi
    if [ -d "$GIT_LOCAL_TREE" ]; then
        echo "Processing local git tree branch: $GIT_BRANCH, using commitish:"\
            "$GIT_UPSTREAM_COMMIT_ISH"
        if ! (cd $GIT_LOCAL_TREE && git show-branch $GIT_BRANCH &>/dev/null)
        then
            echo "Error: Branch $GIT_BRANCH not found - please create a remote"\
                "tracking branch of origin/$GIT_BRANCH"
            exit
        fi
# check if we should also do submodule's here as well
        git clone -ls $GIT_LOCAL_TREE $GIT_DIR -b $GIT_BRANCH &>/dev/null
        if ! (cd $GIT_LOCAL_TREE && git remote show upstream &>/dev/null); then
            echo "Remote for upstream git tree not found. Next time add remote"\
                "named upstream for git://git.qemu.org/qemu.git and update"
            (cd $GIT_DIR && git remote add upstream \
                git://git.qemu-project.org/qemu.git)
            (cd $GIT_DIR && git remote update)
        fi
    else
        echo "Processing $GIT_BRANCH branch of remote git tree, using"\
            "commitish: $GIT_UPSTREAM_COMMIT_ISH"
        echo "(For fast processing, consider establishing a local git tree"\
            "at $GIT_LOCAL_TREE)"
        git clone $GIT_TREE $GIT_DIR -b $GIT_BRANCH
        (cd $GIT_DIR && git remote add upstream \
            git://git.qemu-project.org/qemu.git)
        (cd $GIT_DIR && git remote update)
    fi
    QEMU_VERSION=$(cat $GIT_DIR/VERSION)
    SOURCE_VERSION=$OLD_SOURCE_VERSION_AND_EXTRA
    NEW_COMMIT_ISH=
    WRITE_LOG=1
fi

(cd $GIT_DIR && git format-patch -N --suffix= --no-renames -o $CMP_DIR -k \
    --stat=72 --indent-heuristic --zero-commit --no-signature \
    $GIT_UPSTREAM_COMMIT_ISH >/dev/null)

check_patch()
{
    if [ ! -e checkpatch.pl ]; then
        tar Jxf qemu-$SOURCE_VERSION$VERSION_EXTRA.tar.xz \
        qemu-$SOURCE_VERSION/scripts/checkpatch.pl --strip-components=2
    fi
    ./checkpatch.pl --no-tree --terse --no-summary --summary-file --patch $1 >>\
        checkpatch.log || true
}

rm -rf $GIT_DIR

(
    CHANGED_COUNT=0
    UNCHANGED_COUNT=0
    DELETED_COUNT=0
    ADDED_COUNT=0
    TOTAL_COUNT=0

    shopt -s nullglob

    # limit patch base file name to 40 chars ('30' is for path length)
    for i in $CMP_DIR/*; do
        tail -n +2 $i > $CMP_DIR/${i:30:40}.patch
	rm $i
    done

    for i in 0???-*.patch; do
        if [ -e $CMP_DIR/$i ]; then
            if cmp -s $CMP_DIR/$i $i; then
                rm $CMP_DIR/$i
                let UNCHANGED_COUNT+=1
            else
                mv $CMP_DIR/$i .
                check_patch $i
                let CHANGED_COUNT+=1
                let TOTAL_COUNT+=1
            fi
        else
            osc rm --force $i
            echo "  ${i##*/}" >> qemu.changes.deleted
            let DELETED_COUNT+=1
            let TOTAL_COUNT+=1
        fi
    done

    for i in $CMP_DIR/*; do
        mv $i .
        osc add ${i##*/}
        check_patch ${i##*/}
        echo "  ${i##*/}" >> qemu.changes.added
        let ADDED_COUNT+=1
        let TOTAL_COUNT+=1
    done
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

    for package in qemu qemu-linux-user; do
        while IFS= read -r line; do
            if [ "$line" = "PATCH_FILES" ]; then
                for i in 0???-*.patch; do
                    NUM=${i%%-*}
                    echo -e "Patch$NUM:      $i"
                done
            elif [ "$line" = "PATCH_EXEC" ]; then
                for i in 0???-*.patch; do
                    NUM=${i%%-*}
                    echo "%patch$NUM -p1"
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

sed -e 's|^\(Name:.*qemu\)|\1-testsuite|' < qemu.spec > qemu-testsuite.spec
sed -i 's/^# spec file for package qemu/&-testsuite/' qemu-testsuite.spec

if [ "$1" = "-f" ]; then
    if [ "$(rpm -q --queryformat '%{VERSION}' obs-service-format_spec_file)" -lt "20180820" ]; then
        echo "WARNING! Not running osc format-spec-file service - recent obs package needed"
    else
        echo "running osc service to format spec file"
        osc service localrun format_spec_file
    fi
else
    echo "note: not running osc format_spec_file service. If desired, pass -f"
fi

/bin/sh pre_checkin.sh -q

echo "Please remember to run pre_checkin.sh after modifying qemu.changes."
