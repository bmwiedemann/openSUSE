#! /bin/bash
#
# Copyright (c) 2009, 2010, 2011, 2012 SUSE Linux Product GmbH, Germany.
# Licensed under GPL v2, see COPYING file for details.
#
# Written by Michael Matz and Stephan Coolo
# Enhanced by Andreas Jaeger

# library of functions used by scripts

RPM="rpm -qp --nodigest --nosignature"

declare -a rpm_querytags
collect_rpm_querytags() {
  rpm_querytags=( $(rpm --querytags) )
}
# returns 0 if tag is known, returns 1 if unknown
rpmtag_known() {
  local needle="\<${1}\>"
  local haystack="${rpm_querytags[@]}"
  [[ "${haystack}" =~ ${needle} ]]
  return $?
}

set_rpm_meta_global_variables() {

  local pkg=$1
  local rpm_tags=
  local out=`mktemp`
  local t v qt
  local -a type variant list

# Name, Version, Release
QF_NAME="%{NAME}"
QF_VER_REL="%{VERSION}-%{RELEASE}"
QF_NAME_VER_REL="%{NAME}-%{VERSION}-%{RELEASE}"

QF_PROVIDES=
type=(
  CONFLICT
  OBSOLETE
  OLDSUGGESTS
  PROVIDE
  RECOMMEND
  REQUIRE
  SUGGEST
  SUPPLEMENT
)
variant=(
  NAME
  FLAGS
  VERSION
)
for t in "${type[@]}"
do
  unset list
  list=()
  for v in "${variant[@]}"
  do
    qt="${t}${v}"
    rpmtag_known "${qt}" || continue
    list+=("%{${qt}}")
  done
  QF_PROVIDES+="${t}\\n[${list[@]}\\n]\\n"
done

# don't look at RELEASE, it contains our build number
QF_TAGS="%{NAME} %{VERSION} %{EPOCH}\\n"
QF_TAGS="${QF_TAGS}%{SUMMARY}\\n%{DESCRIPTION}\\n"
# the DISTURL tag can be used as checkin ID
QF_TAGS="${QF_TAGS}%{VENDOR} %{DISTRIBUTION} %{DISTURL}\\n"
QF_TAGS="${QF_TAGS}%{LICENSE}\\n"
QF_TAGS="${QF_TAGS}%{GROUP} %{URL} %{EXCLUDEARCH} %{EXCLUDEOS} %{EXCLUSIVEARCH}\\n"
QF_TAGS="${QF_TAGS}%{EXCLUSIVEOS} %{RPMVERSION} %{PLATFORM}\\n"
QF_TAGS="${QF_TAGS}%{PAYLOADFORMAT} %{PAYLOADCOMPRESSOR} %{PAYLOADFLAGS}\\n"

# XXX We also need to check the existence (but not the content (!))
# of SIGGPG (and perhaps the other SIG*)
# XXX We don't look at triggers
# Only the first ChangeLog entry; should be enough
QF_TAGS="${QF_TAGS}%{CHANGELOGTIME} %{CHANGELOGNAME} %{CHANGELOGTEXT}\\n"

# scripts, might contain release number
QF_SCRIPT=
type=(
  PRETRANS
  PREIN
  POSTIN
  PREUN
  POSTUN
  POSTTRANS
  VERIFYSCRIPT
)
variant=(
  PROG
  FLAGS
  ''
)
for t in "${type[@]}"
do
  unset list
  list=()
  for v in "${variant[@]}"
  do
    qt="${t}${v}"
    rpmtag_known "${qt}" || continue
    list+=("%{${qt}}")
  done
  QF_SCRIPT+="${t}\\n[${list[@]}\\n]\\n"
done

# Now the files. We leave out mtime and size.  For normal files
# the size will influence the MD5 anyway.  For directories the sizes can
# differ, depending on which file system the package was built.  To not
# have to filter out directories we simply ignore all sizes.
# Also leave out FILEDEVICES, FILEINODES (depends on the build host),
# FILECOLORS, FILECLASS (normally useful but file output contains mtimes),
# FILEDEPENDSX and FILEDEPENDSN.
# Also FILELANGS (or?)
QF_FILELIST="[%{FILENAMES} %{FILEFLAGS} %{FILESTATES} %{FILEMODES:octal} %{FILEUSERNAME} %{FILEGROUPNAME} %{FILERDEVS} %{FILEVERIFYFLAGS} %{FILELINKTOS}\n]\\n"
# ??? what to do with FILEPROVIDE and FILEREQUIRE?

QF_CHECKSUM="[%{FILENAMES} %{FILEMD5S} %{FILEFLAGS}\n]\\n"

QF_SOURCERPM="%{SOURCERPM}\\n"

QF_ALL="\n___QF_NAME___\n${QF_NAME}\n___QF_NAME___\n"
QF_ALL="$QF_ALL\n___QF_TAGS___\n${QF_TAGS}\n___QF_TAGS___\n"
QF_ALL="$QF_ALL\n___QF_VER_REL___\n${QF_VER_REL}\n___QF_VER_REL___\n"
QF_ALL="$QF_ALL\n___QF_NAME_VER_REL___\n${QF_NAME_VER_REL}\n___QF_NAME_VER_REL___\n"
QF_ALL="$QF_ALL\n___QF_PROVIDES___\n${QF_PROVIDES}\n___QF_PROVIDES___\n"
QF_ALL="$QF_ALL\n___QF_SCRIPT___\n${QF_SCRIPT}\n___QF_SCRIPT___\n"
QF_ALL="$QF_ALL\n___QF_FILELIST___\n${QF_FILELIST}\n___QF_FILELIST___\n"
QF_ALL="$QF_ALL\n___QF_CHECKSUM___\n${QF_CHECKSUM}\n___QF_CHECKSUM___\n"
QF_ALL="$QF_ALL\n___QF_SOURCERPM___\n${QF_SOURCERPM}\n___QF_SOURCERPM___\n"
}

