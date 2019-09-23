#
# spec file for package libfm-qt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libfm-qt
Version:        0.14.1
Release:        0
Summary:        Library providing components to build desktop file managers
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://lxqt.org
Source:         https://github.com/lxde/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxde/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        libfm-qt.keyring
BuildRequires:  cmake >= 3.1.0
# Needs private headers, see xdndworkaround.cpp
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  lxqt-build-tools-devel >= 0.6.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.7.1
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.7.1
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 0.4.0
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(x11)
Provides:       libfm-qt

%description
libfm-qt is the Qt port of libfm, a library providing components to
build desktop file managers.

%{lang_package -r libfm-qt6}

%package -n libfm-qt6
Summary:        Library providing components to build desktop file managers
Group:          System/Libraries
Recommends:     %{name}-lang
Conflicts:      pcmanfm <= 0.10.0

%description -n libfm-qt6
libfm-qt is the Qt port of libfm, a library providing components to
build desktop file managers.

%package -n libfm-qt-devel
Summary:        Development files for libfm-qt
Group:          Development/Libraries/C and C++
Requires:       libfm-qt6 >= %{version}
Requires:       pkgconfig
# libfm-qt has an -I on a path from menu-cache-devel
Requires:       pkgconfig(libmenu-cache) >= 0.4.0

%description -n libfm-qt-devel
Libfm-Qt libraries for development

%prep
%setup -q

%build
%cmake -DPULL_TRANSLATIONS=No
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name} --with-qt

%post -n libfm-qt6 -p /sbin/ldconfig
%postun -n libfm-qt6 -p /sbin/ldconfig

%files -n libfm-qt6
%license LICENSE
%doc README.md
%dir %{_datadir}/libfm-qt/
%{_libdir}/libfm-qt.so.*
%{_datadir}/libfm-qt/archivers.list
%{_datadir}/libfm-qt/terminals.list
%{_datadir}/mime/packages/libfm-qt-mimetypes.xml

%files -n libfm-qt-devel
%doc %{_datadir}/cmake/fm-qt
%{_includedir}/libfm-qt/
%{_libdir}/libfm-qt.so
%{_libdir}/pkgconfig/libfm-qt.pc
%{_datadir}/cmake/fm-qt/fm-qt-config-version.cmake
%{_datadir}/cmake/fm-qt/fm-qt-config.cmake
%{_datadir}/cmake/fm-qt/fm-qt-targets-*.cmake
%{_datadir}/cmake/fm-qt/fm-qt-targets.cmake

%files lang -f %{name}.lang 
%dir %{_datadir}/libfm-qt
%dir %{_datadir}/libfm-qt/translations

%changelog
