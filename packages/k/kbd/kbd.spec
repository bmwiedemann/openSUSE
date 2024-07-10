#
# spec file for package kbd
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define legacy_folders amiga,atari,include,mac,pine,ppc,sun

Name:           kbd
Version:        2.6.4
Release:        0
Summary:        Keyboard and Font Utilities
# git: git://git.altlinux.org/people/legion/packages/kbd.git
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Console
URL:            http://kbd-project.org/
# repack_kbd.sh on https://www.kernel.org/pub/linux/utils/kbd/kbd-%%{version}.tar.xz
Source:         %{name}-%{version}-repack.tar.xz
Source2:        suse-add.tar.bz2
Source3:        README.SUSE
Source4:        vlock.pamd
Source8:        sysconfig.console
Source9:        sysconfig.keyboard
Source10:       autogen.sh
Source11:       fbtest.c
Source12:       fbtest.8
Source15:       cz-map.patch
Source20:       kbdsettings
Source21:       kbdsettings.service
Source22:       numlockbios.c
Source42:       convert-kbd-mac.sed
Source43:       repack_kbd.sh
Source44:       xml2lst.pl
Source45:       genmap4systemd.sh
# PATCH-FEATURE-SUSE kbd-1.15.2-unicode_scripts.patch -- To be able to use bold, only fonts with 256 glyphs can be used. Therefore we prefer the font specified in /etc/sysconfig/console.
Patch2:         kbd-1.15.2-unicode_scripts.patch
# PATCH-FIX-SUSE kbd-1.15.2-docu-X11R6-xorg.patch jw@suse.de -- Mention all X11R6 paths in the documentation. Not upstreamable, the documentation is dead and frozen.
Patch3:         kbd-1.15.2-docu-X11R6-xorg.patch
# PATCH-FIX-UPSTREAM kbd-1.15.2-sv-latin1-keycode10.patch jw@suse.de bsc280988 -- It's impossible to press [CTRL]+[]] with sv keyboard. Fix that.
Patch4:         kbd-1.15.2-sv-latin1-keycode10.patch
# PATCH-FIX-UPSTREAM kbd-2.0.2-doshell-reference.patch pgajdos@suse.cz bsc675317 -- Drop doshell reference from openvt.1 man page.
Patch10:        kbd-2.0.2-doshell-reference.patch
# PATCH-FIX-OPENSUSE kbd-2.0.2-euro-unicode.patch pgajdos@suse.cz joehtg@joehtg.co.at boo360993 -- Use Unicode Euro symbol instead of the currency symbol. Not upstreamable as it breaks 8-bit environment using false ISO-8859-1 and ISO-8859-9 naps mapping currency to euro.
Patch11:        kbd-2.0.2-euro-unicode.patch
# PATCH-FIX-OPENSUSE kbd-2.0.2-fix-bashisms.patch ledest@gmail.com -- Fix bash specific code.
Patch12:        kbd-2.0.2-fix-bashisms.patch
# PATCH-FEATURE-SUSE kbd-1.15.5-loadkeys-search-path.patch openSUSE FATE#318355 sle FATE#318426 sndirsch@suse.com -- Add xkb and legacy keymaps subdirs to loadkyes search path.
Patch13:        kbd-1.15.5-loadkeys-search-path.patch
# PATCH-FEATURE-OPENSUSE kbdsettings-nox86.patch sbrabec@suse.cz -- Disable "bios" option for NumLock settings on non x86 platforms.
Patch14:        kbdsettings-nox86.patch
# PATCH-FIX-SLE kbd-unicode-fxxx.patch sbrabec@suse.com bsc1085432 -- Do not cause error on UNICODE characters >= 0xF000 (e. g. ligature fi)
Patch15:        kbd-unicode-fxxx.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  console-setup
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc >= 4.6
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  suse-module-tools
BuildRequires:  xkeyboard-config
BuildRequires:  xz
Requires(post): coreutils
Requires(postun): coreutils
Requires(pre):  %fillup_prereq
Provides:       vlock = 2.2.3
Obsoletes:      vlock <= 2.2.3
# Keymaps moved from kbd-legacy to kbd (bsc#1194609) after SLE15 SP6, Leap 15.6 before ALP 1.0
Conflicts:      kbd-legacy < %{version}

