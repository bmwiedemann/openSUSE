#!/bin/bash

# macro: suse_update_desktop_file
#
#     Used to add easily a category to .desktop files according to XDG
#     standard.
#

. /usr/lib/rpm/map-desktop-category.sh

#
# parse arguments
#
INSTALL=no
I18N=yes
CREATE=no
RESET=no
UNIMPORTANT=no
NAME=no
COMMENT=no
GNAME=no

function usage() {
	local exitcode="$1"
	if [ -z "$exitcode" ]; then
		exitcode=1
	fi
	echo
	echo "Usage: $(basename $0) [OPTIONS] <APPLICATION> [CATEGORIES]"
	echo
	echo " Summary:"
	echo "       Used to add easily a category to .desktop files according to XDG"
	echo "       standard. More information is available on"
	echo "       http://en.opensuse.org/SUSE_Package_Conventions/RPM_Macros"
	echo "       If you have any questions, please use our mailinglist: "
	echo "       opensuse-packaging@opensuse.org"
	echo " Options:"
	echo "       <APPLICATION>             : The name of the desktop file."
	echo "                                   Example: use \"qbrew\" to edit qbrew.desktop"
	echo "                                   If APPLICATION has multiple desktop files, try the exact path"
	echo "                                   to the desktop file."
	echo "                                   Example: use \"%suse_update_desktop_file \\"
	echo "                                   %{buildroot}%{_datadir}/susehelp/meta/%name/%name.desktop\""
	echo "                                   to edit the susehelp desktop entry file instead."
	echo "       -u|--unimportant          : add \"NoDisplay=true\" to the resulting desktop"
	echo "                                   file."
	echo "       -n|--no-i18n              : Do not prepare the desktop file for translators (obsoletes -t)."
	echo "                                   (adds X-SuSE-translate=false to the desktop file)"
	echo "       -i|--install              : Install an existing desktop file in /usr/share/applications/"
	echo "                                   The to be installed desktop file can be located in:"
	echo "                                   - RPM_SOURCE_DIR or"
	echo "                                   - RPM_BUILD_DIR"
	echo "                                   A referenced icon file (ending *.png; *.xpm) is installed in"
	echo "                                   /usr/share/pixmaps/ automatically if it is located in one of the " 
	echo "                                   directories mentioned above (-maxdepth 1)."
	echo "       -r|--reset                : Reset the \"Categories\" line in an existing desktop file."
	echo "                                   Normally, categories mentioned in an existing desktop file will be"
	echo "                                   obtained. Additional categories from commandline are added."
	echo "       -d|--docid <string>       : Add \"X-SuSE-DocTeamID=<string>\" to the desktop file."
	echo "       -D|--docpath <path>       : Add \"DocPath=<path>\" to the desktop file - do not guess it"
	echo "                                   automatically."
	echo "       -c|--create <name>        : Create a new desktop file in /usr/share/applications/<name>.desktop ."
	echo "       -C|--comment <string>     : Use <string> as \"Comment=<string>\" in desktop file."
	echo "       -N|--name <string>        : Use <string> as \"Name=<string>\" in desktop file."
	echo "       -G|--genericname <string> : Use <string> as \"GenericName=<string>\" in desktop file."
	echo ""
	exit $exitcode
}


