#
# spec file for package kbd (Version 1.12)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           kbd
URL:            ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/utils/kbd
License:        GPL v2 or later
Group:          System/Console
Autoreqprov:    on
Version:        1.12
Release:        132
Summary:        Keyboard and Font Utilities
Source:         ftp://ftp.win.tue.nl/pub/home/aeb/linux-local/utils/kbd/%{name}-%{version}.tar.bz2
Source1:        kbd_fonts.tar.bz2
Source2:        suse-add.tar.bz2
Source3:        README.SuSE
Source4:        kbd.init
Source5:        kbd.fillup
Source6:        kbd.fillup.nonpc
Source8:        sysconfig.console
Source9:        sysconfig.keyboard
Source10:       testutf8.c
Source42:       convert-kbd-mac.sed
Source43:       repack_kbd.sh
Patch:          kbd-%{version}.diff
Patch2:         kbd-%{version}-prtscr_no_sigquit.diff
Patch3:         kbd-%{version}-swiss.diff
Patch4:         kbd-%{version}-Meta-Tab.diff
Patch5:         kbd-%{version}-noclaudio.diff
Patch6:         kbd-%{version}-nohang-kbdrate2.diff
Patch7:         kbd-%{version}-loadkeys-repstdout.diff
Patch8:         kbd-%{version}-mac-dk.diff
Patch9:         kbd-%{version}-dumpkeys-full.diff
Patch10:        kbd-%{version}-dumpkeys-ppc.diff
Patch11:        kbd-%{version}-mac-de.diff
Patch12:        kbd-%{version}-handle-small-table.diff
Patch13:        kbd-%{version}-unicode_scripts.diff
Patch14:        kbd-%{version}-cz-us-qwertz.diff
Patch15:        kbd-%{version}-nounicode-nontty.diff
Patch16:        kbd-%{version}-kbd_mode.diff
Patch17:        piofont_debug.diff
Patch18:        kbd-%{version}-loadkeys-C-opt.diff
Patch19:        kbd-%{version}-happy-abuild.diff
Patch20:        kbd-%{version}-strip.diff
Patch21:        kbd-%{version}-setfont-fpclose.diff
Patch22:        kbd-%{version}-showconsolefont-info.diff
Patch23:        kbd-%{version}-docu-X11R6-xorg.diff
Patch24:        kbd-%{version}-el-locale-update.diff
Patch25:        sv-latin1-keycode10.diff
Patch26:        kbd-%{version}-setfont-no-cruft.diff
Patch27:        kbd-%{version}-be-nice-to-kdm.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %fillup_prereq %insserv_prereq
BuildRequires:  bison flex

%description
Load and save keyboard mappings. This is needed if you are not using
the US keyboard map. This package also contains utilities for changing
your console fonts. If you install this package, YaST includes an extra
menu to allow you to choose between the different fonts. This package
also includes fonts from the kbd_fonts.tar.gz package (by Paul
Gortmaker) on Sunsite.



Authors:
--------
    Andries Brouwer <aeb@cwi.nl>

%define kbdrate_in_util %(rpm -ql util 2>/dev/null | grep -s /sbin/kbdrate && echo "1" || echo "0"; exit 0)
%define kbd /usr/share/kbd
%prep
%if %{kbdrate_in_util}
  echo "kbdrate is in util"
%endif
%setup -q -a 1 -a 2 -n kbd-%{version}
%patch -p1 -E
# choose-tty.diff went upstream, 27.2.2004, jw
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24
%patch25 -p1
%patch26 -p1
# %patch27 -p1		# obsoleted. #302010

%build
for i in `find data/keymaps/mac -type f` ; do
sed -i -f %{S:42} $i
done
# bugzilla #33301, but noclobber.
(cd data/keymaps/i386/qwerty; test -f se-latin1.map || cp sv-latin1.map se-latin1.map)
./configure --prefix=/ --datadir=%{kbd} --mandir=%{_mandir}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os"
gcc $RPM_OPT_FLAGS -o testutf8 $RPM_SOURCE_DIR/testutf8.c

%install
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/sbin
#mkdir -p $RPM_BUILD_ROOT/usr/bin
#mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/init.d
DOC=${RPM_BUILD_ROOT}%{_defaultdocdir}/kbd
KBD=%{kbd}
K=$RPM_BUILD_ROOT$KBD
mkdir -p $K/consolefonts
# First install the fonts from the vfont package 
# (allowing kbd to overwrite some of them)
mkdir -p $DOC/fonts
install -m 644 fonts/README $DOC/fonts/README.fonts
install -m 644 fonts/vfont-4.36/README $DOC/fonts/README.vfont-4.36
install -m 644 fonts/vfont-5.10/README $DOC/fonts/README.vfont-5.10
install -m 644 fonts/vfont-5.10/SCRIPT $DOC/fonts/SCRIPT.vfont-5.10
rm -f fonts/vfont-5.10/SCRIPT fonts/*/README
install -m 644 fonts/*/* $K/consolefonts/
# Now call kbd install
echo "# Now call kbd install DESTDIR=$RPM_BUILD_ROOT DATA_DIR=%{kbd} MAN_DIR=%{_mandir}"
make DESTDIR=$RPM_BUILD_ROOT DATA_DIR=%{kbd} MAN_DIR=%{_mandir} install
# ln -s iso01-12x22.psfu $K/consolefonts/suse12x22.psfu
install -m 644 data/consolefonts/README* $DOC/fonts/
mkdir -p $DOC/doc/
install -m 644 doc/keysyms.h.info doc/kbd.FAQ.txt doc/kbd.FAQ*.html doc/README* doc/TODO $DOC/doc/
install -m 644 doc/as400.kbd doc/console.docs doc/repeat/set_kbd_repeat-2 $DOC/doc/
echo "See /usr/share/i18/charmaps for a description of char maps" >$DOC/doc/README.charmaps
install -m 644 COPYING CHANGES CREDITS README $DOC/
install -m 644 %SOURCE3 $DOC/
rm -f $K/consolefonts/README* $K/consolefonts/ERRORS.gz
if ls $K/consolefonts/Agafari-* > /dev/null 2>&1; then
  echo "";
  echo "ERROR: Ethiopian Agafari fonts are for noncommercial distribution only."
  echo "please run repack_kbd.sh";
  echo "";
  exit 1
