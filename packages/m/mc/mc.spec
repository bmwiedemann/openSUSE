#
# spec file for package mc
#
# Copyright (c) 2023 SUSE LLC
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
Version:        4.8.29
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
# changed mc-extfs-iso9660-xorriso.patch
# to reflect upstream fix
Patch23:        mc-extfs-iso9660-xorriso.patch
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
Patch61:        mc-extd-misc.patch
Patch62:        mc-extd-video.patch
Patch63:        mc-extd-doc.patch
Patch64:        mc-extd-sound.patch
Patch69:        mc-extd-xdg.patch
Patch71:        mc-ext-audio.patch
Patch100:       xls2csv_update.patch
BuildRequires:  audiofile-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gettext >= 0.18.1
BuildRequires:  glib2-devel >= 2.26.0
BuildRequires:  gpm-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRequires:  slang-devel
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-devel
BuildRequires:  xz
Requires(pre):  permissions
Recommends:     %{name}-lang = %{version}
Enhances:       fish
Recommends:     mkisofs
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
%setup -q
%patch0
%patch61
%patch62
%patch63
%patch64
%patch69
%patch71 -p1
%patch12 -p1
%patch16
%patch20
%patch21
%patch22 -p1
%patch23
%patch32
%patch41 -p1
%patch42 -p1
%patch52 -p1
%patch100 -p1

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
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

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

%post
%if 0%{?suse_version} >= 1140
%set_permissions %{_libexecdir}/mc/cons.saver
%else
%run_permissions
%endif

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
%config %{_sysconfdir}/mc/edit.indent.rc
%dir %{_libexecdir}/mc
%{_libexecdir}/mc/ext.d
%{_libexecdir}/mc/extfs.d
%verify(not mode) %{_libexecdir}/mc/cons.saver
%exclude %{_mandir}/*/man1/*
%{_mandir}/man1/*
%{_datadir}/mc
%{_datadir}/mc/syntax/Syntax
%{_datadir}/mc/mc.charsets
%{_datadir}/mc/mc.lib
%exclude %{_datadir}/mc/hints/mc.hint.*
%{_datadir}/mc/hints/mc.hint
%exclude %{_datadir}/mc/help/mc.hlp.*
%{_datadir}/mc/help/mc.hlp
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
%if 0%{?suse_version} < 1140 || 0%{?sles_version} && 0%{?sles_version} <= 11
%lang(sv) %dir %{_datadir}/locale/sv_SE
%lang(sv) %dir %{_datadir}/locale/sv_SE/LC_MESSAGES
%lang(szl) %dir %{_datadir}/locale/szl
%lang(szl) %dir %{_datadir}/locale/szl/LC_MESSAGES
%endif

%lang(hu) %dir %{_mandir}/hu/
%lang(hu) %dir %{_mandir}/hu/man1/
%lang(hu) %{_mandir}/hu/man1/mc.1.gz

%lang(pl) %dir %{_mandir}/pl/
%lang(pl) %dir %{_mandir}/pl/man1/
%lang(pl) %{_mandir}/pl/man1/mc.1.gz

%lang(sr) %dir %{_mandir}/sr/
%lang(sr) %dir %{_mandir}/sr/man1/
%lang(sr) %{_mandir}/sr/man1/mc.1.gz

%lang(cs) %doc %{_datadir}/mc/*/mc.*.cs
%lang(es) %doc %{_datadir}/mc/*/mc.*.es
%lang(hu) %doc %{_datadir}/mc/*/mc.*.hu
%lang(it) %doc %{_datadir}/mc/*/mc.*.it
%lang(nl) %doc %{_datadir}/mc/*/mc.*.nl
%lang(pl) %doc %{_datadir}/mc/*/mc.*.pl
%lang(ru) %doc %{_datadir}/mc/*/mc.*.ru
%lang(sr) %doc %{_datadir}/mc/*/mc.*.sr
%lang(uk) %doc %{_datadir}/mc/*/mc.*.uk

%changelog
