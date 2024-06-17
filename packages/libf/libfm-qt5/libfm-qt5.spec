#
# spec file for package libfm-qt5
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
%define _name libfm-qt

Name:           libfm-qt5
Version:        1.4.0
Release:        0
Summary:        Library providing components to build desktop file managers
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            http://lxqt.org
Source:         https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
Source2:        libfm-qt.keyring
BuildRequires:  cmake >= 3.5.0
BuildRequires:  lxqt-build-tools-qt5-devel >= 0.13.0
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(lxqt) >= 2.0.0
BuildRequires:  cmake(lxqt-menu-data) >= 2.0.0
BuildRequires:  cmake(qt5xdg)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 1.1.0
BuildRequires:  pkgconfig(x11)

%description
libfm-qt5 is the Qt5 port of libfm, and provides compatibility for Qt5 Applications in LXQt >= 2.0

%lang_package

%package -n libfm-qt5-14
Summary:        Library providing components to build desktop file managers
# Require data files read by the library. For parallel installed library versions, the newest one wins
Conflicts:      pcmanfm <= 0.10.0
Provides:       libfm-qt5 = %{version}

%description -n libfm-qt5-14
libfm-qt is the Qt port of libfm, a library providing components to
build desktop file managers.

%package -n libfm-qt5-devel
Summary:        Development files for libfm-qt
Requires:       libfm-qt5-14 >= %{version}
Requires:       pkgconfig
# libfm-qt has an -I on a path from menu-cache-devel
Requires:       pkgconfig(libmenu-cache) >= 0.4.0

%description -n libfm-qt5-devel
Libfm-Qt libraries for development

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{_name} --with-qt

%ldconfig_scriptlets -n libfm-qt5-14

%check
%ctest

%files -n libfm-qt5-14
%license LICENSE LICENSE.BSD-3-Clause
%doc README.md
%dir %{_datadir}/%{_name}
%{_libdir}/%{_name}.so.*
%{_datadir}/%{_name}/*.list
%{_datadir}/mime/packages/%{_name}-mimetypes.xml

%files -n libfm-qt5-devel
%{_includedir}/%{_name}/
%{_libdir}/%{_name}.so
%{_libdir}/pkgconfig/%{_name}.pc
%{_datadir}/cmake/fm-qt/

%files lang -f %{_name}.lang
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/translations

%changelog
