#! /bin/bash
#
# Copyright (c) 2009, 2010, 2011, 2012 SUSE Linux Product GmbH, Germany.
# Licensed under GPL v2, see COPYING file for details.
#
# Written by Michael Matz and Stephan Coolo
# Enhanced by Andreas Jaeger
declare -i watchdog_host_timeout_seconds='3600'
declare -i watchdog_touch_percent_prior_timeout='25'
declare -i watchdog_next_touch_seconds=0

function watchdog_reset
{
  local uptime idle
  local -i next_touch now

  read uptime idle < /proc/uptime

  now="${uptime%.*}"
  next_touch=$(( ${now} + ( (${watchdog_host_timeout_seconds} * ${watchdog_touch_percent_prior_timeout}) / 100 ) ))
  watchdog_next_touch_seconds=${next_touch}
}

function watchdog_touch
{
  local uptime idle
  local -i next_touch now

  read uptime idle < /proc/uptime

  now="${uptime%.*}"
  if test "${now}" -lt "${watchdog_next_touch_seconds}"
  then
    return
  fi
  echo 'build-compare touching host-watchdog.'
  watchdog_reset
}

function wprint
{
  echo "$@"
  watchdog_reset
}

filter_disasm()
{
  [[ $nofilter ]] && return
  sed -e '
    s/^ *[0-9a-f]\+://
    s/\$0x[0-9a-f]\+/$something/
    s/callq *[0-9a-f]\+/callq /
    s/# *[0-9a-f]\+/#  /
    s/\(0x\)\?[0-9a-f]\+(/offset(/
    s/[0-9a-f]\+ </</
    s/^<\(.*\)>:/\1:/
    s/<\(.*\)+0x[0-9a-f]\+>/<\1 + ofs>/
  ' 
}

filter_xenefi() {
   # PE32+ executable (EFI application) x86-64 (stripped to external PDB), for MS Windows
   perl -e "open fh, '+<', '$f'; seek fh, 0x80 + 0x08, SEEK_SET; print fh 'time'; seek fh, 0x80 + 0x58, SEEK_SET; print fh 'chck';"
}

filter_pyc() {
   perl -e "open fh, '+<', '$f'; seek fh, 4, SEEK_SET; print fh '0000';"
}

filter_dvi() {
   # Opcodes 247: pre; i[1], num[4], den[4], mag[4], k[1], x[k]
   perl -e "
   my \$rec;
   open fh, '+<', '$f';
   my \$dummy = read fh, \$rec, 15;
   (\$pre, \$i, \$num, \$den, \$mag, \$k) = unpack('C2 N3 C', \$rec);
   seek fh, 15, SEEK_SET;
   while (\$k > 0) {
     print fh '0';
     \$k--;
   }
   "
}

filter_png() {
   convert "$f" +set date:create +set date:modify "${f}.$PPID.$$"
   mv -f "${f}.$PPID.$$" "${f}"
}

filter_emacs_lisp() {
   sed -i -e '
    s|^;;; .ompiled by abuild@.* on ... ... .. ..:..:.. ....|;;; compiled by abuild@buildhost on Wed Jul 01 00:00:00 2009|
    s|^;;; from file .*\.el|;;; from file /home/abuild/rpmbuild/BUILD/anthy-9100h/src-util/elc.8411/anthy-azik.el|
    s|^;;; emacs version .*|;;; emacs version 21.5  (beta34) "kale" XEmacs Lucid.|
    s|^;;; bytecomp version .*|;;; bytecomp version 2.28 XEmacs; 2009-08-09.|
    ' "$f"
}

filter_pdf() {
   # PDF files contain a unique ID, remove it
   # Format of the ID is:
   # /ID [<9ACE247A70CF9BEAFEE15E116259BD6D> <9ACE247A70CF9BEAFEE15E116259BD6D>]
   # with optional spaces. pdftex creates also:
   # /CreationDate (D:20120103083206Z)
   # /ModDate (D:20120103083206Z)
   # and possibly XML metadata as well
   sed -i \
        '/obj/,/endobj/{
           s%/ID \?\[ \?<[^>]\+> \?<[^>]\+> \?\]%/IDrandom%g;
           s%/CreationDate \?(D:[^)]*)%/CreationDate (D: XXX)%g;
           s%/ModDate \?(D:[^)]*)%/ModDate (D: XXX)%g;
           s%<pdf:CreationDate>[^<]*</pdf:CreationDate>%<pdf:CreationDate>XXX</pdf:CreationDate>%g;
           s%<pdf:ModDate>[^<]*</pdf:ModDate>%<pdf:ModDate>XXX</pdf:ModDate>%g;
           s%<xap:CreateDate>[^<]*</xap:CreateDate>%<xap:CreateDate>XXX</xap:CreateDate>%g;
           s%<xap:ModifyDate>[^<]*</xap:ModifyDate>%<xap:ModifyDate>XXX</xap:ModifyDate>%g;
           s%<xap:MetadataDate>[^<]*</xap:MetadataDate>%<xap:MetadataDate>XXX</xap:MetadataDate>%g;
        }' "$f"
}

filter_ps() {
   sed -i -e '
    /^%%CreationDate:[[:blank:]]/d
    /^%%Creator:[[:blank:]]groff[[:blank:]]version[[:blank:]]/d
    /^%DVIPSSource:[[:blank:]]/d
   ' "$f"
}

filter_mo() {
   sed -i -e "s,POT-Creation-Date: ....-..-.. ..:..+....,POT-Creation-Date: 1970-01-01 00:00+0000," "$f"
}

filter_linuxrc_config() {
   sed -i '/^InitrdID:/s@^.*@InitrdID: something@' "$f"
}

