
CFILES="
deprecated/management/applets/apparmorapplet-gnome/src/apparmor-applet.c
deprecated/management/applets/apparmorapplet-gnome/src/preferences_dialog.c
deprecated/management/applets/apparmorapplet-gnome/src/reject_list.c
parser/parser_alias.c
parser/parser_include.c
parser/parser_interface.c
parser/parser_lex.l
parser/parser_main.c
parser/parser_merge.c
parser/parser_misc.c
parser/parser_policy.c
parser/parser_regex.c
parser/parser_symtab.c
parser/parser_variable.c
parser/parser_yacc.y
"

CPPFILES="
deprecated/management/profile-editor/src/AboutDialog.cpp
deprecated/management/profile-editor/src/AboutDialog.h
deprecated/management/profile-editor/src/Configuration.cpp
deprecated/management/profile-editor/src/Preferences.cpp
deprecated/management/profile-editor/src/Preferences.h
deprecated/management/profile-editor/src/profileeditor.cpp
deprecated/management/profile-editor/src/SearchAllProfiles.cpp
deprecated/management/profile-editor/src/SearchAllProfiles.h
parser/libapparmor_re/regexp.yy
"

PERLFILES="
utils/aa-repo.pl
utils/audit
utils/autodep
utils/complain
utils/enforce
utils/genprof
utils/logprof
utils/Reports.pm
utils/SubDomain.pm
utils/unconfined
"

ARGS="--keyword=_ --keyword=N_ -n --force-po"

xgettext $ARGS --output=apparmor-C.pot -L C $CFILES
xgettext $ARGS --output=apparmor-CPP.pot -L C++ $CPPFILES
xgettext $ARGS --output=apparmor-PERL.pot -L Perl $PERLFILES
msgcat apparmor-*.pot > apparmor.pot

sed  \
  -e 's/Project-Id-Version: PACKAGE VERSION/Project-Id-Version: apparmor/g' \
  -e 's/PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE/PO-Revision-Date: 2009-02-05 13:38/' \
  -e 's/Report-Msgid-Bugs-To: /Report-Msgid-Bugs-To: apparmor-general@forge.novell.com/' \
  -e 's/Last-Translator: FULL NAME <EMAIL@ADDRESS>/Last-Translator: Novell Language <language@novell.com>/' \
  -e 's/Language-Team: LANGUAGE <LL@li.org>/Language-Team: Novell Language <language@novell.com>/' \
  -e 's/Content-Type: text\/plain; charset=CHARSET/Content-Type: text\/plain; charset=UTF-8/' \
  < apparmor.pot > apparmor.pot.new
  mv apparmor.pot.new apparmor.pot

for file in $(find . -name '*.po'); do
	f=$(basename $file)
	msgmerge -U apparmor.pot $file
	if [ -e "po/$f" ]; then
		msgcat $file po/$f > $f
		mv $f po/$f
	else
		cp $file po/$f
	fi
done