%description
Load and save keyboard mappings. This is needed if you are not using
the US keyboard map. This package also contains utilities for changing
your console fonts. If you install this package, YaST includes an extra
menu to allow you to choose between the different fonts. This package
also includes fonts from the kbd_fonts.tar.gz package (by Paul
Gortmaker) on Sunsite.

%package legacy
Summary:        Legacy data for kbd package
Group:          System/Console
BuildArch:      noarch

%description legacy
The %{name}-legacy package contains original keymaps for kbd package.
Please note that %{name}-legacy is not helpful without kbd.

%define kbd %{_datadir}/kbd

%prep
%setup -q -a 2 -n kbd-%{version}

cp -fp %{SOURCE8} .
cp -fp %{SOURCE9} .
cp -fp %{SOURCE10} .
cp -fp %{SOURCE44} .
cp -fp %{SOURCE45} .
cp -fp %{SOURCE20} .
cp -fp %{SOURCE21} .
cp -fp %{SOURCE22} .
%autopatch -p1
%ifarch %{ix86} x86_64
%patch -P 14 -p1 -R
%endif

%build
for i in `find data/keymaps/mac -type f` ; do
sed -i -f %{SOURCE42} $i
done
# workaround ambiguous keymap names
pushd data/keymaps/i386
	# bnc#48301
	test -f qwerty/se-latin1.map || cp qwerty/sv-latin1.map qwerty/se-latin1.map
	# bnc#435121
	test -f olpc/es-olpc.map || mv olpc/es.map olpc/es-olpc.map
	# Rename conflicting keymaps, as Fedora do
	#test -f dvorak/no.map || mv dvorak/no.map dvorak/no-dvorak.map
	test -f fgGIod/trf.map || mv fgGIod/trf.map fgGIod/trf-fgGIod.map
	test -f olpc/pt.map || mv olpc/pt.map olpc/pt-olpc.map
	test -f qwerty/cz.map || mv qwerty/cz.map qwerty/cz-qwerty.map
popd
chmod 755 autogen.sh
./autogen.sh
%configure \
	--disable-silent-rules \
	--datadir=%{kbd} \
	--enable-nls \
	--localedir=%{_datadir}/locale \
	--enable-optional-progs \
	--disable-static
make %{?_smp_mflags}
gcc %{optflags} -o fbtest      $RPM_SOURCE_DIR/fbtest.c
%ifarch %{ix86} x86_64
gcc %{optflags} -o numlockbios $RPM_SOURCE_DIR/numlockbios.c
%endif
# fix lat2-16.psfu (bnc#340579)
font=data/consolefonts/lat2a-16.psfu
./src/psfxtable -i $font -it  data/unimaps/lat2u.uni \
	-o t.psfu
mv t.psfu $font
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sbindir}
DOC=%{buildroot}%{_defaultdocdir}/kbd
KBD=%{kbd}
K=%{buildroot}$KBD
mkdir -p $DOC/fonts
# Now call kbd install
echo "# Now call kbd install DESTDIR=%{buildroot} DATA_DIR=%{kbd} MAN_DIR=%{_mandir}"
make DESTDIR=%{buildroot} DATA_DIR=%{kbd} MAN_DIR=%{_mandir} install
# ln -s iso01-12x22.psfu $K/consolefonts/suse12x22.psfu
install -m 644 data/consolefonts/README* $DOC/fonts/
mkdir -p $DOC/doc/
install -m 644 docs/doc/keysyms.h.info docs/doc/kbd.FAQ.txt docs/doc/kbd.FAQ*.html docs/doc/README* docs/doc/TODO $DOC/doc/
install -m 644 docs/doc/as400.kbd docs/doc/console.docs docs/doc/repeat/set_kbd_repeat-2 $DOC/doc/
echo "See %{_datadir}/i18/charmaps for a description of char maps" >$DOC/doc/README.charmaps
install -m 644 CREDITS README $DOC/
install -m 644 %{SOURCE3} $DOC/
rm -f $K/consolefonts/README* $K/consolefonts/ERRORS.gz
if ls $K/consolefonts/Agafari-* > /dev/null 2>&1; then
  echo "";
  echo "ERROR: Ethiopian Agafari fonts are for noncommercial distribution only."
  echo "please run repack_kbd.sh";
  echo "";
  exit 1