# call specified filter on old and new file
filter_generic()
{
   filtertype=$1
   [[ $nofilter ]] && return
   local f
   for f in "old/$file" "new/$file" ; do
      eval "filter_$filtertype $f"
   done
}

# returns 0 if both files are identical
# returns 1 if files differ or one is missing
# returns 2 if files must be processed further
verify_before_processing()
{
  local file="$1"
  local cmpout="$2"

  if test ! -e "old/$file"; then
    wprint "Missing in old package: $file"
    return 1
  fi
  if test ! -e "new/$file"; then
    wprint "Missing in new package: $file"
    return 1
  fi

  # consider only files and symlinks
  if test ! -f "old/$file"; then
    return 0
  fi
  if test ! -f "new/$file"; then
    return 0
  fi

  if cmp -b "old/$file" "new/$file" > "${cmpout}" ; then
    return 0
  fi

  if test -s "${cmpout}" ; then
    # cmp produced output for futher processing
    return 2
  fi

  # cmp failed
  return 1
}

diff_two_files()
{
  local offset length

  verify_before_processing "${file}" "${dfile}"
  case "$?" in
    0) return 0 ;;
    1) return 1 ;;
    *) ;;
  esac

  offset=`sed 's@^.*differ: byte @@;s@,.*@@' < $dfile`
  wprint "$file differs at offset '$offset' ($ftype)"
  offset=$(( ($offset >> 6) << 6 ))
  length=512
  diff -u \
    <( hexdump -C -s $offset -n $length "old/$file" ) \
    <( hexdump -C -s $offset -n $length "new/$file" ) | $buildcompare_head
  return 1
}

trim_man_first_line()
{
    # Handles the first line if it is like:
    #.\" Automatically generated by Pod::Man 2.28 (Pod::Simple 3.28)
    #.\" Automatically generated by Pandoc 2.9.2.1
    #.\" DO NOT MODIFY THIS FILE!  It was generated by help2man 1.43.3.
    local f=$1
    [[ $nofilter ]] && return
    sed -i -e '1{
    s|^\.\\"[[:blank:]]\+Automatically[[:blank:]]generated[[:blank:]]by[[:blank:]].*|.\\" Automatically generated by SomeTool|
    s|^\.\\"[[:blank:]]\+DO[[:blank:]]NOT[[:blank:]]MODIFY[[:blank:]]THIS[[:blank:]]FILE![[:blank:]]\+It[[:blank:]]was[[:blank:]]generated[[:blank:]]by[[:blank:]]help2man[[:blank:]].*|.\\" Overly verbose help2man|
    }' $f
}

trim_man_TH()
{
    # Handles lines like:
    # .TH debhelper 7 "2010-02-27" "7.4.15" "Debhelper"
    # .TH DIRMNGR-CLIENT 1 2010-02-27 "Dirmngr 1.0.3" "GNU Privacy Guard"
    # .TH ccmake 1 "March 06, 2010" "ccmake 2.8.1-rc3"
    # .TH QEMU-IMG 1 "2010-03-14" " " " "
    # .TH kdecmake 1 "May 07, 2010" "cmake 2.8.1"
    # .TH "appender.h" 3 "12 May 2010" "Version 1.2.1" "log4c" \" -*- nroff -*-
    # .TH "appender.h" 3 "Tue Aug 31 2010" "Version 1.2.1" "log4c" \" -*- nroff -*-
    # .TH "OFFLINEIMAP" "1" "11 May 2010" "John Goerzen" "OfflineIMAP Manual"
    # .TH gv 3guile "13 May 2010"
    #.TH "GIT\-ARCHIMPORT" "1" "09/13/2010" "Git 1\&.7\&.1" "Git Manual"
    # .TH LDIRECTORD 8 "2010-10-20" "perl v5.12.2" "User Contributed Perl Documentation"
    # .TH ccmake 1 "February 05, 2012" "ccmake 2.8.7"
    # .TH "appender.h" 3 "Tue Aug 31 2010" "Version 1.2.1" "log4c" \" -*- nroff -*-
    # .TH ARCH "1" "September 2010" "GNU coreutils 8.5" "User Commands"
    # .TH "GCM-CALIBRATE" "1" "03 February 2012" "" ""
    #.TH Locale::Po4a::Xml.pm 3pm "2015-01-30" "Po4a Tools" "Po4a Tools"
    local f=$1
    [[ $nofilter ]] && return
    # (.TH   quoted section) (quoted_date)(*)
    sed -i -e 's|^\([[:blank:]]*\.TH[[:blank:]]\+"[^"]\+"[[:blank:]]\+[^[:blank:]]\+\)[[:blank:]]\+\("[^"]\+"\)\([[:blank:]]\+.*\)\?|\1 "qq2000-01-01"\3|' $f
    # (.TH unquoted section) (quoted_date)(*)
    sed -i -e 's|^\([[:blank:]]*\.TH[[:blank:]]\+[^"][^[:blank:]]\+[[:blank:]]\+[^[:blank:]]\+\)[[:blank:]]\+\("[^"]\+"\)\([[:blank:]]\+.*\)\?|\1 "uq2000-02-02"\3|' $f
    # (.TH   quoted section) (unquoted_date)(*)
    sed -i -e 's|^\([[:blank:]]*\.TH[[:blank:]]\+"[^"]\+"[[:blank:]]\+[^[:blank:]]\+\)[[:blank:]]\+\([^"][^[:blank:]]\+\)\([[:blank:]]\+.*\)\?|\1 qu2000-03-03\3|' $f
    # (.TH unquoted section) (unquoted_date)(*)
    sed -i -e 's|^\([[:blank:]]*\.TH[[:blank:]]\+[^"][^[:blank:]]\+[[:blank:]]\+[^[:blank:]]\+\)[[:blank:]]\+\([^"][^[:blank:]]\+\)\([[:blank:]]\+.*\)\?|\1 uu2000-04-04\3|' $f
}

