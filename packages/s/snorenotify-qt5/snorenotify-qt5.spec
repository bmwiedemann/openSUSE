#
# spec file for package snorenotify-qt5
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


%define rname  snorenotify
Name:           snorenotify-qt5
Version:        0.7.0
Release:        0
Summary:        Snorenotify is a multi platform Qt based notification framework
License:        LGPL-3.0-only
URL:            https://github.com/KDE/snorenotify
Source:         %{rname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_desktop_files.patch
Patch0:         fix_desktop_files.patch
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Snorenotify is a multi platform Qt based notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Unix and Mac.

%package devel
Summary:        Snorenotify is a multi platform Qt based notification framework
Requires:       %{name} = %{version}

%description devel
Snorenotify is a multi platform Qt based notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Unix and Mac.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DWITH_QT4=OFF -DWITH_FREEDESKTOP_FRONTEND=ON
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license COPYING*
%doc README.md
%{_bindir}/snorenotify
%{_bindir}/snoresend
%{_bindir}/snoresettings
%{_bindir}/snoresettings-cli
%{_datadir}/applications/snorenotify.desktop
%{_datadir}/applications/snoresettings.desktop
%{_datadir}/icons/hicolor/128x128/apps/snore.png
%{_libdir}/libsnore-qt5.so.*
%{_libdir}/libsnoresettings-qt5.so.*
%{_libdir}/qt5/plugins/libsnore-qt5
%{_libdir}/qt5/plugins/libsnore-qt5/libsnore*

%files devel
%license COPYING*
%{_includedir}/libsnore/
%{_libdir}/cmake/libsnoreQt5/
%{_libdir}/cmake/libsnoresettingsQt5/
%{_libdir}/libsnore-qt5.so
%{_libdir}/libsnoresettings-qt5.so
%{_libdir}/qt5/mkspecs/modules/qt_LibsnoreQt5.pri
%{_libdir}/qt5/mkspecs/modules/qt_LibsnoreSettingsQt5.pri

%changelog