while [ "${1:0:1}" = "-" ]; do
  case ${1} in
    -h|--help)
       usage 0 ;;
    -u|--unimportant)
       UNIMPORTANT=yes
       shift
       continue;;
    -n|--no-i18n)
       I18N=no
       shift
       continue;;
    -i|--install)
       INSTALL=yes
       shift
       continue;;
    -r|--reset)
       RESET=yes
       shift
       continue;;
    -d|--docid)
       shift
       DOCID="${1}"
       shift
       continue;;
    -D|--docpath)
       shift
       DOCPATH="${1}"
       if ! [ -r "$RPM_BUILD_ROOT/opt/kde3/share/doc/HTML/en/$DOCPATH/index.docbook" -o -r $RPM_BUILD_ROOT/usr/share/gnome/help/$DOCPATH/C/$DOCPATH.xml -o -r $RPM_BUILD_ROOT/usr/share/gnome/help/${DOCPATH/\///C/} ] ; then 
         echo WARNING: suse_update_desktop_file: DocPath target $DOCPATH for $FILE does not exist
       fi
       shift
       continue;;
    -c|--create)
       CREATE=yes
       INSTALL=yes
       shift
       continue;;
    -C|--comment)
       shift
       COMMENT="${1}"
       shift
       continue;;
    -N|--name)
       shift
       NAME="${1}"
       shift
       continue;;
    -G|--genericname)
       shift
       GNAME="${1}"
       shift
       continue;;
    --basedir)
       echo "WARNING: basedir is no longer supported"
       shift
       shift
       continue;;
    --project)
       echo "WARNING: project is no longer supported"
       shift
       shift
       continue;;
   *)
       echo "UNKNOWN OPTION: $1"
       usage 1 ;;
  esac
done

APPLICATION="$1"
shift
if [ "$CREATE" = "yes" ]; then
  NAME="$1"
  shift
  GNAME="$1"
  shift
  EXEC="$1"
  shift
  ICON="$1"
  shift
  if [ -z "$NAME" -o -z "$EXEC" ]; then
     echo "ERROR: after --create you should define" >&2
     echo "       DESKTOP_FILE_NAME NAME GENERICNAME EXECUTABLE \[ ICON CATEGORIES... \]" >&2
     usage 1
  fi
  mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
  cat > $RPM_SOURCE_DIR/$APPLICATION.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=$NAME
GenericName=$GNAME
Type=Application
Exec=$EXEC
Icon=$ICON
EOF
NAME=no
GNAME=no
fi
if [ "$INSTALL" = "yes" ]; then
  mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
  FILE=`find $RPM_SOURCE_DIR $RPM_BUILD_DIR . -name $APPLICATION.desktop| sort -r | head -n 1`
  if [ -s "$FILE" ]; then
    cp -v "$FILE" $RPM_BUILD_ROOT/usr/share/applications/
    icon_file=`sed -n '/^\[Desktop Entry\]/,/(\[.*|$)/ s,Icon=\(.*\),\1,p' "$FILE"`
    icon_file=`find $RPM_SOURCE_DIR $RPM_BUILD_DIR -maxdepth 1 -name ${icon_file}.png -o -name ${icon_file}.xpm -o -name $icon_file | sort -r | head -n 1`
    if [ -s "$icon_file" ]; then
      mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
      cp -v "$icon_file" $RPM_BUILD_ROOT/usr/share/pixmaps/
    fi
  fi
fi
while [ "$1" ]; do
  CATEGORIES="$CATEGORIES;$1"
  shift
done
CATEGORIES="${CATEGORIES#;}"
if [ -z "$APPLICATION" ]; then
  echo "ERROR: suse_update_desktop_file: no application argument given" >&2
  echo "                                 Example: use "qbrew" to edit qbrew.desktop" >&2
  usage 1
fi

#
# find file
#
for i in /$RPM_BUILD_ROOT/usr/share/applications/ \
  /$RPM_BUILD_ROOT/etc/xdg/autostart/ ; do
    [ -e "$i" ] && DIRS="$DIRS $i" 
done 
if [ "${APPLICATION:0:1}" == "/" -a -e "$APPLICATION" ]; then
  FILE_="$APPLICATION"
else
  FILE_=`find $DIRS -name $APPLICATION.desktop` 
fi
if [ -z "$FILE_" ]; then 
   echo "ERROR: suse_update_desktop_file: unable to find $APPLICATION" >&2
   usage 1 
fi 
FILE=""
for i in $FILE_; do
  #
  # fix old files
  #
  sed -e 's/\[KDE Desktop Entry\]/[Desktop Entry]/' "$i" > "${i}_" && mv "${i}_" "$i"

  # dos2unix for the poor
  sed -e 's/\r//' "$i" > "${i}_" && mv "${i}_" "$i"

  if [ "$FILE" ]; then
    echo "ERROR: suse_update_desktop_file: $APPLICATION has multiple desktop files" >&2
    usage 1
  fi
  FILE=$i
