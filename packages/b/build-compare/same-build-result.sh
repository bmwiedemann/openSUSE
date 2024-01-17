#!/bin/bash
#
# Copyright (c) 2009, 2010, 2012 SUSE Linux Product GmbH, Germany.
# Licensed under GPL v2, see COPYING file for details.
#
# Written by Adrian Schroeter <adrian@suse.de>
# Enhanced by Andreas Jaeger <aj@suse.de>
#
# The script decides if the new build differes from the former one,
# using pkg-diff.sh.
# The script is called as part of the build process as:
# /usr/lib/build/same-build-result.sh /.build.oldpackages /usr/src/packages/RPMS /usr/src/packages/SRPMS

CMPSCRIPT=${0%/*}/pkg-diff.sh
SCMPSCRIPT=${0%/*}/srpm-check.sh

declare -a exit_code
# exit_code[0]='' # binaries_differ
# exit_code[1]='' # rpmlint_differs
# exit_code[2]='' # appdata_differs
# exit_code[3]='' # srcrpm_differs
file1=`mktemp`
file2=`mktemp`
_x() {
  rm -f ${file1} ${file2}
}
trap _x EXIT
#
remove_check_time_report() {
  local f=$1
  awk '
    BEGIN {
      ctr_seen=0;
    }
    /Check time report .*:$/ {
      ctr_seen=1;
      next;
    }
    /TOTAL[[:blank:]]+[0-9]/ {
      if (ctr_seen == 1) {
        ctr_seen=0;
        next;
      }
    }
    {
      if (ctr_seen == 1) {
        next;
      }
      print $0;
    }
  ' < "${f}"
}
#
check_all=
if test "$1" = "-a"
then
  check_all="-a"
  shift
fi
#
OLDDIR="$1"
shift
NEWDIRS="$*"

echo "$CMPSCRIPT"

if [ ! -d "$OLDDIR" ]; then
  echo "No valid directory with old build result given !"
  exit 1
fi
if [ -z "$NEWDIRS" ]; then
  echo "No valid directory with new build result given !"
  exit 1
fi

if test `find $NEWDIRS -name '*.rpm' -and ! -name '*.delta.rpm' | wc -l` != `find $OLDDIR -name '*.rpm' -and ! -name '*.delta.rpm' | wc -l`; then
   echo "different number of subpackages"
   find $OLDDIR  -name '*.rpm' -and ! -name '*.delta.rpm' -print0 | xargs -0 rpm -qp --qf '%{NAME}\n' | sort > ${file1}
   find $NEWDIRS -name '*.rpm' -and ! -name '*.delta.rpm' -print0 | xargs -0 rpm -qp --qf '%{NAME}\n' | sort > ${file2}
   diff -u ${file1} ${file2}
   exit 1
fi

osrpm=$(find "$OLDDIR" -name \*src.rpm)
nsrpm=$(find $NEWDIRS -name \*src.rpm)

if test ! -f "$osrpm"; then
  echo no old source rpm in $OLDDIR
  exit 1
fi

if test ! -f "$nsrpm"; then
  echo no new source rpm in $NEWDIRS
  exit 1
fi

echo "compare $osrpm $nsrpm"
if bash $SCMPSCRIPT $check_all "$osrpm" "$nsrpm"
then
  : src.rpm identical
else
  test -z "${check_all}" && exit 1
  exit_code[3]='srcrpm_differs'
fi

# technically we should not all exclude all -32bit but filter for different archs,
# like done with -x86
# but it would be better if this script ran earlier in the build
# sort the rpms so that both lists have the same order
# problem: a package can contain both noarch and arch subpackages, so we have to 
# take care of proper sorting of NEWRPMS, e.g. noarch/x.rpm and x86_64/w.rpm since OLDRPMS 
# has all the packages in a single directory and would sort this as w.rpm, x.rpm.
find $OLDDIR  -type f -name '*.rpm' \
  -a ! -name '*src.rpm' \
  -a ! -name '*.delta.rpm' \
  -a ! -name '*-32bit-*' \
  -a ! -name '*-64bit-*' \
  -a ! -name '*-x86-*.ia64.rpm' \
  > ${file1}
find $NEWDIRS -type f -name '*.rpm' \
  -a ! -name '*src.rpm' \
  -a ! -name '*.delta.rpm' \
  -a ! -name '*-32bit-*' \
  -a ! -name '*-64bit-*' \
  -a ! -name '*-x86-*.ia64.rpm' \
  > ${file2}
OLDRPMS=($( sort --field-separator=/ --key=` sed -n '1s@[^/]@@gp' ${file1} | wc -c ` ${file1} ))
NEWRPMS=($( sort --field-separator=/ --key=` sed -n '1s@[^/]@@gp' ${file2} | wc -c ` ${file2} ))

# Get version-release from first RPM and keep for rpmlint check
# Remember to quote the "." for future regexes
ver_rel1=$(rpm -qp --nodigest --nosignature --qf "%{VERSION}-%{RELEASE}" "${OLDRPMS[0]}"|sed -e 's/\./\\./g')
ver_rel2=$(rpm -qp --nodigest --nosignature --qf "%{VERSION}-%{RELEASE}" "${NEWRPMS[0]}"|sed -e 's/\./\\./g')

rpmqp='rpm -qp --qf %{NAME} --nodigest --nosignature '
for opac in ${OLDRPMS[*]}; do
  npac=${NEWRPMS[0]}
  NEWRPMS=(${NEWRPMS[@]:1}) # shift
  echo compare "$opac" "$npac"
  oname=`$rpmqp $opac`
  nname=`$rpmqp $npac`
  if test "$oname" != "$nname"; then
    echo "names differ: $oname $nname"
    exit 1
  fi
  case "$opac" in
    *debuginfo*)
      echo "skipping -debuginfo package"
    ;;
    *)
      bash $CMPSCRIPT $check_all "$opac" "$npac" || exit_code[0]='binaries_differ'
    ;;
  esac
done

if [ -n "${NEWRPMS[0]}" ]; then
  echo additional new package
  exit 1
fi

OTHERDIR=
# Compare rpmlint.log files
if test -d /home/abuild/rpmbuild/OTHER; then
  OTHERDIR=/home/abuild/rpmbuild/OTHER
elif test -d /usr/src/packages/OTHER; then
  OTHERDIR=/usr/src/packages/OTHER
else
  for newdir in $NEWDIRS
  do
    test -f "${newdir}/rpmlint.log" || continue
    OTHERDIR="${newdir}"
    break
  done
  test -n "$OTHERDIR" || echo "no OTHERDIR"
fi

if test -n "$OTHERDIR"; then
  old_log=$OLDDIR/rpmlint.log
  new_log=$OTHERDIR/rpmlint.log
  if test -e ${old_log} && test -e ${new_log} ; then
    echo "comparing ${old_log} and ${new_log}"
    # Remove --time-report from rpmlint
    # Sort the files first since the order of messages is not deterministic
    # Remove release from files
    remove_check_time_report ${old_log}|sort -u|sed -e "s,$ver_rel1,@VERSION@-@RELEASE@,g" -e "s|/tmp/rpmlint\..*spec|.spec|g" > $file1
    remove_check_time_report ${new_log}|sort -u|sed -e "s,$ver_rel2,@VERSION@-@RELEASE@,g" -e "s|/tmp/rpmlint\..*spec|.spec|g" > $file2
    # Remove odd warning about not-hardlinked files
    # Remove odd warning about data and time, it comes and goes
    # Remove warning about python mtime mismatch, a republish will not help
    # Remove odd warning about filenames, they contain VERSION-RELEASE
    # Remove durations from progress reports
    # Remove odd output about number of checks and packages
    sed -i -e "
    /: W: files-duplicate /d
    /: W: file-contains-date-and-time /d
    /: W: python-bytecode-inconsistent-mtime /d
    /: W: filename-too-long-for-joliet /d
    /: I: \(filelist-initialization\|check-completed\) /s| [0-9]\+\.[0-9] s| x.x s|
    s/; has taken [0-9]\+\.[0-9] s/; has taken x.x s/
    /^checks: [0-9]\+, packages: [0-9]\+/d
    " $file1 $file2
    if ! cmp -s $file1 $file2; then
      echo "rpmlint.log files differ:"
      diff -u $file1 $file2 |head -n 20
      exit_code[1]='rpmlint_differs'
    fi
    rm $file1 $file2
  else
    if test -e "${new_log}"
    then
      exit_code[1]='rpmlint_new'
      echo "rpmlint.log is new"
    elif test -e "${old_log}"
    then
      exit_code[1]='rpmlint_old'
      echo "rpmlint.log disappeared"
    else
      echo "No rpmlint.log available"
    fi
  fi

  appdatas=$(cd $OTHERDIR && find . -name "*-appdata.xml")
  for xml in $appdatas; do
    # compare appstream data
    if test -e $OLDDIR/$xml && test -e $OTHERDIR/$xml; then
      file1=$OLDDIR/$xml
      file2=$OTHERDIR/$xml
      if ! cmp -s $file1 $file2; then
        echo "$xml files differ:"
        diff -u0 $file1 $file2 |head -n 20
        exit_code[2]='appdata_differs'
      fi
    elif test -e $OTHERDIR/$xml; then
      echo "$xml is new"
      exit_code[2]='appdata_new'
    fi
  done
fi
if test -n "${exit_code[*]}"; then
  exit 1
fi
echo 'compare validated build as identical !'
exit 0
# vim: tw=666 ts=2 shiftwidth=2 et
