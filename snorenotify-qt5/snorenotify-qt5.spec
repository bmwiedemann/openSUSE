#
# spec file for package snorenotify-qt5
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           snorenotify-qt5
%define rname  snorenotify
Version:        0.7.0
Release:        0
Summary:        Snorenotify is a multi platform Qt based notification framework
License:        LGPL-3.0
Group:          System/Libraries
Url:            https://github.com/KDE/snorenotify
Source:         %{rname}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM fix_desktop_files.patch
Patch0:         fix_desktop_files.patch
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(Qt5WebSockets)
%endif
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Snorenotify is a multi platform Qt based notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Unix and Mac.

%package devel
Summary:        Snorenotify is a multi platform Qt based notification framework
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Snorenotify is a multi platform Qt based notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Unix and Mac.

%prep
%setup -q -n %{rname}-%{version}
%patch0 -p1

%build
%cmake_kf5 -d build -- -DWITH_QT4=OFF -DWITH_FREEDESKTOP_FRONTEND=ON
%make_jobs

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md COPYING*
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
%defattr(-,root,root)
%doc COPYING*
%{_includedir}/libsnore/
%{_libdir}/cmake/libsnoreQt5/
%{_libdir}/cmake/libsnoresettingsQt5/
%{_libdir}/libsnore-qt5.so
%{_libdir}/libsnoresettings-qt5.so
%{_libdir}/qt5/mkspecs/modules/qt_LibsnoreQt5.pri
%{_libdir}/qt5/mkspecs/modules/qt_LibsnoreSettingsQt5.pri

%changelog