strip_numbered_anchors()
{
  # Remove numbered anchors on Docbook / HTML files.
  #  <a id="idp270624" name=
  #  "idp270624"></a>
  # <a href="#ftn.id32751" class="footnote" id="id32751">
  # <a href="#id32751" class="para">
  # <a href="#tex">1 TeX</a>
  # <a href="dh-manual.html#id599116">
  # <a id="id479058">
  # <div id="ftn.id43927" class="footnote">
  # <div class="section" id="id46">

  [[ $nofilter ]] && return
  for f in old/$file new/$file; do
    sed -ie '
      1 {
      : N
        $ {
          s@\(<a[^>]\+id=\n\?"\)\(id[a-z0-9]\+\)\("[^>]*>\)@\1a_idN\3@g
          s@\(<a[^>]\+name=\n\?"\)\(id[a-z0-9]\+\)\("[^>]*>\)@\1a_nameN\3@g
          s@\(<a[^>]\+href="#\)\([^"]\+\)\("[^>]*>\)@\1href_anchor\3@g
          s@\(<a[^>]\+href="[^#]\+#\)\([^"]\+\)\("[^>]*>\)@\1href_anchor\3@g
          s@\(<div[^>]\+id="\)\([\.a-z0-9]\+\)\("[^>]*>\)@\1div_idN\3@g
        }
      N
      b N
      }' $f &
  done
  wait
}


check_compressed_file()
{
  local file=$1
  local ext=$2
  local tmpdir=`mktemp -d`
  local ftype
  local ret=0
  wprint "$ext file with odd filename: $file"
  if test -n "$tmpdir"; then
    mkdir $tmpdir/{old,new}
    cp --parents --dereference old/$file $tmpdir/
    cp --parents --dereference new/$file $tmpdir/
    if pushd $tmpdir > /dev/null ; then
      case "$ext" in
        bz2)
          mv old/$file{,.bz2}
          mv new/$file{,.bz2}
          bzip2 -d old/$file.bz2 &
          bzip2 -d new/$file.bz2 &
          wait
          ;;
        gzip)
          mv old/$file{,.gz}
          mv new/$file{,.gz}
          gzip -d old/$file.gz &
          gzip -d new/$file.gz &
          wait
          ;;
        xz)
          mv old/$file{,.xz}
          mv new/$file{,.xz}
          xz -d old/$file.xz &
          xz -d new/$file.xz &
          wait
          ;;
      esac
      ftype=`/usr/bin/file old/$file | sed 's@^[^:]\+:[[:blank:]]*@@'`
      case $ftype in
        POSIX\ tar\ archive)
          wprint "$ext content is: $ftype"
          mv old/$file{,.tar}
          mv new/$file{,.tar}
          if ! check_single_file ${file}.tar; then
            ret=1
          fi
          ;;
        ASCII\ cpio\ archive\ *)
          wprint "$ext content is: $ftype"
          mv old/$file{,.cpio}
          mv new/$file{,.cpio}
          if ! check_single_file ${file}.cpio; then
            ret=1
          fi
          ;;
        fifo*pipe*)
          ftype_new="`/usr/bin/file new/$file | sed -e 's@^[^:]\+:[[:blank:]]*@@' -e 's@[[:blank:]]*$@@'`"
          if [ "$ftype_new" != "$ftype"  ]; then
            ret=1
          fi
          ;;
        *)
          wprint "unhandled $ext content: $ftype"
          if ! diff_two_files; then
            ret=1
          fi
          ;;
      esac
      popd > /dev/null
    fi
    rm -rf "$tmpdir"
  fi
  return $ret
}

# returns 0 if file should be skipped
file_is_on_ignorelist()
{
  local file="$1"
  local ret=0

  case "${file}" in
    # Just debug information, we can skip them
    *.exe.mdb|*.dll.mdb) ;;

    # binary dump of TeX and Metafont formats, we can ignore them for good
    /var/lib/texmf/web2c/*/*fmt|\
    /var/lib/texmf/web2c/metafont/*.base|\
    /var/lib/texmf/web2c/metapost/*.mem) ;;

    # ruby documentation, file just contains a timestamp and nothing else
    */created.rid) ;;

    # R binary cache of DESCRIPTION
    /usr/lib*/R/library/*/Meta/package.rds) ;;

    # binary cache of interpreted R code
    /usr/lib*/R/library/*/R/*.rd[bx]) ;;

    # LibreOffice log file
    /usr/lib/libreoffice/solver/inc/*/deliver.log) ;;

    # packaged by libguestfs
    */ld.so.cache|*/etc/machine-id) ;;

    # everything else will be processed
    *) ret=1 ;;
  esac

  return ${ret}
}