check_header()
{
   $RPM --qf "$1" "$2"
}

# Trim version-release string:
# - it is used as direntry below certain paths
# - it is assigned to some variable in scripts, at the end of a line
# - it is used in PROVIDES, at the end of a line
#   - special-case KMP package:
#     PROVIDES version_k.*-release at end of line, trim release
#     [   23s] -acpi_call-kmp-default 8 1.2.2_k5.17.0_rc5_1.ga9b2c1d-6.110
#     [   23s] +acpi_call-kmp-default 8 1.2.2_k5.17.0_rc5_1.ga9b2c1d-6.111
# Trim name-version-release string:
# - it is used in update-scripts which are called by libzypp
#   - special-case KMP package:
#     [   64s]  PREIN
#     [   64s]  /bin/sh (none)  /usr/lib/module-init-tools/kernel-scriptlets/kmp-pre --name "acpi_call-kmp-default" \
#     [   64s] -  --version "1.2.2_k5.17.0_rc5_1.ga9b2c1d" --release "6.112" --kernelrelease "5.17.0-rc5-1.ga9b2c1d" \
#     [   64s] +  --version "1.2.2_k5.17.0_rc5_1.ga9b2c1d" --release "6.113" --kernelrelease "5.17.0-rc5-1.ga9b2c1d" \
function trim_release_old()
{
  local rel_regex_l=${version_release_old_regex_l##*-}
  sed -e "
  /\(\/boot\|\/lib\/modules\|\/lib\/firmware\|\/usr\/src\|$version_release_old_regex_l\$\|$version_release_old_regex_l)\)/{s,$version_release_old_regex_l,@VERSION@-@RELEASE_LONG@,g;s,$version_release_old_regex_s,@VERSION@-@RELEASE_SHORT@,g}
  s/\(\/var\/adm\/update-scripts\/\)${name_ver_rel_old_regex_l}\([^[:blank:]]\+\)/\1@NAME_VER_REL@\2/g
  s/\(\/var\/adm\/update-messages\/\)${name_ver_rel_old_regex_l}\([^[:blank:]]\+\)/\1@NAME_VER_REL@\2/g
  s/\(^[^[:blank:]].*-kmp-.*[[:blank:]].*_k.*-\)${rel_regex_l}$/\1@RELEASE_LONG@/g
  s/--release \"${rel_regex_l}\" --kernel/--release \"@RELEASE_LONG@\" --kernel/g
  /\/usr\/lib\/\.build-id/d
  "
}
function trim_release_new()
{
  local rel_regex_l=${version_release_new_regex_l##*-}
  sed -e "
  /\(\/boot\|\/lib\/modules\|\/lib\/firmware\|\/usr\/src\|$version_release_new_regex_l\$\|$version_release_new_regex_l)\)/{s,$version_release_new_regex_l,@VERSION@-@RELEASE_LONG@,g;s,$version_release_new_regex_s,@VERSION@-@RELEASE_SHORT@,g}
  s/\(\/var\/adm\/update-scripts\/\)${name_ver_rel_new_regex_l}\([^[:blank:]]\+\)/\1@NAME_VER_REL@\2/g
  s/\(\/var\/adm\/update-messages\/\)${name_ver_rel_new_regex_l}\([^[:blank:]]\+\)/\1@NAME_VER_REL@\2/g
  s/\(^[^[:blank:]].*-kmp-.*[[:blank:]].*_k.*-\)${rel_regex_l}$/\1@RELEASE_LONG@/g
  s/--release \"${rel_regex_l}\" --kernel/--release \"@RELEASE_LONG@\" --kernel/g
  /\/usr\/lib\/\.build-id/d
  "
}
# Get single directory or filename with long or short release string
function grep_release_old()
{
  grep -E "(/boot|/lib/modules|/lib/firmware|/usr/src|/var/adm/update-scripts)/[^/]*(${version_release_old_regex_l}(\$|[^/]+\$)|${version_release_old_regex_s}(\$|[^/]+\$))"
}
function grep_release_new()
{
  grep -E "(/boot|/lib/modules|/lib/firmware|/usr/src|/var/adm/update-scripts)/[^/]*(${version_release_new_regex_l}(\$|[^/]+\$)|${version_release_new_regex_s}(\$|[^/]+\$))"
}

