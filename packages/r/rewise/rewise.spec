#
# spec file for package rewise
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           rewise
Version:        0.3.1
Release:        0
Summary:        Extract files from Wise installers without executing them
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://codeberg.org/CYBERDEV/REWise
Source:         https://codeberg.org/CYBERDEV/REWise/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)

%description
The aim of this project is to extract assets from old game installers
made with Wise installer without executing the PE/NE file (.exe), so
they can be used with free software implementations of the game engine.

%prep
%autosetup -p1 -n %{name}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/rewise
%{_mandir}/man1/rewise.1%{?ext_man}

%changelog
