# RPM macros for Tcl

# The minor version of Tcl
%tcl_version %(echo 'puts [info tclversion]'|tclsh)

# compiled packges should go here
%tcl_archdir %(echo 'puts [lindex $tcl_pkgPath 0]'|tclsh)

# script-only packages should go here
%tcl_noarchdir %(echo 'puts [lindex  $tcl_pkgPath 1]'|tclsh)

# tclscriptdir is deprecated, please use tcl_archdir or
# tcl_noarchdir instead, depending on the type of your package
%tclscriptdir %tcl_noarchdir