fi
install -m 755 %SOURCE4 $RPM_BUILD_ROOT/etc/init.d/kbd
ln -sf ../etc/init.d/kbd $RPM_BUILD_ROOT/sbin/rckbd
ln -sf us.map.gz $K/keymaps/i386/qwerty/khmer.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/korean.map.gz
# Compatability links; don't know what the first three are good for.
# The others are for yast/langselection and should be removed as soon as
# yast knows about it.
#ln -sf de-latin1-nodeadkeys.map.gz \
#  $K/keymaps/i386/qwertz/de-lat1-nd.map.gz
#ln -sf ru1.map.gz $K/keymaps/i386/qwerty/russian.map.gz
#ln -sf sg-latin1-lk450.map.gz \
#  $K/keymaps/i386/qwertz/sg-l1-lk450.map.gz
# The next two links are for yast-language choise; should be obsolete
# with the next yast version (on 6.1)
#ln -sf lat1-16.psfu.gz $K/consolefonts/lat1u-16.psf.gz
#ln -sf lat2-16.psfu.gz $K/consolefonts/lat2u-16.psf.gz
#
# This is for stupid default font search
rm -f $K/consolefonts/default8x16.gz
ln -sf default8x16.psfu.gz $K/consolefonts/default8x16.gz
#
rm -f $K/keymaps/i386/qwerty/*~ $K/keymaps/i386/qwerty/*,v
#
# this is until the Cyr* font are not part of the package
rm -f $K/consolefonts/Cyr_a8x14.gz
ln -sf Cyr_a8x14.psfu.gz $K/consolefonts/Cyr_a8x14.gz
rm -f $K/consolefonts/Cyr_a8x16.gz
ln -sf Cyr_a8x16.psfu.gz $K/consolefonts/Cyr_a8x16.gz
rm -f $K/consolefonts/Cyr_a8x8.gz
ln -sf Cyr_a8x8.psfu.gz $K/consolefonts/Cyr_a8x8.gz
#
find $K -name \*.orig | xargs -r rm -vf
# add some missing maps to mac and remap french board
(
cd $K/keymaps/mac/all
pwd
#ln -s mac-fr-latin1.map.gz mac-fr_CH-latin1.map.gz
#ln -s mac-fr-latin1.map.gz mac-fr.map.gz
for i in \
	mac-es.map.gz \
	mac-it.map.gz \
	mac-pt-latin1.map.gz \
	mac-br-abnt2.map.gz \
	mac-gr.map.gz \
	mac-dk-latin1.map.gz \
	mac-no-latin1.map.gz \
	mac-fi-latin1.map.gz \
	mac-cz-us-qwertz.map.gz \
	mac-hu.map.gz \
	mac-Pl02.map.gz \
	mac-ru1.map.gz \
	mac-jp106.map.gz
do test -f $i || ln -sv mac-us.map.gz $i
done
)
FILLUP_DIR=$RPM_BUILD_ROOT/var/adm/fillup-templates
mkdir -p $FILLUP_DIR
install -m 644 %SOURCE8 $FILLUP_DIR/sysconfig.console
install -m 644 %SOURCE9 $FILLUP_DIR/sysconfig.keyboard
%ifarch %ix86 alpha ia64 x86_64
cat %SOURCE5 >> $FILLUP_DIR/sysconfig.keyboard
%else
cat %SOURCE6 >> $FILLUP_DIR/sysconfig.keyboard
%endif
#mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
#touch $RPM_BUILD_ROOT/etc/sysconfig/console
%ifnarch %ix86
   rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/resizecons.8*
%endif
%ifarch sparc m68k
rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/getkeycodes.8*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/setkeycodes.8*
%endif
install -m 755 ./testutf8 $RPM_BUILD_ROOT/bin/

%post
%{fillup_and_insserv -npy console kbd}
%{fillup_only -n keyboard}
#echo "Please read the docu about the new COMPOSETABLE rc.config variable."
#echo "See /etc/sysconfig/console, /etc/sysconfig/keyboard"
#echo "and %{_docdir}/kbd/README.SuSE."

%postun
%{insserv_cleanup}

%files
%defattr(-,root,root)
#%config(noreplace) /etc/sysconfig/console
%doc %{_defaultdocdir}/kbd
#%doc COPYING CHANGES README CREDITS
%config /etc/init.d/kbd
/var/adm/fillup-templates/sysconfig.console
/var/adm/fillup-templates/sysconfig.keyboard
%dir %{kbd}
%{kbd}
/usr/share/locale/*/LC_MESSAGES/kbd.mo
/sbin/rckbd
/bin/chvt
/bin/openvt
/bin/deallocvt
/bin/dumpkeys
%ifnarch sparc m68k
/bin/getkeycodes
/bin/setkeycodes
%endif
/bin/fgconsole
/bin/kbd_mode
/bin/loadkeys
/bin/loadunimap
/bin/mapscrn
/bin/psfaddtable
/bin/psfgettable
/bin/psfstriptable
/bin/psfxtable
%ifarch %ix86
/bin/resizecons
%endif
/bin/setfont
/bin/setleds
/bin/setmetamode
/bin/showconsolefont
/bin/showkey
/bin/unicode_start
/bin/unicode_stop
%if ! %{kbdrate_in_util}
/bin/kbdrate
%doc %{_mandir}/man8/kbdrate.8.gz
%endif
/bin/testutf8
%doc %{_mandir}/man1/chvt.1.gz
%doc %{_mandir}/man1/deallocvt.1.gz
%doc %{_mandir}/man1/dumpkeys.1.gz
%doc %{_mandir}/man1/kbd_mode.1.gz
%doc %{_mandir}/man1/loadkeys.1.gz
%doc %{_mandir}/man1/psfaddtable.1.gz
%doc %{_mandir}/man1/psfgettable.1.gz
%doc %{_mandir}/man1/psfstriptable.1.gz
%doc %{_mandir}/man1/psfxtable.1.gz
%doc %{_mandir}/man1/setleds.1.gz
%doc %{_mandir}/man1/setmetamode.1.gz
%doc %{_mandir}/man1/showkey.1.gz
%doc %{_mandir}/man1/fgconsole.1.gz
%doc %{_mandir}/man5/keymaps.5.gz
%ifnarch sparc m68k
%doc %{_mandir}/man8/getkeycodes.8.gz
%doc %{_mandir}/man8/setkeycodes.8.gz
%endif
%doc %{_mandir}/man8/showconsolefont.8.gz
%doc %{_mandir}/man8/loadunimap.8.gz
%doc %{_mandir}/man8/mapscrn.8.gz
%ifarch %ix86
%doc %{_mandir}/man8/resizecons.8.gz
%endif
%doc %{_mandir}/man8/setfont.8.gz
%doc %{_mandir}/man1/openvt.1.gz
%doc %{_mandir}/man1/unicode_start.1.gz
%doc %{_mandir}/man1/unicode_stop.1.gz