fi
ln -sf us.map.gz $K/keymaps/i386/qwerty/khmer.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/ara.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/ir.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/chinese.map.gz
ln -sf us.map.gz $K/keymaps/i386/qwerty/taiwanese.map.gz
ln -sf sr-cy.map.gz $K/keymaps/i386/qwerty/sr-latin.map.gz
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
FILLUP_DIR=%{buildroot}%{_fillupdir}
mkdir -p $FILLUP_DIR
install -m 644 sysconfig.console $FILLUP_DIR/sysconfig.console
install -m 644 sysconfig.keyboard $FILLUP_DIR/sysconfig.keyboard
%ifnarch %{ix86} x86_64
   rm -f %{buildroot}%{_mandir}/man8/resizecons.8*
%endif
%ifarch %{sparc} m68k
rm -f %{buildroot}%{_mandir}/man8/getkeycodes.8*
rm -f %{buildroot}%{_mandir}/man8/setkeycodes.8*
%endif
install -m 755 fbtest      %{buildroot}%{_sbindir}
%ifarch %{ix86} x86_64
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 755 numlockbios %{buildroot}%{_libexecdir}/%{name}
%endif
%if %{defined _distconfdir}
rm -rf %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/vlock
%else
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/vlock
%endif
install -m 644 %{SOURCE12} %{buildroot}%{_mandir}/man8/
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/sbin
ln -s %{_bindir}/chvt %{buildroot}/bin
ln -s %{_bindir}/clrunimap %{buildroot}/bin
ln -s %{_bindir}/deallocvt %{buildroot}/bin
ln -s %{_bindir}/dumpkeys %{buildroot}/bin
ln -s %{_bindir}/fgconsole %{buildroot}/bin
ln -s %{_bindir}/getunimap %{buildroot}/bin
ln -s %{_bindir}/kbd_mode %{buildroot}/bin
ln -s %{_bindir}/kbdinfo %{buildroot}/bin
ln -s %{_bindir}/kbdrate %{buildroot}/bin
ln -s %{_bindir}/loadkeys %{buildroot}/bin
ln -s %{_bindir}/loadunimap %{buildroot}/bin
ln -s %{_bindir}/mapscrn %{buildroot}/bin
ln -s %{_bindir}/openvt %{buildroot}/bin
ln -s %{_bindir}/outpsfheader %{buildroot}/bin
ln -s %{_bindir}/psfaddtable %{buildroot}/bin
ln -s %{_bindir}/psfgettable %{buildroot}/bin
ln -s %{_bindir}/psfstriptable %{buildroot}/bin
ln -s %{_bindir}/psfxtable %{buildroot}/bin
ln -s %{_bindir}/screendump %{buildroot}/bin
ln -s %{_bindir}/setfont %{buildroot}/bin
ln -s %{_bindir}/setleds %{buildroot}/bin
ln -s %{_bindir}/setlogcons %{buildroot}/bin
ln -s %{_bindir}/setmetamode %{buildroot}/bin
ln -s %{_bindir}/setpalette %{buildroot}/bin
ln -s %{_bindir}/setvesablank %{buildroot}/bin
ln -s %{_bindir}/setvtrgb %{buildroot}/bin
ln -s %{_bindir}/showconsolefont %{buildroot}/bin
ln -s %{_bindir}/showkey %{buildroot}/bin
ln -s %{_bindir}/spawn_console %{buildroot}/bin
ln -s %{_bindir}/spawn_login %{buildroot}/bin
ln -s %{_bindir}/unicode_start %{buildroot}/bin
ln -s %{_bindir}/unicode_stop %{buildroot}/bin
ln -s %{_sbindir}/fbtest %{buildroot}/sbin
%ifnarch %{sparc} m68k
ln -s %{_bindir}/getkeycodes %{buildroot}/bin
ln -s %{_bindir}/setkeycodes %{buildroot}/bin
%endif
%ifarch %{ix86} x86_64
ln -s %{_bindir}/resizecons %{buildroot}/bin
%endif
%endif