# void
normalize_file()
{
  local file="$1"
  local f

  case "$file" in
    *.spec)
      sed -i -e "s,Release:.*$release1,Release: @RELEASE@," "old/$file"
      sed -i -e "s,Release:.*$release2,Release: @RELEASE@," "new/$file"
      ;;
    */xen*.efi)
      filter_generic xenefi
      ;;
    *.pyc|*.pyo)
      filter_generic pyc
      ;;
    *.dvi)
      filter_generic dvi
      ;;
    *png)
      # Try to remove timestamps, only if convert from ImageMagick is installed
      if [[ $(type -p convert) ]]; then
        filter_generic png
      fi
      ;;
    /usr/share/locale/*/LC_MESSAGES/*.mo|\
    /usr/share/locale-bundle/*/LC_MESSAGES/*.mo|\
    /usr/share/vdr/locale/*/LC_MESSAGES/*.mo)
      filter_generic mo
    ;;
    */rdoc/files/*.html)
      # ruby documentation
      # <td>Mon Sep 20 19:02:43 +0000 2010</td>
      for f in old/$file new/$file; do
        sed -i -e 's%<td>[A-Z][a-z][a-z] [A-Z][a-z][a-z] [0-9]\+ [0-9]\+:[0-9]\+:[0-9]\+ +0000 201[0-9]</td>%<td>Mon Sep 20 19:02:43 +0000 2010</td>%g' $f
      done
      strip_numbered_anchors
    ;;
    /usr/share/doc/HTML/*/*/index.cache|\
    /usr/share/doc//HTML/*/*/*/index.cache|\
    /usr/share/doc/kde/HTML/*/*/index.cache|\
    /usr/share/doc/kde/HTML/*/*/*/index.cache|\
    /usr/share/gtk-doc/html/*/*.html|\
    /usr/share/gtk-doc/html/*/*.devhelp2)
      # various kde and gtk packages
      strip_numbered_anchors
      for f in old/$file new/$file; do
        sed -i -e '
          /^<head>/{
            : next
            n
            /^<\/head>/{
            b end_head
            }
            s/^<meta name="generator" content="[^"]\+">/<meta name="generator" content="GTK-Doc V1.29 (XML mode)">/
            b next
          }
          : end_head
          ' $f
      done
    ;;
    /usr/share/doc/packages/*/*.html|\
    /usr/share/doc/packages/*/*/*.html|\
    /usr/share/doc/*/html/*.html|\
    /usr/share/doc/kde/HTML/*/*/*.html)
      for f in old/$file new/$file; do
        sed -i -e '
          s|META NAME="Last-modified" CONTENT="[^"]\+"|META NAME="Last-modified" CONTENT="Thu Mar  3 10:32:44 2016"|
          s|<!-- Created on [^,]\+, [0-9]\+ [0-9]\+ by texi2html [0-9\.]\+ -->|<!-- Created on July, 14 2015 by texi2html 1.78 -->|
          s|<!-- Created on [^,]\+, [0-9]\+ by texi2html [0-9\.]\+$|<!-- Created on October 1, 2015 by texi2html 5.0|
          s|^<!-- Created on .*, 20.. by texi2html .\...|<!-- Created on August 7, 2009 by texi2html 1.82|
          s|This document was generated by <em>Autobuild</em> on <em>[^,]\+, [0-9]\+ [0-9]\+</em> using <a href="http://www.nongnu.org/texi2html/"><em>texi2html [0-9\.]\+</em></a>.|This document was generated by <em>Autobuild</em> on <em>July, 15 2015</em> using <a href="http://www.nongnu.org/texi2html/"><em>texi2html 1.78</em></a>.|
          s|^ *This document was generated by <em>Autobuild</em> on <em>.*, 20..</em> using <a href="http://www.nongnu.org/texi2html/"><em>texi2html .\...</em></a>.$|  This document was generated by <em>Autobuild</em> on <em>August 7, 2009</em> using <a href="http://www.nongnu.org/texi2html/"><em>texi2html 1.82</em></a>.|
          s|^ *This document was generated on <i>[a-zA-Z]\+ [0-9]\+, [0-9]\+</i> using <a href="http://www.nongnu.org/texi2html/"><i>texi2html [0-9\.]\+</i></a>.|  This document was generated on <i>October 1, 2015</i> using <a href="http://www.nongnu.org/texi2html/"><i>texi2html 5.0</i></a>.|
          s|Generated on ... ... [0-9]* [0-9]*:[0-9][0-9]:[0-9][0-9] 20[0-9][0-9] for |Generated on Mon May 10 20:45:00 2010 for |
          s|Generated on ... ... [0-9]* 20[0-9][0-9] [0-9]*:[0-9][0-9]:[0-9][0-9] for |Generated on Mon May 10 20:45:00 2010 for |
          ' $f
      done
      strip_numbered_anchors
    ;;
    /usr/*/javadoc/*.html)
      strip_numbered_anchors
      # There are more timestamps in html, so far we handle only some primitive versions.
      for f in old/$file new/$file; do
        # Javadoc:
        # <head>
        # <!-- Generated by javadoc (version 1.7.0_75) on Tue Feb 03 02:20:12 GMT 2015 -->
        # <!-- Generated by javadoc on Tue Feb 03 00:02:48 GMT 2015 -->
        # <!-- Generated by javadoc (1.8.0_72) on Thu Mar 03 12:50:28 GMT 2016 -->
        # <!-- Generated by javadoc (10-internal) on Wed Feb 07 06:33:41 GMT 2018 -->
        # <meta name="dc.created" content="2019-02-07">
        # <meta name="date" content="2015-02-03">
        # </head>
        sed -i -e '
          /^<head>/{
            : next
            n
            /^<\/head>/{
            b end_head
            }
            s/^<!-- Generated by javadoc ([0-9._]\+) on ... ... .. ..:..:.. \(GMT\|UTC\) .... -->/<!-- Generated by javadoX (1.8.0_72) on Thu Mar 03 12:50:28 GMT 2016 -->/
            t next
            s/^\(<!-- Generated by javadoc\) \((\(build\|version\) [0-9._]\+) on ... ... .. ..:..:.. \(GMT\|UTC\) ....\) \(-->\)/\1 some-date-removed-by-build-compare \5/
            t next
            s/^\(<!-- Generated by javadoc\) ([0-9._]\+-internal) on ... ... .. ..:..:.. \(GMT\|UTC\) .... \(-->\)/\1 some-date-removed-by-build-compare \3/
            t next
            s/^\(<!-- Generated by javadoc\) \(on ... ... .. ..:..:.. \(GMT\|UTC\) ....\) \(-->\)/\1 some-date-removed-by-build-compare \3/
            t next
            s/^<meta name="dc.created" content="[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}">/<meta name="dc.created" content="some-date-removed-by-build-compare">/
            t next
            s/^<meta name="date" content="[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}">/<meta name="date" content="some-date-removed-by-build-compare">/
            b next
          }
          : end_head
          s%Generated by Gjdoc HtmlDoclet [0-9,.]*, part of <a href="http://www.gnu.org/software/classpath/cp-tools/" title="" target="_top">GNU Classpath Tools</a>, on .*, 20.. [0-9]*:..:.. \(a\|p\)\.m\. GMT.%Generated by Gjdoc.%
          s%<!DOCTYPE html PUBLIC "-//gnu.org///DTD XHTML 1.1 plus Target 1.0//EN"\(.*\)GNU Classpath Tools</a>, on [A-Z][a-z]* [0-9]*, 20?? [0-9]*:??:?? \(a|p\)\.m\. GMT.</p>%<!DOCTYPE html PUBLIC "-//gnu.org///DTD XHTML 1.1 plus Target 1.0//EN"\1GNU Classpath Tools</a>, on January 1, 2009 0:00:00 a.m. GMT.</p>%
          s%<!DOCTYPE html PUBLIC "-//gnu.org///DTD\(.*GNU Classpath Tools</a>\), on [a-zA-Z]* [0-9][0-9], 20.. [0-9]*:..:.. \(a\|p\)\.m\. GMT.</p>%<!DOCTYPE html PUBLIC "-//gnu.org///DTD\1,on May 1, 2010 1:11:42 p.m. GMT.</p>%
          ' $f
        # deprecated-list is randomly ordered, sort it for comparison
        case $f in
          */deprecated-list.html)
            [[ $nofilter ]] || sort -o $f $f
          ;;
        esac
      done
    ;;
    /usr/share/javadoc/gjdoc.properties|\
    /usr/share/javadoc/*/gjdoc.properties)
      for f in old/$file new/$file; do
        sed -i -e 's|^#[A-Z][a-z]\{2\} [A-Z][a-z]\{2\} [0-9]\{2\} ..:..:.. GMT 20..$|#Fri Jan 01 11:27:36 GMT 2009|' $f
      done
    ;;
    */fonts.scale|\
    */fonts.dir|\
    */encodings.dir)
      for f in old/$file new/$file; do
        # sort files before comparing
        [[ $nofilter ]] || sort -o $f $f
      done
      ;;
    /var/adm/perl-modules/*)
      for f in old/$file new/$file; do
        sed -i -e 's|^=head2 ... ... .. ..:..:.. ....: C<Module>|=head2 Wed Jul  1 00:00:00 2009: C<Module>|' $f
      done
      ;;
    /usr/share/man/man3/*3pm)
      for f in old/$file new/$file; do
        sed -i -e 's| 3 "20..-..-.." "perl v5....." "User Contributed Perl Documentation"$| 3 "2009-01-01" "perl v5.10.0" "User Contributed Perl Documentation"|' $f
        trim_man_TH $f
        trim_man_first_line $f
      done
      ;;
    */share/man/*|\
    /usr/lib/texmf/doc/man/*/*)
      for f in old/$file new/$file; do
        trim_man_TH $f
        trim_man_first_line $f
        # generated by docbook xml:
        #.\"      Date: 09/13/2010
        sed -i -e 's|Date: [0-1][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]|Date: 09/13/2010|' $f
      done
      ;;
    *.elc)
      filter_generic emacs_lisp
      ;;
    */libtool)
      for f in old/$file new/$file; do
        sed -i -e 's|^# Libtool was configured on host [A-Za-z0-9]*:$|# Libtool was configured on host x42:|' $f
      done
      ;;
    /etc/mail/*cf|\
    /etc/sendmail.cf)
      # from sendmail package
      for f in old/$file new/$file; do
        # - ##### built by abuild@build33 on Thu May 6 11:21:17 UTC 2010
        sed -i -e 's|built by abuild@[a-z0-9]* on ... ... [0-9]* [0-9]*:[0-9][0-9]:[0-9][0-9] .* 20[0-9][0-9]|built by abuild@build42 on Thu May 6 11:21:17 UTC 2010|' $f
      done
      ;;
    /usr/lib*/R/library/*/DESCRIPTION)
      # Simulate R CMD INSTALL --built-timestamp=''
      # Built: R 3.6.1; x86_64-suse-linux-gnu; 2019-08-13 04:19:49 UTC; unix
      sed -i -e 's|\(Built: [^;]*; [^;]*; \)20[0-9][0-9]-[01][0-9]-[0123][0-9] [012][0-9]:[0-5][0-9]:[0-5][0-9] UTC\(; .*\)$|\1\2|' old/$file new/$file
      ;;
    */Linux*Env.Set.sh)
      # LibreOffice files, contains:
      # Generated on: Mon Apr 18 13:19:22 UTC 2011
      for f in old/$file new/$file; do
        sed -i -e 's%^# Generated on:.*UTC 201[0-9] *$%# Generated on: Sometime%g' $f
      done
      ;;
    /var/adm/update-messages/*|\
    /var/adm/update-scripts/*)
      # fetchmsttfonts embeds the release number in the update shell script.
      sed -i "s/${name_ver_rel_old_regex_l}/@NAME_VER_REL@/" old/$file
      sed -i "s/${name_ver_rel_new_regex_l}/@NAME_VER_REL@/" new/$file
      ;;
    *.ps)
      filter_generic ps
      ;;
    *pdf)
      filter_generic pdf
      ;;
    */linuxrc.config)
      filter_generic linuxrc_config
      ;;
    */etc/hosts)
      # packaged by libguestfs
      sed -i 's/^127.0.0.1[[:blank:]].*/127.0.0.1 hst/' "old/$file"
      sed -i 's/^127.0.0.1[[:blank:]].*/127.0.0.1 hst/' "new/$file"
      ;;
  esac
}

