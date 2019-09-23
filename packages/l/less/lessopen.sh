#!/bin/bash
#
# Copyright (c) 2001 SUSE GmbH, Nuernberg, Germany
# Copyright (c) 2002 SUSE Linux AG, Nuernberg, Germany
#
# Author: Vladimir Linek <vinil@suse.cz>
# Support for directory listing by Dimitar Pashov <d.pashov@gmail.com>
#
# Preprocessor for 'less'.
# Use with environment variable:  LESSOPEN="lessopen.sh %s"

# the following hack does not break anything but helps to view file whose name
# begins with a "-" or "+" with names
if echo "$1" | grep -q ^/; then
  # absolute path
  SRC="$1"
else
  # relative path
  SRC="./$1"
fi
  
NAME="${SRC##*/}"

[ ! -r "$SRC" ] && exit 1

cleaner() {
    test "$TMPF_pre" = "$SRC" -o "$TMPF_pre" = "$TMPF" && return
    rm -f "$TMPF_pre"
}
trap 'cleaner' EXIT SIGHUP
TMPF=$(mktemp /tmp/less.XXXXXXXXX) || exit 1
TMPF_pre=$(mktemp /tmp/less.XXXXXXXXX) || exit 1

lang=$LANG
test -n "$LC_CTYPE" && lang="$LC_CTYPE"
case "$lang" in
    *.UTF-8|*.UTF8)
    GROFF_DEVICE=utf8
    ;;
    ja*)
    GROFF_DEVICE=nippon
    ;;
    *)
    GROFF_DEVICE=latin1
    ;;
esac

CMD=
type=`/usr/bin/file -L "$SRC"`
case ${type#"$SRC": } in
	*"gzip compressed data"*|\
	*"compress'd data"*|\
	*"packed data"*)
		CMD="gzip -dc" ;;
	*"Zip archive data"*)
		CMD="unzip -v" ;;
	*"bzip"*" compressed data"*)
		CMD="bzip2 -dc" ;;
	*"xz compressed data"*|\
	*"XZ compressed data"*)
		CMD="xz -dc" ;;
	*)
		rm -f "$TMPF_pre"
		TMPF_pre="$SRC" ;;
esac

test -n "$CMD" && $CMD "$SRC" >"$TMPF_pre" 2>/dev/null

	type=`/usr/bin/file -L "$TMPF_pre"`
	case ${type#"$TMPF_pre": } in
		*tar\ archive*)
			if [ -x "`/usr/bin/which tar 2>/dev/null`" ]; then
			tar tvvf "$TMPF_pre" >"$TMPF" 2>/dev/null
			else echo "tar is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*Microsoft\ Cabinet\ *\ data*)
			if [ -x "`/usr/bin/which cabextract 2>/dev/null`" ]; then
			cabextract -l "$TMPF_pre" >"$TMPF" 2>/dev/null
			else echo "cabextract is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*RPM*)
			if [ -x "`/usr/bin/which rpm 2>/dev/null`" ]; then
			(echo -e "=============================== Information ====================================\n";
			rpm -qip "\"$TMPF_pre\"";
			echo -e "\n\n================================= Changelog (head) =============================\n";
			rpm -qp --changelog "\"$TMPF_pre\"" | head -n 16
			echo -e "\n\n================================= Content ======================================\n";
			rpm -qlp "\"$TMPF_pre\""
                        ) >"$TMPF" 2>/dev/null
			else echo "rpm is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*DVI*)
			if [ -x "`/usr/bin/which dvi2tty 2>/dev/null`" ]; then
			  if [ "${TMPF_pre%.dvi}" != "$TMPF_pre" ] ; then
			     dvi2tty -q "$TMPF_pre" >"$TMPF" 2>/dev/null
			  else echo "dvi2tty requires an input file name with the suffix .dvi" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre" ; fi
			else echo "dvi2tty is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*PDF*)
			if [ -x "`/usr/bin/which pdftotext 2>/dev/null`" ]; then
			pdftotext "$TMPF_pre" "$TMPF" 2>/dev/null
			else echo "pdftotext is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*Debian\ binary\ package*)
			if [ -x "`/usr/bin/which dpkg-deb 2>/dev/null`" ]; then
			dpkg-deb -c "$TMPF_pre" >"$TMPF" 2>/dev/null
			else echo "dpkg-deb is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*\ ar\ archive*)
			if [ -x "`/usr/bin/which nm 2>/dev/null`" ]; then
			nm "$TMPF_pre" >"$TMPF" 2>/dev/null
			else echo "nm is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*directory*)
			# assuming ls is always available
			ls -lh "$TMPF_pre" >"$TMPF" 2>/dev/null
			;;
	        *diff\ output*)
			# I haven't found way, to set less -R from this script
			# so check, if '-R' or '--RAW-CONTROL-CHARS' is set in environment
			R_NOT_SET=true
			for i in $LESS; do
				if [ "${i:0:1}" = "-" ]; then
					if [ "${i:1:1}" = "-" ]; then
						if [ "$i" = --RAW-CONTROL-CHARS ]; then
							R_NOT_SET=false
							break
						else
							continue
						fi
					else
						for j in `seq 1 $((${#i} - 1 ))`; do
							if [ "${i:j:1}" = R ]; then
								R_NOT_SET=false
								break
							fi
						done
					fi
				fi
			done
			# if we have -R and colordiff, we can continue
			if [ $R_NOT_SET = false ] && \
				[ -x "`/usr/bin/which colordiff 2>/dev/null`" ]; then
			colordiff < "$TMPF_pre" | cat > "$TMPF" 2>/dev/null
			else rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
			;;
		*)
			if [ "$LESS_ADVANCED_PREPROCESSOR" = "yes" ]; then
				case ${type#"$TMPF_pre": } in
					*troff*)
						if [ -x "`/usr/bin/which groff 2>/dev/null`" ]; then
						case "$NAME" in
							*.[1-9nxp]*|*.man|*.[1-9nxp]*.*|*.man.*)
								groff -s -p -t -e -T$GROFF_DEVICE -mandoc "$TMPF_pre" >"$TMPF" 2>/dev/null ;;
							*.ms|*.ms.*)
								groff -T$GROFF_DEVICE -ms "$TMPF_pre" >"$TMPF" 2>/dev/null ;;
							*.me|*.me.*)
								groff -T$GROFF_DEVICE -me "$TMPF_pre" >"$TMPF" 2>/dev/null ;;
							*)
								groff -T$GROFF_DEVICE "$TMPF_pre" >"$TMPF" 2>/dev/null ;;
						esac
						else echo "groff is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
						;;
					*PostScript*)
						if [ -x "`/usr/bin/which ps2ascii 2>/dev/null`" ]; then
						ps2ascii "$TMPF_pre" >"$TMPF" 2>/dev/null
						else echo "ps2ascii is not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
						;;
					*HTML*)
						if [ -x "`/usr/bin/which w3m 2>/dev/null`" ]; then
						w3m -dump -T text/html "$TMPF_pre" >"$TMPF" 2>/dev/null
						elif [ -x "`/usr/bin/which lynx 2>/dev/null`" ]; then
						lynx -dump -force_html "$TMPF_pre" >"$TMPF" 2>/dev/null
						else echo "lynx/w3m not available for preprocessing" 1>&2; rm -f "$TMPF"; TMPF="$TMPF_pre"; fi
						;;
					*)
						rm -f "$TMPF"
						TMPF="$TMPF_pre" 
						;;
				esac	
			else
				rm -f "$TMPF"
				TMPF="$TMPF_pre"
			fi
			;;
	esac

test "$TMPF" = "$SRC" || echo "$TMPF"