#usage unpackage <file> $dir
# Unpack files in directory $dir
# like /usr/bin/unpackage - just for one file and with no options
function unpackage()
{
    local file
    local dir
    file=$1
    dir=$2
    mkdir -p $dir
    pushd $dir 1>/dev/null
    case $file in
        *.bz2)
            bzip2 -d $file
            ;;
        *.gz)
            gzip -d $file
            ;;
        *.xz)
            xz -d $file
            ;;
        *.tar|*.tar.bz2|*.tar.gz|*.tgz|*.tbz2)
            tar xf $file
            ;;
        *.rpm)
            CPIO_OPTS="--extract --unconditional --preserve-modification-time --make-directories --quiet"
            rpm2cpio $file | cpio ${CPIO_OPTS}
            ;;
        *.ipk|*.deb)
            ar x $file
            tar xf control.tar.gz
            rm control.tar.gz
            tar xf data.tar.[xg]z
            rm data.tar.[xg]z
            ;;
    esac
    popd 1>/dev/null
}

# Run diff command on the files
# $1: printed info
# $2: file1
# $3: file2
# $4, $5: rpm_meta_old and rpm_meta_new, for cleanup.
function comp_file()
{
    echo "comparing $1"
    if ! diff --label old-$1 --label new-$1 -au $2 $3; then
      if test -z "$check_all"; then
        rm $2 $3 $4 $5
        return 1
      fi
      difffound=1
    fi
    return 0
}

# Get var's value from specfile.
# $1: var name
# $2: specfile
function get_value()
{
    sed -n -e "/^___${1}___/,/^___${1}___/p" $2 | sed -e "/^___${1}___/d"
}