# Make sure Perl has a locale where uc/lc works for unicode codepoints
# see e.g. https://perldoc.perl.org/perldiag.html#Wide-character-(U%2b%25X)-in-%25s
export LC_ALL=C.utf-8
# Convert X keyboard layouts to console keymaps
mkdir -p %{buildroot}%{kbd}/keymaps/xkb
perl xml2lst.pl < %{_datadir}/X11/xkb/rules/base.xml > layouts-variants.lst
while read line; do
  XKBLAYOUT=`echo "$line" | cut -d " " -f 1`
  echo "$XKBLAYOUT" >> layouts-list.lst
  XKBVARIANT=`echo "$line" | cut -d " " -f 2`
  ckbcomp "$XKBLAYOUT" "$XKBVARIANT" > /tmp/"$XKBLAYOUT"-"$XKBVARIANT".map
  # fix conversion of lowercase f in de-e1 keymap (boo#1207841)
  if [ "$XKBLAYOUT-$XKBVARIANT" == "de-e1" ]; then
    sed -i 's/^plain keycode 33 = AltGr/plain keycode 33 = +U+0066/' /tmp/"$XKBLAYOUT"-"$XKBVARIANT".map
  fi
  # skip converted layouts which cannot input ASCII (rh#1031848)
  grep -q "U+0041" /tmp/"$XKBLAYOUT"-"$XKBVARIANT".map && \
    gzip -cn9 /tmp/"$XKBLAYOUT"-"$XKBVARIANT".map > %{buildroot}%{kbd}/keymaps/xkb/"$XKBLAYOUT"-"$XKBVARIANT".map.gz
  rm /tmp/"$XKBLAYOUT"-"$XKBVARIANT".map
done < layouts-variants.lst

# Convert X keyboard layouts (plain, no variant)
cat layouts-list.lst | sort -u >> layouts-list-uniq.lst
while read line; do
  ckbcomp "$line" > /tmp/"$line".map
  grep -q "U+0041" /tmp/"$line".map && \
    gzip -cn9 /tmp/"$line".map > %{buildroot}%{kbd}/keymaps/xkb/"$line".map.gz
  rm /tmp/"$line".map
done < layouts-list-uniq.lst

# Rename the converted default fi (kotoistus) layout (rh#1117891)
mv %{buildroot}%{kbd}/keymaps/xkb/fi.map.gz %{buildroot}%{kbd}/keymaps/xkb/fi-kotoistus.map.gz

# Fix converted cz layout - add compose rules (rh#1181581)
gunzip %{buildroot}%{kbd}/keymaps/xkb/cz.map.gz
patch %{buildroot}%{kbd}/keymaps/xkb/cz.map < %{SOURCE15}
rm -f %{buildroot}%{kbd}/keymaps/xkb/cz.map.orig
gzip -n9 %{buildroot}%{kbd}/keymaps/xkb/cz.map

# Generate entries for systemd's /usr/share/systemd/kbd-model-map
mkdir -p  %{buildroot}%{_datadir}/systemd
bash ./genmap4systemd.sh %{buildroot}%{kbd}/keymaps/xkb \
  > %{buildroot}%{_datadir}/systemd/kbd-model-map.xkb-generated