done

#
# validate file
#
if [ ! -r "$FILE" ]; then 
   echo "ERROR: suse_update_desktop_file: unable to read $FILE" >&2
   usage 1 
fi 
# esp. for susehelp
FILE_DOCPATH=`sed -n -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,;, ,g' -e 's,^DocPath=\\(.*\\),\\1,p' ${FILE}` 
if [ -n "$FILE_DOCPATH" ] ; then
  if [ ! -r "$RPM_BUILD_ROOT/usr/share/gnome/help/$FILE_DOCPATH/C/$FILE_DOCPATH.xml" ] && [ ! -r $RPM_BUILD_ROOT/usr/share/gnome/help/${DOCPATH/\///C/} ] ; then 
     echo WARNING: suse_update_desktop_file: DocPath target $FILE_DOCPATH for $FILE does not exist
  fi
fi

#BEGIN Upstreaming help
DESKTOP_NAME=${APPLICATION##*/}
DESKTOP_PATH=${APPLICATION%$DESKTOP_NAME}
DESKTOP_NAME=${DESKTOP_NAME%.desktop}
if test -z "$DESKTOP_PATH" ; then
  DESKTOP_PATH=$RPM_BUILD_ROOT/usr/share/applications/
fi
# Get rid ugly but common slash duplication
DESKTOP_PATH=${DESKTOP_PATH//\/\//\/}

# Set working directory always to $RPM_BUILD_DIR. It prevents placing
# the files inside BUILDROOT. And some packages are confused by new
# desktop files placed to its build directory.
SUDF_DIR=$RPM_BUILD_DIR

mkdir -p $SUDF_DIR/suse_update_desktop_file/update-desktop-files/$DESKTOP_NAME
cp -v "$FILE" $SUDF_DIR/suse_update_desktop_file/update-desktop-files/$DESKTOP_NAME/$DESKTOP_NAME-upstream.desktop
#END Upstreaming help
#
# update Categories
#
if [ "$RESET" = "no" ]; then
  CATIN=`sed -n -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,;, ,g' -e 's,^Categories=\\(.*\\),\\1,p' ${FILE}` 
fi
CATIN="$CATIN ${CATEGORIES//;/ }"
unset CAT
unset DCAT
for i in $CATIN; do
  ret=""
  mapCategory $i
  if [ -z "$ret" ]; then 
    echo "WARNING: Category \"$i\" is unknown \!"
    echo WARNING: it is ignored, until you registered a Category at opensuse-packaging@opensuse.org .
  else
    echo "$CAT" | grep -q "[=;]$i;" || CAT="$CAT$ret;"
  fi
done
echo "" >> "${FILE}" 
CAT="${CAT#;}"
if grep -q ^Categories= $FILE; then 
  sed -i -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^Categories=.*,Categories='${CAT}',' "$FILE"
else 
  if [ -n "${CAT%;}" ]; then
    sed -i -e '/^\[Desktop Entry\]/a \
'"Categories=${CAT%;};" $FILE
  fi
fi
if [ "$UNIMPORTANT" = "yes" ]; then
  if grep -q ^NoDisplay= $FILE; then
    sed -i -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^NoDisplay=.*,NoDisplay=true,' "$FILE" 
  else
    sed -i -e '/^\[Desktop Entry\]/a \
NoDisplay=true' $FILE 
  fi
fi
if [ "$DOCID" ]; then
  sed -i -e '/^\[Desktop Entry\]/a \
'"X-SuSE-DocTeamID=$DOCID" $FILE
fi

#
# check or set DocPath
#
DOCPATH_IS_GUESS=false
if [ -z "$DOCPATH" ] ; then
  if [ -f $RPM_BUILD_ROOT/usr/share/gnome/help/$APPLICATION/C/$APPLICATION.xml ] ; then
    DOCPATH=$APPLICATION
    DOCPATH_IS_GUESS=true
  fi
  # NOTE: Here we can add guess for application/file.xml
fi
if [ -n "$DOCPATH" ] ; then
  if [ -n "$FILE_DOCPATH" ] ; then 
    # DocPath already exists. Update it only from command line, not from guess.
    if $DOCPATH_IS_GUESS ; then
      if [ "$DOCPATH" != "$FILE_DOCPATH" ] ; then
        echo WARNING: suse_update_desktop_file: DocPath target $FILE_DOCPATH differs from guess $DOCPATH for $FILE
      fi
    else
      sed -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^DocPath=.*,DocPath='${DOCPATH}',' "$FILE" > "${FILE}.new" &&
      mv "${FILE}.new" "${FILE}"
    fi
  else 
    sed -i -e '/^\[Desktop Entry\]/a \
'"DocPath=${DOCPATH}" $FILE 
    if $DOCPATH_IS_GUESS ; then
      echo NOTE: suse_update_desktop_file: Guessing DocPath=$DOCPATH in $FILE
    fi
  fi
fi

if grep -q ^X-SuSE-translate= $FILE; then
   echo "ERROR: $FILE contains X-SuSE-translate - called the macro twice?" >&2
   usage 1
fi

if [ "$NAME" != "no" ]; then
    sed -i -e '/^Name\[/d' $FILE 
    if [ -n "$NAME" ]; then
       if ! grep -q ^Name= ${FILE}; then
         sed -i -e '/^\[Desktop Entry\]/a '"Name=${NAME//,/\,}" ${FILE}
       else
         sed -i -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^Name=.*,Name='"${NAME//,/\,}"',' ${FILE}
       fi
    else
      sed -i -e '/^Name=/d' $FILE
    fi
fi

if [ "$GNAME" != "no" ]; then
    sed -i -e '/^GenericName\[/d' $FILE
    if [ -n "$GNAME" ]; then
       if ! grep -q ^GenericName= ${FILE}; then
	 sed -i -e '/^\[Desktop Entry\]/a '"GenericName=${GNAME//,/\,}" ${FILE}
       else
         sed -i -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^GenericName=.*,GenericName='"${GNAME//,/\,}"',' ${FILE}
       fi
    else
      sed -i -e '/^GenericName=/d' $FILE
    fi
fi

if [ "$COMMENT" != "no" ]; then
    sed -i -e '/^Comment\[/d' $FILE 
    if [ -n "$COMMENT" ]; then
	if ! grep -q ^Comment= ${FILE}; then
          sed -i -e '/^\[Desktop Entry\]/a '"Comment=${COMMENT//,/\,}" ${FILE}
	else
          sed -i -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,^Comment=.*,Comment='"${COMMENT//,/\,}"',' ${FILE}
	fi
    else
      sed -i -e '/^Comment=/d' $FILE
    fi
fi

#BEGIN Upstreaming help
GENERIC_CHANGES=false
TRANSLATION_CHANGES=false
DEADPACKAGE_SUCCESS=false
shopt -s nullglob
cp -v "$FILE" $SUDF_DIR/suse_update_desktop_file/update-desktop-files/$DESKTOP_NAME/$DESKTOP_NAME-downstream-no-translation.desktop
# Insert translations from the downstream
ORIG_DIR=$PWD
cd $SUDF_DIR/suse_update_desktop_file/update-desktop-files/$DESKTOP_NAME
if [ "$I18N" != "no" ]; then
    sed "s@^Name=@_&Name($DESKTOP_NAME.desktop): @;s@^GenericName=@_&GenericName($DESKTOP_NAME.desktop): @;s@^Comment=@_&Comment($DESKTOP_NAME.desktop): @;s@^Keywords=@_&Keywords($DESKTOP_NAME.desktop): @" $FILE >$DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop
    intltool-merge /usr/share/desktop-translations/desktop_translations $DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop $DESKTOP_NAME-downstream-translated-raw.desktop -d -u
    sed -i "s@^Name=Name($DESKTOP_NAME.desktop): @Name=@;s@^GenericName=GenericName($DESKTOP_NAME.desktop): @GenericName=@;s@^Comment=Comment($DESKTOP_NAME.desktop): @Comment=@;s@^Keywords=Keywords($DESKTOP_NAME.desktop): @Keywords=@" $DESKTOP_NAME-downstream-translated-raw.desktop
    ${0%.sh}_process_translations.py $DESKTOP_NAME
    cp -a -v $DESKTOP_NAME-downstream-translated.desktop $FILE
    if ! diff -u $DESKTOP_NAME-upstream.desktop $DESKTOP_NAME-downstream-translated.desktop >$DESKTOP_NAME-downstream-directly-translated.diff ; then
        TRANSLATION_CHANGES=true
    fi
    sed -i "1,2s/$DESKTOP_NAME-\(upstream\|downstream-translated\).desktop/$DESKTOP_NAME.desktop/" $DESKTOP_NAME-downstream-directly-translated.diff
    for DESKTOP in $DESKTOP_NAME-upstream $DESKTOP_NAME-downstream-no-translation ; do
        sed "/\(Name\|GenericName\|Comment\|Keywords\)\[/d;s@^Name=@_Name=@;s@^GenericName=@_GenericName=@;s@^Comment=@_Comment=@;s@^Keywords=@_Keywords=@" $DESKTOP.desktop >$DESKTOP.desktop.in
    done
    if ! diff -u $DESKTOP_NAME-upstream.desktop.in $DESKTOP_NAME-downstream-no-translation.desktop.in >$DESKTOP_NAME-downstream-in-translated.diff ; then
        GENERIC_CHANGES=true
    fi
    sed -i "1,2s/$DESKTOP_NAME-\(upstream\|downstream-no-translation\).desktop.in/$DESKTOP_NAME.desktop.in/" $DESKTOP_NAME-downstream-in-translated.diff
    mkdir po
    intltool-extract --type=gettext/ini $DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop
    xgettext --default-domain=$DESKTOP_NAME --add-comments --keyword=_ --keyword=N_ --keyword=U_ $DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop.h -o po/$DESKTOP_NAME.pot
    for PO in /usr/share/desktop-translations/desktop_translations/*.po ; do
        LNG=${PO##*/}
        LNG=${LNG%.po}
        msgmerge $PO po/$DESKTOP_NAME.pot -o po/$LNG-pre.po
        if test -f po/$LNG-pre.po ; then
            msgattrib --no-obsolete po/$LNG-pre.po -o po/$LNG.po
        fi
        sed -i "s@\"\(Name\|GenericName\|Comment\|Keywords\)($DESKTOP_NAME.desktop): @\"@" po/$LNG.po
        rm po/$LNG-pre.po
    done
    sed -i "s@\"\(Name\|GenericName\|Comment\|Keywords\)($DESKTOP_NAME.desktop): @\"@" po/$DESKTOP_NAME.pot
    rm $DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop $DESKTOP_NAME-downstream-no-translation-desktop_translations.desktop.h $DESKTOP_NAME-downstream-translated-raw.desktop
    mkdir -p deadpackage/po
    if test -d $ORIG_DIR/po ; then
        echo -n "" >$DESKTOP_NAME-deadpackage-po.diff
        echo -n "" >$DESKTOP_NAME-deadpackage-po-upstreamfirst.diff
        for PO in po/*.po po/$DESKTOP_NAME.pot ; do
            if test -f $ORIG_DIR/$PO ; then
                msgcat --use-first $PO $ORIG_DIR/$PO -o deadpackage/$PO
                diff -u $ORIG_DIR/$PO deadpackage/$PO >>$DESKTOP_NAME-deadpackage-po.diff
                msgcat --use-first $ORIG_DIR/$PO $PO -o deadpackage/$PO
                diff -u $ORIG_DIR/$PO deadpackage/$PO >>$DESKTOP_NAME-deadpackage-po-upstreamfirst.diff
            else
                diff -u /dev/null $PO >>$DESKTOP_NAME-deadpackage-po.diff
                diff -u /dev/null $PO >>$DESKTOP_NAME-deadpackage-po-upstreamfirst.diff
            fi
        done
        sed -i 's:^\(---\|\+\+\+\) deadpackage/:\1 :;s:^\(---\|\+\+\+\) '$ORIG_DIR/':\1 :' $DESKTOP_NAME-deadpackage-po.diff $DESKTOP_NAME-deadpackage-po-upstreamfirst.diff
        DEADPACKAGE_SUCCESS=true
        rm -rf deadpackage
    fi
fi

# Generate output in the OTHER directory
cd ..
RPM_OTHER_DIR=${RPM_BUILD_DIR%/BUILD*}/OTHER
if test -f $RPM_OTHER_DIR/update-desktop-files.tar.gz ; then
    X=r
else
    X=c
fi
cd ..
tar ${X}f $RPM_OTHER_DIR/update-desktop-files.tar.gz update-desktop-files

EOF=EOF
cat <<EOF
========================= Deprecation notice ==============================

%suse_update_desktop_file is deprecated and will be removed in the future.
It provides SUSE specific changes that were never sent to the upstream.
there is a time to change this now.

Please follow
https://en.opensuse.org/openSUSE:Update-desktop-files_deprecation

Are there any generic changes to upstream: $GENERIC_CHANGES
Are there any translation changes to upstream: $TRANSLATION_CHANGES
po files diff generator succeeded: $DEADPACKAGE_SUCCESS

Location of the upstreaming files during the build:
$SUDF_DIR/suse_update_desktop_file/$DESKTOP_NAME
- $DESKTOP_NAME-downstream-directly-translated.diff
- $DESKTOP_NAME-downstream-in-translated.diff
- $DESKTOP_NAME-downstream-no-translation.desktop
- $DESKTOP_NAME-downstream-no-translation.desktop.in
- $DESKTOP_NAME-downstream-translated.desktop
- $DESKTOP_NAME-upstream.desktop
- $DESKTOP_NAME-upstream.desktop.in

And for dead packages (optionally):
- $DESKTOP_NAME-deadpackage-po.diff
- $DESKTOP_NAME-deadpackage-po-upstreamfirst.diff

Customized helpers for you (for cut-and-paste purpose):
cd update-desktop-files/$DESKTOP_NAME/po
for PO in *.po ; do
	if test -f ../../../po/\$PO ; then
		msgcat --use-first \$PO ../../../po/\$PO -o ../../../po/\$PO.new
		mv ../../../po/\$PO.new ../../../po/\$PO
	else
		cp -a \$PO ../../../po/\$PO
	fi
done

Or swap arguments of msgcat according to the documentation:
		msgcat --use-first ../../../po/\$PO \$PO -o ../../../po/\$PO.new

sed "/\(Name\|GenericName\|Comment\|Keywords\)\[/d;s@^Name=@_Name=@;s@^GenericName=@_GenericName=@;s@^Comment=@_Comment=@;s@^Keywords=@_Keywords=@" <$DESKTOP_NAME.desktop >$DESKTOP_NAME.desktop.in
patch <$DESKTOP_NAME-downstream-in-translated.diff

Source{number}: $DESKTOP_NAME.desktop.in
or
Source{number}: $DESKTOP_NAME.desktop

cp %{SOURCE{NUMBER}} .

%translate_suse_desktop $DESKTOP_NAME.desktop

install -D -m 0644 $DESKTOP_NAME.desktop %{buildroot}${DESKTOP_PATH#$RPM_BUILD_ROOT}$DESKTOP_NAME.desktop

osc add $DESKTOP_NAME.desktop.in
osc rm $DESKTOP_NAME.desktop

if ! diff $DESKTOP_NAME.desktop %{SOURCE{number}} ; then
cat <<EOF
A new version of desktop file exists. Please update $DESKTOP_NAME.desktop
rpm source from $PWD to get translations to older products.
$EOF
-===========================================================================
EOF
cd $ORIG_DIR
#END Upstreaming help

if [ "$I18N" = "no" ]; then
  #
  # this file will not get translated
  #
  sed -i -e '/^\[Desktop Entry\]/a \
X-SuSE-translate=false' $FILE
fi
