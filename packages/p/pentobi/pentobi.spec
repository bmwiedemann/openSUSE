#
# spec file for package pentobi
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           pentobi
Version:        28.0
Release:        0
Summary:        Program to play the board game Blokus
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://pentobi.sourceforge.net/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.18
# For hicolor dirs ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  rsvg-convert
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.5
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Xml)

%description
Pentobi is a computer opponent for the board game Blokus with
support for Classic, Duo, Junior, Trigon, and Nexos game variants.
Different levels of playing strength are available. Pentobi can
save and load games along with comments and move variations.

%prep
%setup -q

%build
%cmake_qt6 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%qt6_build

%install
%qt6_install

%files
%license LICENSE.md
%doc AUTHORS.md NEWS.md README.md
%{_bindir}/pentobi
%{_datadir}/applications/io.sourceforge.pentobi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/io.sourceforge.pentobi.appdata.xml

%changelog