archive_a()
{
  local cmd=$1
  local file=$2
  case "${cmd}" in
  f)
    test -x "$(type -P ar)" && return 0
    echo "ERROR: ar missing for ${file}"
    return 1
  ;;
  l)
    ar t "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  x)
    ar x "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  esac
}

archive_cpio()
{
  local cmd=$1
  local file=$2
  case "${cmd}" in
  f)
    test -x "$(type -P cpio)" && return 0
    echo "ERROR: cpio missing for ${file}"
    return 1
  ;;
  l)
    cpio --quiet --list --force-local < "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  x)
    cpio --quiet --extract --force-local < "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  esac
}

archive_squashfs()
{
  local cmd=$1
  local file=$2
  case "${cmd}" in
  f)
    test -x "$(type -P unsquashfs)" && return 0
    echo "ERROR: unsquashfs missing for ${file}"
    return 1
  ;;
  l)
    unsquashfs -no-progress -ls -dest '' "${file}" | grep -Ev '^(Parallel unsquashfs:|[0-9]+ inodes )'
    test "$?" = "0" && return 0
    return 1
  ;;
  x)
    unsquashfs -no-progress -dest "." "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  esac
}

archive_tar()
{
  local cmd=$1
  local file=$2
  case "${cmd}" in
  f)
    test -x "$(type -P tar)" && return 0
    echo "ERROR: tar missing for ${file}"
    return 1
  ;;
  l)
    tar tf "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  x)
    tar xf "${file}"
    test "$?" = "0" && return 0
    return 1
  ;;
  esac
}

