#
# spec file for package qt5ct
#
# Copyright (c) 2024 SUSE LLC
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


Name:           qt5ct
Version:        1.8
Release:        0
Summary:        Qt5 Configuration Tool
License:        BSD-2-Clause
URL:            https://sourceforge.net/projects/qt5ct
Source:         https://downloads.sf.net/qt5ct/%{name}-%{version}.tar.bz2
Source1:        qt5ct.sh
Source2:        qt5ct.csh
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libqt5-qtpaths
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  cmake(Qt5Widgets)
%requires_eq    libQt5Gui5
# libqt5-qtct was last used in openSUSE Leap 42.1.
Provides:       libqt5-qtct = %{version}
Obsoletes:      libqt5-qtct < %{version}

%description
This applications allows users to configure Qt5 settings (theme, font,
icons, etc.) under DE/WM without Qt integration.

%prep
%autosetup -p1

%build
%cmake

%cmake_build

%install
%cmake_install

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/qt5ct.sh
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/qt5ct.csh

# Unneeded
rm %{buildroot}%{_libdir}/libqt5ct-common.so

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README
%config %{_sysconfdir}/profile.d/qt5ct.*sh
%{_bindir}/qt5ct
%{_datadir}/applications/qt5ct.desktop
%{_datadir}/qt5ct/
%{_libdir}/libqt5ct-common.*
%dir %{_libdir}/qt5/plugins/platformthemes/
%{_libdir}/qt5/plugins/platformthemes/libqt5ct.so
%dir %{_libdir}/qt5/plugins/styles/
%{_libdir}/qt5/plugins/styles/libqt5ct-style.so

%changelog
