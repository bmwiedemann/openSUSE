#
# spec file for package mc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           mc
Version:        4.8.33
Release:        0
Summary:        Midnight Commander
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://midnight-commander.org/
Source0:        http://ftp.midnight-commander.org/mc-%{version}.tar.xz
Source1:        x11_browser
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        cmake.syntax
Source6:        http://ftp.midnight-commander.org/%{name}-%{version}.sha256
Source7:        mc.fish
Patch0:         mc-fix_lib_search_path.patch
Patch12:        mc-wrapper.patch
Patch16:        mc-esc-seq.patch
Patch20:        mc-f-keys.patch
Patch21:        mc-extfs-helpers-deb.patch
# add patch. bnc#856501
# http://www.midnight-commander.org/ticket/3128
Patch22:        mc-vfs-fish-deleted_source_file.patch
#Debian fixes
Patch32:        20_wrong_path_to_wrappers.patch
# PATCH-FIX-UPSTREAM mc-multi-press-f-keys.patch mc287 sbrabec@suse.cz - Fixed Esc + Numeral F-key emulation.
Patch41:        mc-multi-press-f-keys.patch
# PATCH-FIX-UPSTREAM 4258-fish-subshell-prompt.patch https://midnight-commander.org/ticket/4258 mcepl@suse.com
# don't send \r while printing prompt
Patch42:        4258-fish-subshell-prompt.patch
# Patches from Fedora
#Patch adding -fpie and -pie to compilation and linking of setuid binaries
Patch52:        mc-pie.patch
Patch62:        mc-extd-video.patch
Patch63:        mc-extd-doc.patch
Patch64:        mc-extd-sound.patch
Patch69:        mc-extd-xdg.patch
Patch71:        mc-ext-audio.patch
# PATCH-FEATURE-OPENSUSE mc-ext-obscpio.patch bsc#1233006 mcepl@suse.com
# mc can now handle SUSE *.obscpio archives
Patch72:        mc-ext-obscpio.patch
Patch100:       xls2csv_update.patch
BuildRequires:  audiofile-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gettext >= 0.18.1
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  gpm-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRequires:  slang-devel
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  xz
BuildRequires:  pkgconfig(x11)
Requires(pre):  permissions
Recommends:     %{name}-lang = %{version}
Enhances:       fish
Recommends:     xorriso

%description
GNU Midnight Commander (also referred to as MC) is a user shell much
like the (in)famous Norton Commander with text-mode full-screen
interface. It can be run on the OS console, in xterm and other
terminal emulators.

GNU Midnight Commander allows you to manage files while making most of
your screen and giving you a clear representation of the filesystem, yet
it's simple enough to be run over a telnet or ssh session.

MC needs several other programs for its various extfs extensions, e.g.
isoinfo (from mkisofs) or xorriso for the iso:// extension.