UNJAR=
archive_zip()
{
  local cmd=$1
  local file=$2
  case "${cmd}" in
  f)
    if test -x "$(type -P fastjar)"
     then
      UNJAR="${_}"
    elif test -x "$(type -P jar)"
    then
      UNJAR="${_}"
    elif test -x "$(type -P unzip)"
    then
      UNJAR="${_}"
    else
      echo "ERROR: jar/fastjar/unzip missing for ${file}"
      return 1
    fi
    return 0
  ;;
  l)
    case "${UNJAR##*/}" in
      jar|fastjar)
        "${UNJAR}" -tf "${file}"
      ;;
      unzip)
        "${UNJAR}" -Z -1 "${file}"
      ;;
    esac
    test "$?" = "0" && return 0
    return 1
  ;;
  x)
    case "${UNJAR##*/}" in
      jar|fastjar)
        "${UNJAR}" -xf "${file}"
      ;;
      unzip)
        "${UNJAR}" -oqq "${file}"
      ;;
    esac
    test "$?" = "0" && return 0
    return 1
  ;;
  esac
}

# returns 0 if content is identical
# returns 1 if at least one file differs
# handler f returns 1 if required tool for inspection is missing
# handler l lists content, returns 1 if tool failed
# handler x extracts content, returns 1 if tool failed
compare_archive()
{
  local file="$1"
  local handler="$2"
  local old="`readlink -f \"old/$file\"`"
  local new="`readlink -f \"new/$file\"`"
  local f
  local -a content
  local -i ret=1

  "${handler}" 'f' "${file}" || return 1

  mkdir -p "d/old/${file}" "d/new/${file}"
  if pushd "d" > /dev/null
  then
    "${handler}" 'l' "${old}" | ${sort} > 'co'
    test "${PIPESTATUS[0]}" = "0" || return 1
    "${handler}" 'l' "${new}" | ${sort} > 'cn'
    test "${PIPESTATUS[0]}" = "0" || return 1
    if cmp -s 'co' 'cn'
    then
      if pushd "old/${file}" > /dev/null
      then
        "${handler}" 'x' "${old}" || return 1
        popd > /dev/null
      fi
      if pushd "new/${file}" > /dev/null
      then
        "${handler}" 'x' "${new}" || return 1
        popd > /dev/null
      fi
      readarray -t content < 'cn'
      for f in "${content[@]}"
      do
        if ! check_single_file "${file}/${f}"
        then
          ret=1
          if test -z "$check_all"
          then
            break
          fi
        fi
        watchdog_touch
      done
      ret=$?
    else
      wprint "$file has different file list"
      diff -u 'co' 'cn'
    fi
    popd > /dev/null
    rm -rf "d"
  fi

  return ${ret}
}

