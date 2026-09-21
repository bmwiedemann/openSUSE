#
# spec file for package qterm
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


Name:           qterm
Version:        0.8.2
Release:        0
Summary:        BBS client based on Qt
License:        GPL-2.0-or-later
URL:            https://github.com/qterm/qterm
Source0:        https://github.com/qterm/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        qterm.desktop
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-tools-helpgenerators
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)

%description
QTerm is a full featured BBS client written in Qt.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes -s %{buildroot}

%files
%license COPYRIGHT
%doc README.rst RELEASE_NOTES
%{_bindir}/qterm
%{_datadir}/qterm/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/qterm.png

%changelog
