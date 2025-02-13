#
# spec file for package syncterm
#
# Copyright (c) 2021 SUSE LLC
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


Name:           syncterm
Version:        1.5
Release:        0
Summary:        An ANSI-BBS terminal which supports telnet, rlogin, and SSH
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://syncterm.net
#Git-Clone:     https://gitlab.synchro.net/main/sbbs.git
Source:         https://master.dl.sourceforge.net/project/syncterm/syncterm/%{name}-%{version}/%{name}-%{version}-src.tgz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  hicolor-icon-theme
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)

%description
An ANSI-BBS terminal designed to connect to remote BBSs via telnet, rlogin, or
SSH. Supports ANSI music and the IBM charset when possible. Will run from a
console, under X11 using XLib, or using SDL.

%prep
%autosetup -p1

%build
%cmake -DWITHOUT_CRYPTLIB=ON
%make_jobs

%install
%cmake_install
# HACK should be fixed upstream
install -d %{buildroot}%{_mandir}/man1/
mv -v %{buildroot}%{_mandir}/syncterm.man %{buildroot}%{_mandir}/man1/syncterm.1

%files
%license src/syncterm/LICENCE src/syncterm/gpl.txt
%doc src/syncterm/CHANGES
%{_bindir}/syncterm
%{_datadir}/applications/syncterm.desktop
%{_datadir}/icons/hicolor/*/apps/syncterm.png
%{_datadir}/icons/hicolor/*/apps/syncterm*.svg
%{_mandir}/man1/syncterm.1%{?ext_man}

%changelog