check_single_file()
{
  local file="$1"
  local ret=0
  local i
  local failed
  local objdump_failed
  local elfdiff
  local sections
  local -a pipestatus

  if file_is_on_ignorelist "${file}"
  then
    return 0
  fi

  verify_before_processing "${file}" "${dfile}"
  case "$?" in
    0) return 0 ;;
    1) return 1 ;;
    *) ;;
  esac

  normalize_file "${file}"

  case "$file" in
    *.a)
      compare_archive "${file}" 'archive_a'
      return $?
       ;;
    *.cpio)
      compare_archive "${file}" 'archive_cpio'
      return $?
       ;;
    *.squashfs)
      compare_archive "${file}" 'archive_squashfs'
      return $?
       ;;
    *.tar|*.tar.bz2|*.tar.gz|*.tgz|*.tbz2)
      compare_archive "${file}" 'archive_tar'
      return $?
      ;;
    *.zip|*.egg|*.jar|*.war)
      compare_archive "${file}" 'archive_zip'
      return $?
      ;;
     *.bz2)
        bunzip2 -c old/$file > old/${file/.bz2/}
        bunzip2 -c new/$file > new/${file/.bz2/}
        check_single_file ${file/.bz2/}
        return $?
        ;;
     *.gz)
        gunzip -c old/$file > old/${file/.gz/}
        gunzip -c new/$file > new/${file/.gz/}
        check_single_file ${file/.gz/}
        return $?
        ;;
     *.rpm)
	$self_script -a old/$file new/$file
        return $?
        ;;
  esac

  ftype=`/usr/bin/file "old/$file" | sed -e 's@^[^:]\+:[[:blank:]]*@@' -e 's@[[:blank:]]*$@@'`
  case $ftype in
     PE32\ executable*Mono\/\.Net\ assembly*)
       wprint "PE32 Mono/.Net assembly: $file"
       if [ -x /usr/bin/monodis ] ; then
         monodis "old/$file" 2>/dev/null|sed -e 's/GUID = {.*}/GUID = { 42 }/;'> ${file1}
         monodis "new/$file" 2>/dev/null|sed -e 's/GUID = {.*}/GUID = { 42 }/;'> ${file2}
         if ! cmp -s "${file1}" "${file2}"; then
           wprint "$file differs ($ftype)"
           diff --speed-large-files -u "${file1}" "${file2}"
           return 1
         fi
       else
         wprint "Cannot compare, no monodis installed"
         return 1
       fi
       ;;
    ELF*executable*|\
    ELF*[LM]SB\ relocatable*|\
    ELF*[LM]SB\ shared\ object*|\
    setuid\ ELF*[LM]SB\ shared\ object*|\
    ELF*[LM]SB\ pie\ executable*|\
    setuid\ ELF*[LM]SB\ pie\ executable*)
      diff --speed-large-files --unified \
        <( $OBJDUMP -d --no-show-raw-insn old/$file |
          filter_disasm |
          sed -e "s,old/,," ;
          echo "${PIPESTATUS[@]}" > $file1
          ) \
        <( $OBJDUMP -d --no-show-raw-insn new/$file |
          filter_disasm |
          sed -e "s,new/,," ;
          echo "${PIPESTATUS[@]}" > $file2
          ) > $dfile
      ret=$?

      failed=
      read i < ${file1}
      pipestatus=( $i )
      objdump_failed="${pipestatus[0]}"
      i=0
      while test $i -lt ${#pipestatus[@]}
      do
        if test "${pipestatus[$i]}" != "0"
        then
          wprint "ELF: pipe command #$i failed with ${pipestatus[$i]} for old/$file"
          failed='failed'
        fi
        : $(( i++ ))
      done
      read i < ${file2}
      pipestatus=( $i )
      objdump_failed="${objdump_failed}${pipestatus[0]}"
      i=0
      while test $i -lt ${#pipestatus[@]}
      do
        if test "${pipestatus[$i]}" != "0"
        then
          wprint "ELF: pipe command #$i failed with ${pipestatus[$i]} for new/$file"
          failed='failed'
        fi
        : $(( i++ ))
      done

      if test "${objdump_failed}" != "00" || test -n "${failed}"
      then
        # objdump had no idea how to handle it
        if diff_two_files; then
          return 0
        fi
        return 1
      fi

      elfdiff=
      if test "$ret" != "0"
      then
        wprint "$file differs in assembler output"
        $buildcompare_head $dfile
        elfdiff='elfdiff'
      fi

      sections="$(
        $OBJDUMP -s new/$file |
        sed -n --regexp-extended -e '
          /Contents of section .*:/ {
            s,.* (.*):,\1,g
            /\.build-id/d
            /\.gnu_debuglink/d
            /\.gnu_debugdata/d
            p
          }
        '
        )"
      for section in $sections
      do
        diff --unified \
          <( $OBJDUMP -s -j $section old/$file |
              sed -e "s,^old/,," ;
              echo "${PIPESTATUS[@]}" > $file1) \
          <( $OBJDUMP -s -j $section new/$file |
            sed -e "s,^new/,," ;
            echo "${PIPESTATUS[@]}" > $file2
            ) > $dfile
        ret=$?
        failed=
        read i < ${file1}
        pipestatus=( $i )
        objdump_failed="${pipestatus[0]}"
        i=0
        while test $i -lt ${#pipestatus[@]}
        do
          if test "${pipestatus[$i]}" != "0"
          then
            wprint "ELF section: pipe command #$i failed with ${pipestatus[$i]} for old/$file"
            failed='failed'
          fi
          : $(( i++ ))
        done
        read i < ${file2}
        pipestatus=( $i )
        objdump_failed="${objdump_failed}${pipestatus[0]}"
        i=0
        while test $i -lt ${#pipestatus[@]}
        do
          if test "${pipestatus[$i]}" != "0"
          then
            wprint "ELF section: pipe command #$i failed with ${pipestatus[$i]} for new/$file"
            failed='failed'
          fi
          : $(( i++ ))
        done
        if test -n "${failed}"
        then
          elfdiff='elfdiff'
          break
        fi
        if test "$ret" != "0"
        then
          wprint "$file differs in ELF section $section"
          $buildcompare_head $dfile
          elfdiff='elfdiff'
        else
          watchdog_touch
        fi
      done
      if test -n "$elfdiff"; then
        return 1
      fi
      return 0
      ;;
     *ASCII*|*text*)
       if ! cmp -s "old/$file" "new/$file"; then
         wprint "$file differs ($ftype)"
         diff -u "old/$file" "new/$file" | $buildcompare_head
         return 1
       fi
       ;;
     directory|setuid\ directory|setuid,\ directory|sticky,\ directory)
       # tar might package directories - ignore them here
       return 0
       ;;
     bzip2\ compressed\ data*)
       if ! check_compressed_file "$file" "bz2"; then
           return 1
       fi
       ;;
     gzip\ compressed\ data*)
       if ! check_compressed_file "$file" "gzip"; then
           return 1
       fi
       ;;
     XZ\ compressed\ data*)
       if ! check_compressed_file "$file" "xz"; then
           return 1
       fi
       ;;
    Zip\ archive\ data,*)
      if ! compare_archive "${file}" 'archive_zip' ; then
        return 1
      fi
      ;;
     POSIX\ tar\ archive)
          mv old/$file{,.tar}
          mv new/$file{,.tar}
          if ! check_single_file ${file}.tar; then
            return 1
          fi
       ;;
     cpio\ archive)
          mv old/$file{,.cpio}
          mv new/$file{,.cpio}
          if ! check_single_file ${file}.cpio; then
            return 1
          fi
     ;;
     Squashfs\ filesystem,*)
        wprint "$file ($ftype)"
        mv old/$file{,.squashfs}
        mv new/$file{,.squashfs}
        if ! check_single_file ${file}.squashfs; then
          return 1
        fi
     ;;
     broken\ symbolic\ link\ to\ *|symbolic\ link\ to\ *)
       readlink "old/$file" > $file1
       readlink "new/$file" > $file2
       if ! diff -u $file1 $file2; then
         wprint "symlink target for $file differs"
         return 1
       fi
       ;;
     block\ special\ *)
     ;;
     character\ special\ *)
     ;;
     *)
       if ! diff_two_files; then
           return 1
       fi
       ;;
  esac
  return 0
}