install -m0755 kbdsettings %{buildroot}%{_sbindir}/
install -d %{buildroot}%{_prefix}/lib/systemd/system
install -m0644 kbdsettings.service %{buildroot}%{_prefix}/lib/systemd/system

%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name}

%pre
%{service_add_pre kbdsettings.service}
# move outdated pam.d/*.rpmsave files away
test -f /etc/pam.d/vlock.rpmsave && mv -v /etc/pam.d/vlock.rpmsave /etc/pam.d/vlock.rpmsave.old ||:

%post
%{fillup_only -n console}
%{fillup_only -n keyboard}
# Variables deleted before Leap 15 and SLE 15
%{remove_and_set -n keyboard KEYTABLE COMPOSETABLE}
%ifnarch %{ix86} x86_64
# "bios" was accepted but ingnored on non-x86 platforms up to Leap 42.* and SLE 12.*
sed -i 's/^KBD_NUMLOCK="bios"/KBD_NUMLOCK="no"/' /etc/sysconfig/keyboard
%endif
%{service_add_post kbdsettings.service}
%{?regenerate_initrd_post}

%preun
%{service_del_preun kbdsettings.service}

%postun
%{service_del_postun kbdsettings.service}
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}
# Migration to /usr/etc.
test -f /etc/pam.d/vlock.rpmsave && mv -v /etc/pam.d/vlock.rpmsave /etc/pam.d/vlock ||:

