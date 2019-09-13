#! /bin/sh
# Shell script helper to activate tuxcursors.
#
# Same license as enclosing package.
# 2008-10-07, jw@suse.de

if [ "$1" = "-help" -o "$1" = "-h" -o "$1" = "--help" ]; then
  echo $0
  echo "Simple wrapper script to help with activating the tuxcursors mouse scheme."
  echo "If called without parameters, this script will try to bring up a dialog"
  echo "that allows you to change your cursor settings."
  echo ""
  echo "Improvements welcome."
  exit 0;
fi

if [ -n "$KDE_SESSION_UID" ]; then
  kcmshell mouse;
else
  cat << EOF
  No KDE_SESSION_UID -> dialog for mouse cursor change unknown.
  Please try to navigate your desktop menues.
KDE menu style:

-> Personal Settings (Configure Desktop)
 -> Hardware
  -> Mouse
   -> Cursor Theme -> tuxcursors

Other menues:

Try the search box with 'mouse'.

EOF
fi
exit
