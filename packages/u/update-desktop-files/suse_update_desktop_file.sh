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
for i in /$RPM_BUILD_ROOT/opt/kde3/share/applications/kde/ \
  /$RPM_BUILD_ROOT/opt/kde3/share/applnk \
  /$RPM_BUILD_ROOT/usr/share/applications/ \
  /$RPM_BUILD_ROOT/usr/share/gnome/apps/ \
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
# move KDE legacy files to XDG path
#
if echo $FILE | grep -q /opt/kde3/share/applnk/ ; then
 if ! echo $FILE | grep -q /opt/kde3/share/applnk/.hidden/ ; then
  if ! echo $FILE | grep -q /opt/kde3/share/applnk/Settings/ ; then
   if ! echo $FILE | grep -q /opt/kde3/share/applnk/System/ScreenSavers/ ; then
     echo "WARNING: file is in old KDE legacy path, moving it to XDG path"
     mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/applications/kde/
     mv "$FILE" $RPM_BUILD_ROOT/opt/kde3/share/applications/kde/
     FILE="$RPM_BUILD_ROOT/opt/kde3/share/applications/kde/${FILE##*/}"
   fi
  fi
 fi
fi

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
  if [ ! -r "$RPM_BUILD_ROOT/opt/kde3/share/doc/HTML/en/$FILE_DOCPATH/index.docbook" ] && [ ! -r "$RPM_BUILD_ROOT/usr/share/gnome/help/$FILE_DOCPATH/C/$FILE_DOCPATH.xml" ] && [ ! -r $RPM_BUILD_ROOT/usr/share/gnome/help/${DOCPATH/\///C/} ] ; then 
     echo WARNING: suse_update_desktop_file: DocPath target $FILE_DOCPATH for $FILE does not exist
  fi
fi

#
# update Categories
#
if [ "$RESET" = "no" ]; then
  CATIN=`sed -n -e '/^\[Desktop Entry\]/,/(\[.*|$)/ s,;, ,g' -e 's,^Categories=\\(.*\\),\\1,p' ${FILE}` 
fi
CATIN="$CATIN ${CATEGORIES//;/ }"
if [ -z "$CATIN" ]; then 
  case "${FILE%/*}" in
   */opt/kde3/*) CATIN="Qt KDE" ;;
   */usr/share/gnome*) CATIN="GTK" ;;
  esac
fi
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
  if [ -f $RPM_BUILD_ROOT/opt/kde3/share/doc/HTML/en/$APPLICATION/index.docbook ] ; then
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

if [ "$I18N" = "no" ]; then
  #
  # this file will not get translated
  #
  sed -i -e '/^\[Desktop Entry\]/a \
X-SuSE-translate=false' $FILE
fi