%clean
rm -rf $RPM_BUILD_ROOT
#rm -rf $RPM_BUILD_DIR/kbd-%{version}

%changelog
* Tue Aug 21 2007 - jw@suse.de
- cleaned up setfont according to bugzilla #302010
* Thu Aug 16 2007 - jw@suse.de
- fixed fix of bugzilla #300076
  (fillup_and_insserv is too ugly)
* Tue Aug 14 2007 - jw@suse.de
- fixed /etc/sysconfig/keyboard, bugzilla #300076
* Tue Jul 17 2007 - jw@suse.de
- fixed sv-latin1.map, bugzilla #280988
* Thu Jun 21 2007 - dmueller@suse.de
- update 'el' localisation
* Mon Jun 18 2007 - jw@suse.de
- sleep 3 removed. bugzilla #284348
* Sat Jun 16 2007 - coolo@suse.de
- as discussed with jw and werner kbd does not need to run before
  xdm
* Fri May 11 2007 - olh@suse.de
- do not run setfont on ps3 because it permanently blanks the screen
* Thu Mar 29 2007 - coolo@suse.de
- BuildRequire flex and bison
* Wed Feb 07 2007 - ro@suse.de
- do not build as root
* Mon Oct 23 2006 - olh@suse.de
- update mac-de []|{} mapping to match the X11 and MacOS mapping
* Fri Aug 11 2006 - jw@suse.de
- mention both /usr/share/X11 and /usr/X11R6/lib/X11 in docu.
* Wed Jul 26 2006 - jw@suse.de
- added showconsolefont-info.diff,
  partial fix for #164378
