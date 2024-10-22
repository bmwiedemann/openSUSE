#
# spec file for package qodem
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           qodem
Version:        1.0.1
Release:        0
Summary:        Terminal emulator and communications package
License:        CC0-1.0 OR SUSE-Public-Domain
Group:          Hardware/Modem
URL:            https://qodem.sourceforge.io/index.html
#Git-Clone:     https://gitlab.com/AutumnMeowMeow/qodem.git
Source:         https://sourceforge.net/projects/qodem/files/qodem/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gpm-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl)
# * qodem runs in any terminal (and visually, linedrawing characters are fine
#   with most fonts)
# * xqodem however (just) spawns an xterm with terminus and 8-bit mode or so
Requires:       terminus-bitmap-fonts
Requires:       xterm

%description
Qodem is a re-implementation of the Qmodem
shareware communications package, updated for more modern uses.
Major features include:
 * Unicode display: translation of CP437 (PC VGA), VT100 DEC
   Special Graphics characters, VT220 National Replacement
   Character sets, etc., to Unicode
 * Terminal interface conveniences: scrollback buffer, capture
   file, screen dump, dialing directory, keyboard macros, script
   support
 * Connection methods: serial, local shell, command line, telnet,
   ssh, rlogin, rsh
 * Emulations: ANSI.SYS (including "ANSI music"), Avatar, VT52,
   VT100/102, VT220, Linux, and XTerm
 * Transfer protocols: Xmodem, Ymodem, Zmodem, and Kermit

%prep
%autosetup -p1
# Remove bundled stuff
rm -f intl/gettext.c
rm -rf lib/{c,cryptlib,upnp}

%build
autoreconf -fiv
%configure \
  --disable-x11 \
  --disable-upnp
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog CREDITS FILE_ID.DIZ README.md
%{_bindir}/qodem
%{_bindir}/xqodem
%{_mandir}/man1/qodem.1%{?ext_man}
%{_mandir}/man1/xqodem.1%{?ext_man}

%changelog
