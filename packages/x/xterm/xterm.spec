#
# spec file for package xterm
#
# Copyright (c) 2022 SUSE LLC
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


%define splitbin 0%{?suse_version} >= 1300

Name:           xterm
Version:        377
Release:        0
Summary:        The basic X terminal program
License:        MIT
Group:          System/X11/Utilities
URL:            https://invisible-island.net/xterm/xterm.html
Source:         https://invisible-mirror.net/archives/xterm/xterm-%{version}.tgz
Source1:        https://invisible-mirror.net/archives/xterm/xterm-%{version}.tgz.asc
Source2:        luitx
Source3:        Backarrow2Delete
Source4:        Backarrow2BackSpace
Source5:        README.SUSE
Source6:        terminal.png
Source8:        20x20ja.bdf.bz2
Source9:        20x20ko.bdf.bz2
Source11:       xterm.keyring
# Snoop for the escape sequence assignment of the keypad
Source20:       snooper.tar.bz2
Patch1:         xterm-suse.patch
Patch2:         xterm-sigwinch.patch
Patch3:         xterm-double_width_fonts.patch
Patch4:         xterm-desktop_file_icon.patch
Patch5:         xterm-forbid_window_and_font_ops.patch
Patch6:         xterm-enable_libtinfo.patch
Patch7:         xterm-allow_iso-utf_fonts_in_menu.patch
Patch8:         xterm-decomposed_bitmaps.patch
Patch9:         xterm-desktop-item-in-gnome-utilities-appfolder.patch
BuildRequires:  groff
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
Provides:       XFree86:%{_prefix}/X11R6/bin/xterm
Provides:       xorg-x11:%{_prefix}/X11R6/bin/xterm
%if %{splitbin}
Requires:       %{name}-bin
%endif
%if 0%{?suse_version} > 1220
BuildRequires:  fontpackages-devel
%endif
BuildRequires:  bdftopcf
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
Requires:       luit
Recommends:     xorg-x11-fonts-legacy
%if 0%{?suse_version} > 1220
%reconfigure_fonts_prereq
%endif

%description
%if %{splitbin}
This package contains the basic X.Org terminal program desktop launcher.

%package bin
Summary:        The basic X terminal program
Group:          System/X11/Utilities
Requires:       xterm-resize = %{version}-%{release}

%description bin
%endif
This package contains the basic X.Org terminal program.

%package resize
Summary:        Set environment and terminal settings to current window size
Group:          System/X11/Utilities

%description resize
Prints a shell command for setting the appropriate environment variables to
indicate the current size of the window from which the command is run.

%prep
%autosetup -p1
cp -t . %{SOURCE8} %{SOURCE9}
bunzip2 %{basename:%{SOURCE8}} %{basename:%{SOURCE9}}

%build
%define xappdefs   %{_datadir}/X11/app-defaults
%define xfontsd    %{_datadir}/fonts
%define xterminfo  /usr/lib/X11%{_sysconfdir}

%configure \
    --enable-256-color \
    --enable-dec-locator \
    --enable-hp-fkeys \
    --enable-luit \
    --enable-mini-luit \
    --enable-sco-fkeys \
    --enable-wide-chars \
    --with-utempter \
    --with-tty-group=tty \
    --with-app-defaults=%{xappdefs} \
    --enable-backarrow-is-erase \
    --enable-sixel-graphics \

#ensure we do not lose FreeType support (boo#911683)
grep "#define XRENDERFONT 1" xtermcfg.h
%make_build

if ! which bdftopcf &> /dev/null; then exit 1; fi
for i in *.bdf
do
    bdftopcf "$i" | gzip -n -9 >"${i%.bdf}.pcf.gz"
done

%install
%make_install

mkdir -p %{buildroot}%{xterminfo}
install -m 644 terminfo %{buildroot}%{xterminfo}/xterm.terminfo
install -m 644 termcap  %{buildroot}%{xterminfo}/xterm.termcap

install -m 755 $RPM_SOURCE_DIR/luitx %{buildroot}%{_bindir}
install -m 755 $RPM_SOURCE_DIR/Backarrow2Delete %{buildroot}%{_bindir}
install -m 755 $RPM_SOURCE_DIR/Backarrow2BackSpace %{buildroot}%{_bindir}
install -m 644 $RPM_SOURCE_DIR/README.SUSE .

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 $RPM_SOURCE_DIR/terminal.png \
    %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{xfontsd}/misc/
install -m 644 *.pcf.gz %{buildroot}%{xfontsd}/misc/
%suse_update_desktop_file -i xterm TerminalEmulator

%if 0%{?suse_version} > 1220
%reconfigure_fonts_scriptlets
%endif

%files
%{_datadir}/applications/xterm.desktop
%{_datadir}/pixmaps/*

%if %{splitbin}
%files bin
%endif
%doc README README.i18n README.SUSE
%{_bindir}/luitx
%attr(755,root,root) %{_bindir}/xterm
%{_bindir}/uxterm
%{_bindir}/koi8rxterm
%{_bindir}/Backarrow2Delete
%{_bindir}/Backarrow2BackSpace
%{_mandir}/man1/xterm.1.gz
%{_mandir}/man1/koi8rxterm.1.gz
%{_mandir}/man1/uxterm.1.gz
%dir %{xterminfo}
%{xterminfo}/xterm.termcap
%{xterminfo}/xterm.terminfo
%dir %{xfontsd}/misc
%{xfontsd}/misc/20x20ja.pcf.gz
%{xfontsd}/misc/20x20ko.pcf.gz
%dir %{xappdefs}
%{xappdefs}/KOI8RXTerm
%{xappdefs}/KOI8RXTerm-color
%{xappdefs}/UXTerm
%{xappdefs}/UXTerm-color
%{xappdefs}/XTerm
%{xappdefs}/XTerm-color

%files resize
%{_bindir}/resize
%{_mandir}/man1/resize.1*

%changelog