* Wed Jun 21 2006 - jw@suse.de
- added some pclose(), fixing (#88501)
* Tue Jun 06 2006 - jw@suse.de
- $MAGIC should have been $CONSOLE_MAGIC (#181612)
* Wed May 31 2006 - jw@suse.de
- added consolefonts/cp850-full-* (#179528)
  derived from cp850 via setfont; loadunimap cp850; setfont -O
* Tue Apr 25 2006 - jw@suse.de
- added keymaps/i386/qwerty/cn-latin1.map (#158951)
* Sun Apr 02 2006 - olh@suse.de
- make Alt/Option key and Command/Apple key consistent with X11
  in the mac-* keymaps: flip them
* Mon Mar 20 2006 - ms@suse.de
- added korean console keyboard link ( korean -> us ) (#87443)
* Tue Feb 07 2006 - ms@suse.de
- added khmer console keyboard link ( khmer -> us )
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 13 2006 - schwab@suse.de
- Don't strip binaries.
* Sun Oct 02 2005 - schwab@suse.de
- Remove useless distinction between different machines when finding the
  keymap.
* Mon Aug 15 2005 - jw@suse.de
- mac: fixed support for pc style keymaps
  bugzilla#98363
* Thu Aug 04 2005 - jw@suse.de
- sourcing /etc/profile.d/lang.sh for new dynamic language config
* Tue Jul 12 2005 - jw@suse.de
- removed Agafari fonts from source tar ball.
  bugzilla#95915
* Thu Jul 07 2005 - jw@suse.de
- revamped uninitialized.diff into happy-abuild.diff
  added declarations, added RPM_OPT_FLAGS where it was still missing.
* Mon May 23 2005 - jw@suse.de
- removing noncommercial Agafari fonts during install.
* Tue May 17 2005 - jw@suse.de
- used uninitialized fixed.
* Fri May 13 2005 - jw@suse.de
- convert-kbd-mac.sed: changed 58 from 100 to 125, to enable altgr
  thanks to olh.
* Thu Mar 31 2005 - jw@suse.de
- avoid probing of all /dev/$tty on *iseries*, as it causes
  -ENODEV errors. #74394
* Mon Mar 14 2005 - jw@suse.de
- new init script logic: earlykbd + kbd should now behave
  as werner designed it (using /var/run/keymap as lock).
  Fixes #65246, #71722, #72409 and possibly #65970
* Tue Mar 08 2005 - jw@suse.de
- magic printing second try.
  Better diagnostics to tackle #65246
* Fri Mar 04 2005 - jw@suse.de
- less obstrusive magic printing from kbd.init [fixes #65119]
- loadkeys, setfont: neither annoy X-Servers nor print
  bogus error messages [fixes #63713, and possibly #65246]
* Tue Dec 14 2004 - coolo@suse.de
- adding an early boot script to load the cache created by last
  boot.
* Mon Oct 25 2004 - jw@suse.de
- new cz-lat2-us.map added, fixing #46829
* Thu Sep 30 2004 - jw@suse.de
- #45972 fixed: missing usbhid module added.
- #46113 workaround: wrong write to /proc/sys/kernel/hotplug removed.
- debug printf for unreproducable PIO_FONT error added.
* Wed Sep 08 2004 - werner@suse.de
- Faster boot: skip setleds if nothing is switched on and skip
  not needed virtual consoles
* Mon Sep 06 2004 - werner@suse.de
- More speed for the boot script by checking the vt's only once
* Wed Mar 31 2004 - jw@suse.de
- Bugzilla #37619: force-reload was missing in kbd.init
* Tue Mar 30 2004 - mfabian@suse.de, werner@suse.de
- Bugzilla #37367: add option "-C device" to kbd_mode and
  change /etc/init.d/kbd script to be able to set the mode for
  all console. Previously it worked only on the first console
  (/dev/tty1).
* Tue Mar 30 2004 - jw@suse.de
- iso09.f16n.psf from toganm@dinamizm.com added.
  That fixes bugzilla #37247
* Wed Mar 03 2004 - ro@suse.de
- fix typo in kbd rcscript
* Fri Feb 27 2004 - jw@suse.de
- upgrade to 1.12
  * updated getkeycodes, showkey for Linux 2.6 (fixing #33978)
  * maps updated: is-latin1.map, is-latin1-us.map, bg-cp1251.map,
  bg_bds-cp1251.map, bg_pho-cp1251.map, bg_bds-utf8.map,
  bg_pho-utf8.map, nl.map
  * renamed bg.map to bg-cp855.map
  * fonts: greek-polytonic.psfu
  * translations updated: pl.po, ro.po, cs.po, es.po, gr.po, es.po,
  nl.po, el.po, pl.po
  * new options: -C, openvt -e,
  * docu updates.
- fixed #33301, swedish map renamed
* Sat Nov 08 2003 - olh@suse.de
- add convert-kbd-mac.sed to convert mac maps to 2.6 linuxkeycodes
  load usb drivers unconditionally in runlevel S
* Thu Oct 30 2003 - schwab@suse.de
- /etc/init.d/kbd: usbdevfs has been renamed to usbfs, use /proc/bus/usb
  instead.
* Fri Oct 17 2003 - kukuk@suse.de
- Really delete wrong manual pages
* Fri Oct 17 2003 - kukuk@suse.de
- Fix filelist for SPARC
* Wed Oct 01 2003 - garloff@suse.de
- #31927: kbdrate was not called due to wrong path. Fixed.
- unicode_start: Collapse to one setfont call (as in initscript).
* Fri Sep 19 2003 - garloff@suse.de
- #31153: kbd_mode -a/-u is not good under X11. Skip unicode_start/
  stop dir non-tty devices.
- Collapse setfont calls for font, unimap and screenmap into one.
  Otherwise the font is overridden with default8x16 again.
* Tue Sep 16 2003 - garloff@suse.de
- Fix bug #30097: When switching from cz-us-qwertz to us, y and
  z could be confused.
* Tue Sep 16 2003 - garloff@suse.de
- Add compose table compose.utf8 that uses symbolic names and thus
  works regardless of encoding. Most useful for UTF-8.
- Fix bug #28481: We were writing the activation string to a read-
  only fd.
* Thu Sep 11 2003 - mfabian@suse.de
- Bugzilla #30411: redirect "plus before udiaeresis ignored" and
  similar warnings of "loadkeys --unicode" in Unicode_start
  to /dev/null.
- Bugzilla #30496: don't write file to remember the keyboard
  map to /.kbd/.keymap_sv.
- add program "testutf8" by Gerd Knorr <kraxel@suse.de> to be able
  to check whether a terminal is in UTF-8 mode or not.
* Tue Sep 09 2003 - mfabian@suse.de
- Bugzilla #28720: "kbd_mode", "setfont", and "fgconsole" have
  moved from /usr/bin/ -> /bin. Therefore, /etc/init.d/kbd
  stopped working correctly (I thought I had fixed #28720 before
  but because these binaries moved it broke again).
* Sun Sep 07 2003 - mfabian@suse.de
- save the old keymap in "unicode_start" and reload it in
  "unicode_stop" because "dumpkeys | loadkeys --unicode" cannot
  be reverted.
* Tue Sep 02 2003 - mmj@suse.de
- Add sysconfig metadata [#28855]
* Thu Jul 31 2003 - kukuk@suse.de
- serial was renamed to setserial [Bug #28353]
* Thu Jul 31 2003 - garloff@suse.de
- Fix dumpkeys fix [#28339].
* Thu Jul 31 2003 - garloff@suse.de
- Fix various DESTDIR ... related Makefile headaches
- Port patches to 1.08, all binaries have been moved to /bin
- Tentative fix for dumpkeys, using the large NR_KEYS from 2.6
  kernel but running on 2.4 [#28339]
- Use RPM_OPT_FLAGS (with -Os appended)
* Wed Jul 30 2003 - garloff@suse.de
- Update to kbd-1.08:
  * loadkeys: fix for bison 1.50
  * Makefile cleanups
  * Patch to not map PrtScr to Ctrl-\ (but only Ctrl-PrtScr) merged
  * fi-latin1/9.map changed
  * bg-cp1251.map, il-heb.map, sr-cy.map, fr-latin9.map
- Update to kbd-1.07:
  * showfont -> showconsolefont rename (clash with X)
  * loadkeys fixes: addfunc(), relative symlinks
  * getfd: Try devfs names as well
  * manpgae for fgconsole
  * cyr-sun16.psfu
  * swedish: rename to se-latin1.map to sv-latin1.map
  * cp1251_to_uni, koi8-r_to_uni, koi8-u_to_uni.trans
  * se-fi-* for Northern Sami
  * nl3.map -> nl.map
* Fri Jun 06 2003 - mfabian@suse.de
- fix Bugzilla #27141: add the necessary commands to setup the
  Linux consoles for Unicode or non-Unicode respectively
  to /etc/init.d/kbd, similar to what is done in
  /usr/sbin/{unicode_start,unicode_stop}.
- remove installed but unpackaged file resizecons.8.gz
* Tue Mar 11 2003 - garloff@suse.de
- Add sysconfig metadata to sysconfig/console as well [Bug #22625]
* Sat Mar 08 2003 - kukuk@suse.de
- Don't reset the status, so that final result does not only
  report the status of the last command [Bug #19823]
* Thu Feb 20 2003 - mmj@suse.de
- Add sysconfig metadata [#22625]
* Tue Feb 18 2003 - kukuk@suse.de
- Don't set KBD_RATE and KBD_DELAY per default
* Sat Dec 07 2002 - garloff@suse.de
- Add compose.latin1.cedilla which is a variant which maps accented
  c to cedilla. [Bug #21008]
- Use alarm(5) to limit waiting for (potentially non-existing) kbd
  controller instead of loop (with machine-dependent timeout).
  [Bug #22167]
* Fri Nov 08 2002 - schwab@suse.de
- Fix mac-de-latin1 keymap.
- Fix misaligned columns in full table dump.
- Don't clobber keycode 0 where it is valid.
* Mon Oct 07 2002 - garloff@suse.de
- Don't write "Loading <file>" to stdout when --mktable is used.
  [Bug #19952]
- Use larger timeout waiting for keyboard controller.
* Wed Sep 18 2002 - fehr@suse.de
- add updated keymaps us-acentos.map and br-abnt2.map provided
  by miura@conectiva.com.br to suse-add.tar.bz2 (Bug #19791)
* Mon Aug 26 2002 - sndirsch@suse.de
- remember NumLock BIOS state in /var/run/numlock-on; required
  later for $HOME/.xinitrc (Bug #18248)
* Sat Aug 24 2002 - olh@suse.de
- do the symlinks really in mac/all
* Mon Aug 19 2002 - garloff@suse.de
- Add %%insserv_prereq and %%fillup_prereq (bug #17892)
* Thu Aug 15 2002 - olh@suse.de
- fix some keys with kbd-1.06-mac-dk.diff
  do the symlinks in mac/all instead of mac/
* Mon Aug 05 2002 - olh@suse.de
- merge boot.setup into rckbd (#16476)
* Fri Jul 26 2002 - garloff@suse.de
- Don't wait infinitely long for bit 1 of port 0x64 being 0.
  Blocker #17248.
- Make loadkeys report successful keytable load to stdout instead
  of stderr. Bug #17168.
* Wed Jul 24 2002 - olh@suse.de
- do not run boot.setup on iSeries by accident, kbdrate is bad
* Fri Jul 19 2002 - olh@suse.de
- kbdrate does only work on PC style hardware, hangs on USB and ADB
* Thu Jul 11 2002 - garloff@suse.de
- Removed dangling link to www.claudio.ch (bug #16933)
* Fri Jul 05 2002 - kukuk@suse.de
- Use %%ix86 macro
* Thu Jul 04 2002 - uli@suse.de
- search for x86-64 keymaps in i386
* Mon Jun 17 2002 - sndirsch@suse.de
- sysconfig.keyboard: set KBD_NUMLOCK to "bios" (Bug #16594)
* Fri Jun 14 2002 - olh@suse.de
- no loadkezs, sane systems have <TAB>
* Fri Jun 14 2002 - sndirsch@suse.de
- boot.setup: handle Numlock depending on BIOS setting
  if KBD_NUMLOCK is set to "bios"
- sysconfig.keyboard: added "bios" to KBD_NUMLOCK description
* Mon Jun 10 2002 - garloff@suse.de
- Convert some missing maps.
* Fri Jun 07 2002 - garloff@suse.de
- Convert Shift Tab to Meta_Tab. (#16512)
* Thu Jun 06 2002 - garloff@suse.de
- Add KBD_DISABLE_CAPS_LOCK feature.
* Thu Jun 06 2002 - garloff@suse.de
- Add kbd rate and delay report (#16050).
- Move fbset to X-SuSE-Should-Start.
* Sun Mar 17 2002 - garloff@suse.de
- Fixed all i386 keymaps with 99(PtrScr) = Control_backslash
  to VoidSymbol (but keeping the old meaning with Control)
  Fixes bug #8380.
* Sun Mar 17 2002 - garloff@suse.de
- Changed init script to accept a keymap that is specified by
  absolute path. (Bug #14997)
* Sun Mar 17 2002 - garloff@suse.de
- Add some missing third (AltGr) functions to the number keys
  for fr_CH/de_CH-latin and sg-latin1. (Adresses bug #9368)
* Tue Mar 12 2002 - olh@suse.de
- load usb keyboard in runlevel s and 1 (#14253)
* Mon Mar 04 2002 - garloff@suse.de
- Add Rumanian keyboard layout (ro-latin2.map) donated by
  Manfred Pohler. (#13008)
* Fri Mar 01 2002 - ro@suse.de
- force activation of boot.setup using "Y"
* Mon Feb 18 2002 - ro@suse.de
- don't clobber return code with test
* Thu Feb 14 2002 - garloff@suse.de
- Revert chvt change by default, as it causes too much flickering
  of the screen. It can be manually enabled though. (#12151)
* Tue Feb 12 2002 - ro@suse.de
- added missing "fi" in boot.setup
* Tue Feb 12 2002 - schwab@suse.de
- Fix uses of chvt in init script.
* Fri Feb 08 2002 - ro@suse.de
- return (not implemented) for stop and (unknown) for status
  in boot.setup
* Fri Feb 08 2002 - garloff@suse.de
- Split /etc/sysconfig/console into keyboard and console.
* Fri Feb 08 2002 - garloff@suse.de
- Move keyboard data to /usr/share (it's not arch dependant)
- Try to make setting console fonts work with non-SuSE kernels
  by using chvt. (bug #12151)
* Fri Feb 08 2002 - garloff@suse.de
- Remove duplicated data, rename conflicting
- Don't map PrtScr to Control_backslash (SIGQUIT) by default,
  Control PrtScr will still produce it. (bug #8380)
- Remove test for "none" ifr unicode and screenmaps ("none" can be
  different from not calling setfont)
- Handle empty KEYTABLE (fixes bug #12976)
- Clarified comments for the various CONSOLE settings
* Fri Feb 08 2002 - garloff@suse.de
- kbd-1.06:
  * Lots of our patches got merged :-)
  * Fonts added
  * lat7u.uni -> iso07u.uni, added lat7.uni
  * Scancode docs removed, see
  http://www.win.tue.nl/~aeb/linux/kbd/scancodes.html
  * various minor corrections
* Wed Feb 06 2002 - werner@suse.de
- Add KBD_SCRLOCK variable to make it possible to enable this
- Move setleds from /usr/bin to /sbin and set compatiblity symlink
  (mainly for infra red keyboards)
* Sat Jan 12 2002 - garloff@suse.de
- Move COMPOSETASBLE to /etc/sysconfig/console, where all the other
  console and keyboard related settings are.
* Wed Jan 09 2002 - ro@suse.de
- fixed typo in boot.setup
* Tue Jan 08 2002 - ro@suse.de
- moved COMPOSETABLE to /etc/sysconfig/keyboard (#12736)
* Thu Dec 13 2001 - ro@suse.de
- moved rc.config.d -> sysconfig
* Tue Dec 11 2001 - schwab@suse.de
- Fix boot script for last change.
* Thu Dec 06 2001 - ro@suse.de
- renamed rc.config.d.kbd to rc.config.d.console
- fixed bug for ppc
* Wed Dec 05 2001 - ro@suse.de
- moved KBD related variables from aaa_base to here
- moved boot.setup from aaa_base to here
- use fillup_and_insserv macro
* Fri Nov 30 2001 - olh@suse.de
- handle the ppc64 in machine detection
* Mon Sep 17 2001 - garloff@suse.de
- Add loadkezs->loadkeys symlink (#10752)
* Sat Sep 01 2001 - olh@suse.de
- no keyboard on iSeries available
* Wed Aug 29 2001 - olh@suse.de
- allow querty/us.map.gz as KEYTABLE, fix mac-dk map
* Wed Aug 08 2001 - olh@suse.de
- handle ppc64 in KBDLIB path as i386
* Mon Aug 06 2001 - kukuk@suse.de
- Fix comment about init script location [Bug #9494]
* Sat Jul 21 2001 - olh@suse.de
- update search path for mac keymaps
* Tue Jul 17 2001 - garloff@suse.de
- changed return value of status to 3 if not running. Fixes
  bug #9052.
* Wed Jul 11 2001 - bjacke@suse.de
- switch , to . on number block for {de,fr}_CH keymaps
* Sun Jun 17 2001 - schwab@suse.de
- setfont: output activation string on selected console, not stdout.
* Fri May 11 2001 - garloff@suse.de
- Remove compose combinations from compose.latin1.add that have
  been merged into the official compose.latin1.
* Fri May 11 2001 - garloff@suse.de
- bzip2 sources.
* Fri May 11 2001 - garloff@suse.de
- Apply fixes to kbd iint script from Werner Fink:
  * Dump keymap to /etc/defkeymap after the compose table has been
  loaded. Do it whenever it changed.
  * In runlevels N, S, 1, we might not have /usr available.
  Don't issue tons of "failed" messages but be happy with
  defkeymap.
* Tue May 08 2001 - garloff@suse.de
- Remove redundant sun keymaps from suse-add.
- Especially remove sunkeymap which reintroduces a fixed bug to kbd
- Remove second .map from sunt4-no-latin1.map.map
* Tue May 08 2001 - garloff@suse.de
- On request of Andries (aeb): Removed the Shift-Ctrl mapping
  of Compose but instead put it on Ctrl-.
- Added compose.ctrlperiod to achieve this.
* Mon May 07 2001 - garloff@suse.de
- Remove double fontwidth assignment (cosmetical)
- Add fbset to init script prerequisites
* Wed May 02 2001 - garloff@suse.de
- Fix bug #7474: (defkeymap)
  keycode 97 = Control Compose is wrong. Use shift keycode ...
- Make Shift-Ctrl and Ctrl-Shift behave the same
- bzip2 the suse_add sources instead of gzip
* Wed Apr 25 2001 - garloff@suse.de
- Corrections to the file list:
  * Install fg_console
  * Install unicode_start/stop plus manpages
  * Don't install resizecons/manpage on non-i386 archs
* Tue Apr 24 2001 - garloff@suse.de
- correct y <-> z in mac-de_CH has erroneously been removed from
  last patch. Corrected.
* Tue Apr 24 2001 - garloff@suse.de
- Use KBD_TTY to determine which consoles need to be manipulated,
  not non-functional /dev/tty[1-24].
* Tue Apr 24 2001 - garloff@suse.de
- Add some sun keymaps from console-data to suse_add. (#6109)
- Add original sun12x22.psfu and suse12x22 under its true name.
* Mon Apr 23 2001 - garloff@suse.de
- Finalized merging with 1.05: SuSE patch shrinked from 116k to
  9k :-)
- fillup now defaults to clear the compose table in case one is
  loaded and gives some more examples.
- Set font on all consoles /dev/tty[1-24] (bugzilla #5812)
- install kbd_fonts before kbd, so the latter has the possibility
  to overwrite/update the fonts from the kbd_fonts pack
* Sun Apr 22 2001 - bjacke@suse.de
- correct y <-> z in mac-de_CH
- add mac_dvorak keymap
- move de_CH from qwerty to qwertz
* Fri Apr 20 2001 - garloff@suse.de
- Update to kbd-1.0.5 which incorporates the patches from olh and
  me.
* Fri Mar 16 2001 - ro@suse.de
- create directory sbin in buildroot
* Sun Dec 17 2000 - garloff@suse.de
- Fix lat5 fonts
- ShiftCtrl now leaves the Ctrl scancodes untouched and just
  changes the ShiftCtrl meaning to Compose.
* Wed Dec 13 2000 - olh@suse.de
- use runlevel S and mount proc with -n
* Fri Dec 08 2000 - schwab@suse.de
- Use extended compose table also on ia64.
- Fix typos.
* Thu Dec 07 2000 - werner@suse.de
- Add begin and end mark of LSB header
- Move chvt, openvt, deallocvt to /bin and set link bak to /usr/bin
* Wed Dec 06 2000 - garloff@suse.de
- Argh: loadkeys does not merge the compose table; just the key
  definitions. Make compose.latin1.add include compose.latin1 and
  update docu accordingly to account for this.
* Wed Dec 06 2000 - garloff@suse.de
- Also include the mapping of the compose key in the COMPOSEMAP
  variable and offer winkeys and shiftctrl. Default on i386 and
  alpha.
- Update README.SuSE to document this.
- This together with the changes from Dec 4 should address the
  problems with some keytables (bug #4275).
* Tue Dec 05 2000 - olh@suse.de
- add mac-fr_CH.map
* Mon Dec 04 2000 - garloff@suse.de
- New startup script: Separate KEYMAP from COMPOSE maps. Add new
  rc.config variable COMPOSEMAP to allow setting of compose combi-
  nations defaulting to "latin1 latin1.add"
- Disable the formerly patched in inclusion of compose maps in
  the keymaps, as we have a proper separation now.
* Mon Dec 04 2000 - garloff@suse.de
- Add de_CH ("schwyzerdütsch") keymap.
- Initialize consoles 1-24 (instead of 1-6) with CONSOLE_MAGIC
  (Bugzilla #4468)
* Tue Nov 28 2000 - kukuk@suse.de
- New initscript in /etc/init.d
* Fri Oct 20 2000 - kukuk@suse.de
- Fix filelist on SPARC
* Thu Oct 05 2000 - olh@suse.de
- remove mac-de2-ext.map, obsolete
* Thu Oct 05 2000 - olh@suse.de
- check for /proc/cpuinfo before mounting proc
* Tue Sep 12 2000 - olh@suse.de
- mount proc on ppc, needed for runlevel S
* Tue Aug 22 2000 - olh@suse.de
- update spec file and use only one dif, add mac-pt map, fix maps
* Sat Aug 05 2000 - garloff@suse.de
- Only include kbdrate in kbd package, if it's not already in util
  If not, install it in /sbin, just like util did before.
- Remove the README files and ERRORS from /usr/lib/kbd/consolefonts
* Fri Aug 04 2000 - kukuk@suse.de
- Add support for PS/2 keyboards and serial console on SPARC
* Tue Aug 01 2000 - garloff@suse.de
- Update to version 1.03wip adding support for a PSF format and
  UTF8, including sequences.
- Apply old patches; split in mac keytables and general patch
- Add support for fonts wider than 8 pixels
- Map compose key (W*n95 Menu Key and Shift-RightCtrl) and include
  additional compose combinations for i386 us and de keymaps
- Add suse12x22.psf font to suse-add.tar.gz and remove fonts, map,
  transtables that are already included in 1.03wip.
- Add %%clean section to spec file
- Install more docu and move font specific docu to a subdir
- Add README.SuSE
* Mon Jul 03 2000 - olh@suse.de
- merge keymaps from 6.4 for mac, be,it,de_CH,fi,dk
* Tue Jun 06 2000 - olh@suse.de
- fix mac specific links to nonexistant maps,
  add mac/include to search path
* Wed May 31 2000 - werner@suse.de
- Import script code from boot.setup which is kbd specific
- User new rc.status shell functions
- Move S20kbd to S10kbd (after nfs import init)
* Thu May 25 2000 - olh@suse.de
- update us-map, get rid of misnamed maps
  use includes for mac-*
* Mon May 08 2000 - wede@suse.de
- suse-add: Lithuanian console fonts and mappings added:
  /usr/lib/kbd/consolefonts/lat7.psf.gz
  /usr/lib/kbd/consolefonts/lt-brim-8x14.psfu.gz
  /usr/lib/kbd/consoletrans/lt-brim.uni
- kbd.spec: use of %%{_defaultdocdir}
* Sun Apr 30 2000 - olh@suse.de
- update mac-fr.map
* Wed Apr 05 2000 - olh@suse.de
- fix link to french mac map
* Tue Mar 28 2000 - olh@suse.de
- use Buildroot
  add some dummy maps for mac
* Mon Mar 20 2000 - kukuk@suse.de
- suse-add: Add more sun keymaps
* Thu Mar 16 2000 - schwab@suse.de
- kbd.rc: Use i386 keymaps also on ia64 and alpha.
* Tue Feb 29 2000 - werner@suse.de
- Close first part of bug #592
  * Search with shell tools not with find
  * Dump /etc/defkeymap.map if not exists
  * Use /etc/defkeymap.map as a fallback if no keymap is found
- Move loadkeys from /usr/bin/ to /bin/ and set a symbolic link
  for backward compatibility
- Add openvt to the file list
* Sun Feb 27 2000 - kukuk@suse.de
- Move /usr/man -> /usr/share/man
* Thu Dec 09 1999 - olh@suse.de
- Added i386 keys to mac-de.map, @|\~
  make Symlink mac -> ppc relative
* Thu Nov 11 1999 - kukuk@suse.de
- kbd.rc: Add support for SPARC.
* Tue Sep 28 1999 - ml@suse.de
- Added symlink keymaps/ppc -> keymaps/mac in specfile.
  Added lat9-[12,14,16].psfu consolefonts to suse_add.tar.gz
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jul 01 1999 - ro@suse.de
- don't try to write /var/run/keymap if mounted ro (closing bug 20)
* Fri Jun 18 1999 - uli@suse.de
- cleaned up patch
* Wed Jun 16 1999 - uli@suse.de
- patched de-latin1.map to allow usage of Euro symbol with
  lat0-* console fonts
* Mon Jun 07 1999 - uli@suse.de
- added br-abnt.map and us-acentos.map to suse-addon
* Tue Apr 13 1999 - ml@suse.de
- added lt.baltic.map to suse-addon
* Sun Apr 11 1999 - ml@suse.de
- added a patch for correct KOI8-U (Ukrainian) support
- added screenmap for baltic to suse-addon
* Tue Apr 06 1999 - ml@suse.de
- added a patch harald könig for us.map
* Mon Apr 05 1999 - ml@suse.de
-switch to version 0.99; main change of package: gettext for nls-support
-changes for us: removes the patches for sk-qwertz and sk-qwerty map
  and the map br-abnt2.map (included now)
-added /usr/share/locale/*/LC_MESSAGES/kbd.mo to the %%files-section
  of the specfile for nls-support
* Thu Mar 11 1999 - ml@suse.de
- Changed to kbd-0.97
- lat2u.uni -> now included -> removed from suse-diff
- Pl02.map included into suse-addons and removed from diff
- Same for br-abnt2.map
- added ru3/4 map to suse-addon
- renamed the suse-iso07-extensions to lat7u.*
- removed #mkdir -p $DOC; #mv $K/consolefonts/README* $DOC/ "
  from specfile; now already included in kbd-0.97-makefile
- added ./configure --datadir (which will be best?)
- european default now lat1-16.psfu -> mantel & fehr
- added Cyr_a*.psf* to suse-addons, removed old Cyr-files and set links
- added cyralt.uni
- patched sk-qwertz and sk-qwerty map
* Mon Feb 01 1999 - ro@suse.de
- resizecons is not built on alpha
* Mon Jan 18 1999 - ml@suse.de
- added finally iso07.uni (missed it on Fri Jan  8 10:28:24 MET 1999)
  To do this, two mv-commands in the spec-file have been added, that move
  iso.07.uni to iso07.uni.old and the new one to iso07.uni
* Wed Jan 13 1999 - ml@suse.de
- added latin2u.scrnmap
- added sk-qwertz.map
* Fri Jan 08 1999 - ml@suse.de
-  added lat2u-16.psf and lat2u.uni
* Fri Jan 08 1999 - rolf@suse.de
- added the following keymaps: br-abnt2, Pl02, sk-qwerty
- added the new version of iso07 fonts with SuSE extensions including
  unicode map file
* Sun Dec 13 1998 - bs@suse.de
- removed /var/adm/setup/setup.fontconfig
* Sat Dec 05 1998 - bs@suse.de
- let start script say, that a "keymap" is loaded.
* Thu Nov 26 1998 - bs@suse.de
- made startup script a little bit smoother (let loadkeys not print
  a long path).
* Thu Nov 19 1998 - bs@suse.de
- fixed second find call.
* Tue Nov 17 1998 - bs@suse.de
- moved loadkeys to /usr/bin again (the kbd package does not work without
  a mounted /usr)
- created /sbin/init.d/kbd
- removed Makefile.Linux - was not used anymore :(
* Thu Oct 29 1998 - ro@suse.de
- output "Loading $KEYMAP" to stdout (not stderr)
* Tue Sep 22 1998 - ro@suse.de
- update to 0.96a
- for glibc define _GNU_SOURCE where getopt is used
* Mon Oct 20 1997 - ro@suse.de
- ready for autobuild
* Tue Jun 03 1997 - bs@suse.de
- removed man page console.4.gz (included in ldpman)
* Sun Apr 13 1997 - florian@suse.de
- update to new version 0.93
- mv documentation to /usr/doc
