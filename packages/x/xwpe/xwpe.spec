#
# spec file for package xwpe
#
# Copyright (c) 2026 Juan Manuel Méndez Rey <juan.mendezr@proton.me>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           xwpe
Version:        1.6.6
Release:        0
Summary:        Borland-style programming environment and editor for console and X11
License:        GPL-2.0-only
URL:            https://codeberg.org/mendezr/xwpe
# Upstream "make dist" tarball attached to the Codeberg release for this tag;
# it unpacks to the standard name-version directory and already ships configure.
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-glib
BuildRequires:  gpm-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vterm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(zlib)

# Owns the /usr/share/icons/hicolor directory tree the icons drop into.
Requires:       hicolor-icon-theme

# Tools the IDE shells out to at runtime (F9 compile, Ctrl-G debug). Pulled in
# by default but not hard requirements -- the editor runs without them.
Recommends:     gcc
Recommends:     gcc-c++
Recommends:     gdb
Recommends:     gpm

%description
xwpe (the X Windows Programming Environment) is a programming and text editor
in the style of the Borland Turbo C IDE of the early 1990s -- written by Fred
Kruse in 1993, maintained by Dennis Payne from 2000 to 2006, and revived in
2026. A single binary runs in four modes chosen by the program name: wpe and
we in the console (ncurses), xwpe and xwe under X11 with anti-aliased Xft/Cairo
rendering, UTF-8 and color emoji.

It pairs a syntax-highlighting editor with a Borland-style menu and dialog
system, project management, compiler integration for many languages (C/C++,
Fortran, Pascal, Java, Python, Perl, COBOL, LaTeX) and source-level debugging
through gdb, jdb and pdb.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

# The info dir index is owned by the info system, not by this package.
rm -f %{buildroot}%{_infodir}/dir

desktop-file-validate %{buildroot}%{_datadir}/applications/xwpe.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/io.codeberg.mendezr.xwpe.metainfo.xml

%check
make check

%files
%license COPYING
%doc README.md CHANGELOG AUTHORS
%{_bindir}/we
%{_bindir}/wpe
%{_bindir}/xwe
%{_bindir}/xwpe
%dir %{_libdir}/xwpe
%{_libdir}/xwpe/help.key
%{_libdir}/xwpe/help.xwpe
%{_libdir}/xwpe/syntax_def
%{_datadir}/applications/xwpe.desktop
# Own the scalable theme dirs: the build always installs the SVG into
# hicolor/scalable/apps, and openSUSE's hicolor-icon-theme does not own them
# (the sized PNG dirs, when rsvg-convert is present, are owned by the theme).
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/*/apps/xwpe.*
%{_datadir}/metainfo/io.codeberg.mendezr.xwpe.metainfo.xml
%{_mandir}/man1/we.1%{?ext_man}
%{_mandir}/man1/wpe.1%{?ext_man}
%{_mandir}/man1/xwe.1%{?ext_man}
%{_mandir}/man1/xwpe.1%{?ext_man}
%{_infodir}/xwpe.info%{?ext_info}

%changelog