%lang_package

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE6} | head -n1 | cut -c1-64`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
%{?!make_build:%define make_build make -O %_smp_mflags V=1 VERBOSE=1}
autoreconf -fvi
%define warn_flags -W -Wall -Wstrict-prototypes -Wpointer-arith -Wformat-security -Wno-unused-parameter
export CFLAGS="%{optflags} %{warn_flags}"

export X11_WWW="%{_datadir}/mc/x11_browser"

export PYTHON=%{_bindir}/python3

%configure \
    --localstatedir=%{_localstatedir}/lib \
    --enable-charset \
    --disable-vfs-fish

%make_build

%install
%make_install

# clean up this setuid problem for now
chmod 755 %{buildroot}/%{_libexecdir}/mc/cons.saver

install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/mc/syntax/

#install the shell functions for bourne shell and csh
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
ln -fs -t %{buildroot}%{_sysconfdir}/profile.d %{_datadir}/mc/mc.{,c}sh
#support script for calling available GUI webbrosers
install -m 755 %{SOURCE1} %{buildroot}%{_datadir}/mc/
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/pixmaps/
ln -s ../icons/hicolor/32x32/apps/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Fish wrapper script
install -D -m 644 %{SOURCE7} \
    %{buildroot}%{_datadir}/fish/vendor_functions.d/mc.fish

for f in ext.d/misc.sh ext.d/sound.sh ext.d/video.sh \
    extfs.d/gitfs+ extfs.d/uace extfs.d/uarc ;
do
    sed -i -e '1s@bin/sh@bin/bash@' "%{buildroot}%{_libexecdir}/mc/${f}"
done

%suse_update_desktop_file -i %{name} System FileManager
# Remove not supported language
rm -rf  %{buildroot}%{_datadir}/locale/be@tarask

%find_lang %{name}
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_libexecdir}/mc/extfs.d/*
%endif

%post
%set_permissions %{_libexecdir}/mc/cons.saver

%verifyscript
%verify_permissions -e %{_libexecdir}/mc/cons.saver

%files
%doc ABOUT-NLS NEWS README
%license COPYING
%config %{_sysconfdir}/profile.d/*
%{_bindir}/mc*
%dir %{_sysconfdir}/mc/
%config %{_sysconfdir}/mc/filehighlight.ini
%config %{_sysconfdir}/mc/sfs.ini
%config %{_sysconfdir}/mc/mc.menu
%config %{_sysconfdir}/mc/mc.ext.ini
%config %{_sysconfdir}/mc/mcedit.menu
%config %{_sysconfdir}/mc/mc.keymap
%config %{_sysconfdir}/mc/mc.default.keymap
%config %{_sysconfdir}/mc/mc.emacs.keymap
%config %{_sysconfdir}/mc/mc.vim.keymap
%config %{_sysconfdir}/mc/edit.indent.rc
%dir %{_libexecdir}/mc
%{_libexecdir}/mc/ext.d
%{_libexecdir}/mc/extfs.d
%{_libexecdir}/mc/shell
%verify(not mode) %{_libexecdir}/mc/cons.saver
%exclude %{_mandir}/*/man1/*
%{_mandir}/man1/*
%{_datadir}/mc
%exclude %{_datadir}/mc/hints/mc.hint.*
%exclude %{_datadir}/mc/help/mc.hlp.*
%exclude %{_datadir}/locale/*/LC_MESSAGES/mc.mo

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/mc.fish

%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files lang -f %{name}.lang
%lang(es) %{_mandir}/es/man1/mc.1.gz
%lang(hu) %{_mandir}/hu/man1/mc.1.gz
%lang(it) %{_mandir}/it/man1/mc.1.gz
%lang(pl) %{_mandir}/pl/man1/mc.1.gz
%lang(ru) %{_mandir}/ru/man1/mc.1.gz
%if 0%{?suse_version} < 1600 && 0%{?is_opensuse}
%lang(sr) %dir %{_mandir}/sr
%lang(sr) %dir %{_mandir}/sr/man1
%endif
%lang(sr) %{_mandir}/sr/man1/mc.1.gz

%lang(be) %doc %{_datadir}/mc/*/mc.*.be
%lang(bg) %doc %{_datadir}/mc/*/mc.*.bg
%lang(ca) %doc %{_datadir}/mc/*/mc.*.ca
%lang(cs) %doc %{_datadir}/mc/*/mc.*.cs
%lang(da) %doc %{_datadir}/mc/*/mc.*.da
%lang(de) %doc %{_datadir}/mc/*/mc.*.de
%lang(el) %doc %{_datadir}/mc/*/mc.*.el
%lang(en_GB) %doc %{_datadir}/mc/*/mc.*.en_GB
%lang(eo) %doc %{_datadir}/mc/*/mc.*.eo
%lang(es) %doc %{_datadir}/mc/*/mc.*.es
%lang(et) %doc %{_datadir}/mc/*/mc.*.et
%lang(eu) %doc %{_datadir}/mc/*/mc.*.eu
%lang(fa) %doc %{_datadir}/mc/*/mc.*.fa
%lang(fr) %doc %{_datadir}/mc/*/mc.*.fr
%lang(ga) %doc %{_datadir}/mc/*/mc.*.ga
%lang(gl) %doc %{_datadir}/mc/*/mc.*.gl
%lang(hu) %doc %{_datadir}/mc/*/mc.*.hu
%lang(id) %doc %{_datadir}/mc/*/mc.*.id
%lang(it) %doc %{_datadir}/mc/*/mc.*.it
%lang(ja) %doc %{_datadir}/mc/*/mc.*.ja
%lang(ka) %doc %{_datadir}/mc/*/mc.*.ka
%lang(ko) %doc %{_datadir}/mc/*/mc.*.ko
%lang(lt) %doc %{_datadir}/mc/*/mc.*.lt
%lang(nb) %doc %{_datadir}/mc/*/mc.*.nb
%lang(nl) %doc %{_datadir}/mc/*/mc.*.nl
%lang(pl) %doc %{_datadir}/mc/*/mc.*.pl
%lang(pt) %doc %{_datadir}/mc/*/mc.*.pt
%lang(pt_BR) %doc %{_datadir}/mc/*/mc.*.pt_BR
%lang(ro) %doc %{_datadir}/mc/*/mc.*.ro
%lang(ru) %doc %{_datadir}/mc/*/mc.*.ru
%lang(sk) %doc %{_datadir}/mc/*/mc.*.sk
%lang(sr) %doc %{_datadir}/mc/*/mc.*.sr
%lang(sv) %doc %{_datadir}/mc/*/mc.*.sv
%lang(tr) %doc %{_datadir}/mc/*/mc.*.tr
%lang(uk) %doc %{_datadir}/mc/*/mc.*.uk
%lang(zh_CN) %doc %{_datadir}/mc/*/mc.*.zh_CN
%lang(zh_TW) %doc %{_datadir}/mc/*/mc.*.zh_TW

%changelog