FUNCTIONS=${0%/*}/functions.sh
: ${buildcompare_head:="head -n 200"}
nofilter=${buildcompare_nofilter}
sort=sort
[[ $nofilter ]] && sort=cat

check_all=
case $1 in
  -a | --check-all)
    check_all=1
    shift
esac

if test "$#" != 2; then
   echo "usage: $0 [-a|--check-all] old.rpm new.rpm"
   exit 1
fi

test -z $OBJDUMP && OBJDUMP=objdump

# Always clean up on exit
local_tmpdir=`mktemp -d`
if test -z "${local_tmpdir}"
then
  exit 1
fi
function _exit()
{
  chmod -R u+w "${local_tmpdir}"
  rm -rf "${local_tmpdir}"
}
trap _exit EXIT
# Let further mktemp refer to private tmpdir
export TMPDIR=$local_tmpdir

self_script=$(cd $(dirname $0); echo $(pwd)/$(basename $0))

source $FUNCTIONS

oldpkg=`readlink -f $1`
newpkg=`readlink -f $2`
rename_script=`mktemp`

file1=`mktemp`
file2=`mktemp`
dir=`mktemp -d`
dfile=`mktemp`

if test ! -f "$oldpkg"; then
    echo "can't open $1"
    exit 1
fi

if test ! -f "$newpkg"; then
    echo "can't open $2"
    exit 1
fi

echo "Comparing `basename $oldpkg` to `basename $newpkg`"

case $oldpkg in
  *.rpm)
    cmp_rpm_meta "$rename_script" "$oldpkg" "$newpkg"
    RES=$?
    case $RES in
    0)
      echo "RPM meta information is identical"
      if test -z "$check_all"; then
        exit 0
      fi
      ;;
    1)
      echo "RPM meta information is different"
      if test -z "$check_all"; then
        exit 1
      fi
      ;;
    2)
      echo "RPM file checksum differs."
      RES=0
      ;;
    *)
      echo "Wrong exit code!"
      exit 1
      ;;
    esac
  ;;
esac

wprint "Extracting packages"
unpackage $oldpkg $dir/old
unpackage $newpkg $dir/new

case $oldpkg in
  *.deb|*.ipk)
    adjust_controlfile $dir/old $dir/new
  ;;
esac

# files is set in cmp_rpm_meta for rpms, so if RES is empty we should assume
# it wasn't an rpm and pick all files for comparison.
if [ -z $RES ]; then
  oldfiles=`cd $dir/old; find . -type f`
  newfiles=`cd $dir/new; find . -type f`

  files=`echo -e "$oldfiles\n$newfiles" | sort -u`
fi

cd $dir
bash $rename_script

# We need /proc mounted for some tests, so check that it's mounted and
# complain if not.
PROC_MOUNTED=0
if [ ! -d /proc/self/ ]; then
  echo "/proc is not mounted"
  mount -orw -n -tproc none /proc
  PROC_MOUNTED=1
fi

# preserve cmp_rpm_meta result for check_all runs
ret=$RES
readarray -t filesarray <<<"$files"
for file in "${filesarray[@]}"; do
   if ! check_single_file "$file"; then
       ret=1
       if test -z "$check_all"; then
           break
       fi
   fi
done

if [ "$PROC_MOUNTED" -eq "1" ]; then
  echo "Unmounting proc"
  umount /proc
fi

if test "$ret" = 0; then
     echo "Package content is identical"
fi
exit $ret
# vim: tw=666 ts=2 shiftwidth=2 et