%files -f %{name}.lang
#config(noreplace) /etc/sysconfig/console
%license COPYING
%doc %{_defaultdocdir}/kbd
#doc CREDITS README
%{_fillupdir}/sysconfig.console
%{_fillupdir}/sysconfig.keyboard
%dir %{kbd}
%{kbd}/consolefonts
%{kbd}/consoletrans
%dir %{kbd}/keymaps
%{kbd}/keymaps/xkb
%{kbd}/unimaps
%exclude %{kbd}/keymaps/{%{legacy_folders}}
%if 0%{?suse_version} < 1550
/sbin/fbtest
/bin/chvt
/bin/openvt
/bin/deallocvt
/bin/dumpkeys
%ifnarch %{sparc} m68k
/bin/getkeycodes
/bin/setkeycodes
%endif
/bin/fgconsole
/bin/kbd_mode
/bin/kbdinfo
/bin/loadkeys
/bin/loadunimap
/bin/mapscrn
/bin/psfaddtable
/bin/psfgettable
/bin/psfstriptable
/bin/psfxtable
%ifarch %{ix86} x86_64
/bin/resizecons
%endif
/bin/setfont
/bin/setleds
/bin/setmetamode
/bin/setvtrgb
/bin/showconsolefont
/bin/showkey
/bin/unicode_start
/bin/unicode_stop
/bin/kbdrate
/bin/clrunimap
/bin/getunimap
/bin/outpsfheader
/bin/screendump
/bin/setlogcons
/bin/setpalette
/bin/setvesablank
/bin/spawn_console
/bin/spawn_login
%endif
%{_sbindir}/fbtest
%{_bindir}/chvt
%{_bindir}/openvt
%{_bindir}/deallocvt
%{_bindir}/dumpkeys
%ifnarch %{sparc} m68k
%{_bindir}/getkeycodes
%{_bindir}/setkeycodes
%endif
%{_bindir}/fgconsole
%{_bindir}/kbd_mode
%{_bindir}/kbdinfo
%{_bindir}/loadkeys
%{_bindir}/loadunimap
%{_bindir}/mapscrn
%{_bindir}/psfaddtable
%{_bindir}/psfgettable
%{_bindir}/psfstriptable
%{_bindir}/psfxtable
%ifarch %{ix86} x86_64
%{_bindir}/resizecons
%endif
%{_bindir}/setfont
%{_bindir}/setleds
%{_bindir}/setmetamode
%{_bindir}/setvtrgb
%{_bindir}/showconsolefont
%{_bindir}/showkey
%{_bindir}/unicode_start
%{_bindir}/unicode_stop
%{_bindir}/kbdrate
%{_bindir}/clrunimap
%{_bindir}/getunimap
%{_bindir}/outpsfheader
%{_bindir}/screendump
%{_bindir}/setlogcons
%{_bindir}/setpalette
%{_bindir}/setvesablank
%{_bindir}/spawn_console
%{_bindir}/spawn_login
%{_bindir}/vlock
%ifarch %{ix86} x86_64
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/numlockbios
%endif
%{_mandir}/man1/*
%{_mandir}/man5/keymaps.5%{ext_man}
%ifnarch %{sparc} m68k
%{_mandir}/man8/getkeycodes.8%{ext_man}
%{_mandir}/man8/setkeycodes.8%{ext_man}
%endif
%{_mandir}/man8/showconsolefont.8%{ext_man}
%{_mandir}/man8/loadunimap.8%{ext_man}
%{_mandir}/man8/mapscrn.8%{ext_man}
%ifarch %{ix86} x86_64
%{_mandir}/man8/resizecons.8%{ext_man}
%endif
%{_mandir}/man8/setfont.8%{ext_man}
%{_mandir}/man8/fbtest.8%{ext_man}
%{_mandir}/man8/kbdrate.8%{ext_man}
%{_mandir}/man8/clrunimap.8%{ext_man}
%{_mandir}/man8/getunimap.8%{ext_man}
%{_mandir}/man8/mk_modmap.8%{ext_man}
%{_mandir}/man8/setlogcons.8%{ext_man}
%{_mandir}/man8/setvesablank.8%{ext_man}
%{_mandir}/man8/setvtrgb.8%{ext_man}
%{_mandir}/man8/vcstime.8%{ext_man}
%if %{defined _distconfdir}
%{_pam_vendordir}/vlock
%else
%config(noreplace) %{_sysconfdir}/pam.d/vlock
%endif
%dir %{_datadir}/systemd
%{_prefix}/lib/systemd/system/kbdsettings.service
%{_datadir}/systemd/kbd-model-map.xkb-generated
%{_sbindir}/kbdsettings
# Move legacy keymaps that have no acceptable xkb counterpart to kbd. (bsc#1194609)
%dir %{kbd}/keymaps/i386
%dir %{kbd}/keymaps/i386/include
%dir %{kbd}/keymaps/i386/qwerty
%{kbd}/keymaps/i386/qwerty/gr.map.gz
%{kbd}/keymaps/i386/qwerty/ruwin_alt-UTF-8.map.gz
%{kbd}/keymaps/i386/qwerty/tj_alt-UTF8.map.gz
%{kbd}/keymaps/i386/qwerty/ua-utf.map.gz
%{kbd}/keymaps/i386/include/linux-keys-bare.inc
%{kbd}/keymaps/i386/include/linux-with-alt-and-altgr.inc
%{kbd}/keymaps/i386/include/compose.inc
%{kbd}/keymaps/i386/include/qwerty-layout.inc

%files legacy
%{kbd}/keymaps/{%{legacy_folders},i386}
%exclude %dir %{kbd}/keymaps/i386
%exclude %dir %{kbd}/keymaps/i386/include
%exclude %dir %{kbd}/keymaps/i386/qwerty
%exclude %{kbd}/keymaps/i386/qwerty/gr.map.gz
%exclude %{kbd}/keymaps/i386/qwerty/ruwin_alt-UTF-8.map.gz
%exclude %{kbd}/keymaps/i386/qwerty/tj_alt-UTF8.map.gz
%exclude %{kbd}/keymaps/i386/qwerty/ua-utf.map.gz
%exclude %{kbd}/keymaps/i386/include/linux-keys-bare.inc
%exclude %{kbd}/keymaps/i386/include/linux-with-alt-and-altgr.inc
%exclude %{kbd}/keymaps/i386/include/compose.inc
%exclude %{kbd}/keymaps/i386/include/qwerty-layout.inc

%changelog