# Set version_release_old_regex_s, version_release_old_regex_l and
# name_ver_rel_old_regex_l, also the new ones.
function set_regex() {
  local rel_old=${version_release_old##*-}
  local rel_new=${version_release_new##*-}

  # Short version without B_CNT
  # release may not contain a dot
  case "${rel_old}" in
    *.*)
    version_release_old_regex_s=${version_release_old%.*}
    ;;
    *)
    version_release_old_regex_s=${version_release_old}
    ;;
  esac
  # Remember to quote the . which is in release
  version_release_old_regex_s=${version_release_old_regex_s//./\\.}
  # Long version with B_CNT
  version_release_old_regex_l=${version_release_old//./\\.}
  name_ver_rel_old_regex_l=${name_ver_rel_old//./\\.}

  case "${rel_new}" in
    *.*)
    version_release_new_regex_s=${version_release_new%.*}
    ;;
    *)
    version_release_new_regex_s=${version_release_new}
    ;;
  esac
  version_release_new_regex_s=${version_release_new_regex_s//./\\.}
  version_release_new_regex_l=${version_release_new//./\\.}
  name_ver_rel_new_regex_l=${name_ver_rel_new//./\\.}
}

# Trim a block starting with a keyword and ending with an empty line
# $1: enable
# $2: keyword
function trim_section() {
  if test "${1}" -gt 0 ; then
    sed -e "/^${2}$/,/^$/d"
  else
    cat
  fi
}

# Compare just the rpm meta data of two rpms
# Returns:
# 0 in case of same content
# 1 in case of errors or difference
# 2 in case of differences that need further investigation
# Sets ${files[@]} array with list of files that need further investigation
function cmp_rpm_meta ()
{
    local RES
    local f
    local sh=$1
    local oldrpm=$2
    local newrpm=$3
    local tmpdir="$(mktemp -d)"
    local file1="$tmpdir/file1"
    local file2="$tmpdir/file2"
    local rpm_meta_old="$tmpdir/rpm-meta-old"
    local rpm_meta_new="$tmpdir/rpm-meta-new"

    collect_rpm_querytags
    set_rpm_meta_global_variables $oldrpm

    check_header "$QF_ALL" $oldrpm > $rpm_meta_old
    check_header "$QF_ALL" $newrpm > $rpm_meta_new

    # rpm returns 0 even in case of error
    if test -s $rpm_meta_old && test -s $rpm_meta_new ; then
      : some output provided, all query tags understood by rpm
    else
      ls -l $rpm_meta_old $rpm_meta_new
      echo "empty 'rpm -qp' output..."
      rm -rf "$tmpdir"
      return 1
    fi

    name_new="$(get_value QF_NAME $rpm_meta_new)"
    version_release_new="$(get_value QF_VER_REL $rpm_meta_new)"
    name_ver_rel_new="$(get_value QF_NAME_VER_REL $rpm_meta_new)"

    version_release_old="$(get_value QF_VER_REL $rpm_meta_old)"
    name_ver_rel_old="$(get_value QF_NAME_VER_REL $rpm_meta_old)"

    set_regex

    # Check the whole spec file at first, return 0 immediately if they
    # are the same.
    trim_release_old < $rpm_meta_old > $file1
    trim_release_new < $rpm_meta_new > $file2
    echo "comparing the rpm tags of $name_new"
    if diff --speed-large-files --label old-rpm-tags --label new-rpm-tags -au0 $file1 $file2; then
      rm -rf "$tmpdir"
      return 0
    fi

    get_value QF_TAGS $rpm_meta_old > $file1
    get_value QF_TAGS $rpm_meta_new > $file2
    if ! comp_file rpmtags $file1 $file2 $rpm_meta_old $rpm_meta_new; then
      rm -rf "$tmpdir"
      return 1
    fi

    # This might happen when?!
    echo "comparing RELEASE"
    if [ "${version_release_old%.*}" != "${version_release_new%.*}" ] ; then
      case $name_new in
        kernel-*)
          # Make sure all kernel packages have the same %RELEASE
          echo "release prefix mismatch"
          if test -z "$check_all"; then
            rm -rf "$tmpdir"
            return 1
          fi
          difffound=1
          ;;
        # Every other package is allowed to have a different RELEASE
        *) ;;
      esac
    fi

    # Built packages provide the sourcerpm, for the sourcerpm itself it is "(none)"
    [ "x$(get_value QF_SOURCERPM $rpm_meta_new)" == "x(none)" ] && is_sourcerpm=1 || is_sourcerpm=0

    # FIXME: PROVIDE needs to be handled independent from the other tags
    get_value QF_PROVIDES $rpm_meta_old | trim_section ${is_sourcerpm} 'PROVIDE' | trim_release_old | sort > $file1
    get_value QF_PROVIDES $rpm_meta_new | trim_section ${is_sourcerpm} 'PROVIDE' | trim_release_new | sort > $file2
    if ! comp_file PROVIDES $file1 $file2 $rpm_meta_old $rpm_meta_new; then
      rm -rf "$tmpdir"
      return 1
    fi

    get_value QF_SCRIPT $rpm_meta_old | trim_release_old > $file1
    get_value QF_SCRIPT $rpm_meta_new | trim_release_new > $file2
    if ! comp_file scripts $file1 $file2 $rpm_meta_old $rpm_meta_new; then
      rm -rf "$tmpdir"
      return 1
    fi

    # First check the file attributes and later the md5s
    get_value QF_FILELIST $rpm_meta_old | trim_release_old > $file1
    get_value QF_FILELIST $rpm_meta_new | trim_release_new > $file2
    if ! comp_file filelist $file1 $file2 $rpm_meta_old $rpm_meta_new; then
      rm -rf "$tmpdir"
      return 1
    fi

    # now the md5sums. if they are different, we check more detailed
    # if there are different filenames, we will already have aborted before
    # file flag 64 means "ghost", filter those out.
    get_value QF_CHECKSUM $rpm_meta_old | grep -v " 64$" | trim_release_old > $file1
    get_value QF_CHECKSUM $rpm_meta_new | grep -v " 64$" | trim_release_new > $file2
    RES=2
    # done if the same
    files=()
    echo "comparing file checksum"
    if cmp -s $file1 $file2; then
      RES=0
    else
      # Get only files with different MD5sums
      while read
      do
        : "${REPLY}"
        files+=( "${REPLY}" )
      done < <(diff -U0 $file1 $file2 | sed --regexp-extended -n -e '/^\+\//{s/^\+//;s/ [0-9a-f]+ [0-9]+$//;p}')
    fi

    if test -n "$sh"; then
      echo "creating rename script"
      # Create a temporary helper script to rename files/dirs with release in it
      for f in `$RPM --qf '[%{FILENAMES} %{FILEFLAGS}\n]\n' "$oldrpm" | grep_release_old | grep -vw 64$ | awk '{ print $1}'`
      do
        echo mv -v \"old/${f}\" \"old/`echo ${f} | trim_release_old`\"
      done >> "${sh}"
      #
      for f in `$RPM --qf '[%{FILENAMES} %{FILEFLAGS}\n]\n' "$newrpm" | grep_release_new | grep -vw 64$ | awk '{ print $1}'`
      do
        echo mv -v \"new/${f}\" \"new/`echo ${f} | trim_release_new`\"
      done >> "${sh}"
    fi

    rm -rf "$tmpdir"
    [ "$difffound" = 1 ] && RES=1
    return $RES
}

function adjust_controlfile() {
    version_release_old="`sed -ne 's/^Version: \(.*\)/\1/p' $1/control`"
    name_ver_rel_old="`sed -n -e 's/^Package: \(.*\)/\1/p' $1/control`-`sed -n -e 's/^Version: \(.*\)/\1/p' $1/control`"
    version_release_new="`sed -ne 's/^Version: \(.*\)/\1/p' $2/control`"
    name_ver_rel_new="`sed -n -e 's/^Package: \(.*\)/\1/p' $2/control`-`sed -n -e 's/^Version: \(.*\)/\1/p' $2/control`"
    set_regex
    trim_release_old < $1/control > $1/control.fixed
    mv $1/control.fixed $1/control
    trim_release_new < $2/control > $2/control.fixed
    mv $2/control.fixed $2/control
}


# vim: tw=666 ts=2 shiftwidth=2 et
