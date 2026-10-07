#
# spec file for package speedcrunch
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


Name:           speedcrunch
Version:        1.0.0
Release:        0
Summary:        Calculator with history display, keyboard-oriented
License:        GPL-2.0-or-later
URL:            https://www.speedcrunch.org/
Source0:        https://github.com/heldercorreia/speedcrunch/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

%description
A keyboard-oriented desktop scientific calculator which shows results in a
scrollable display.

%prep
%autosetup -p1

%build
cd src
%cmake_qt6

%qt6_build
cd ..

%install
cd src
%qt6_install
cd ..

%files
%license LICENSE
%doc README.md
%{_bindir}/speedcrunch
%{_datadir}/applications/org.speedcrunch.SpeedCrunch.desktop
%{_datadir}/metainfo/org.speedcrunch.SpeedCrunch.metainfo.xml
%{_datadir}/pixmaps/org.speedcrunch.SpeedCrunch.png

%changelog
