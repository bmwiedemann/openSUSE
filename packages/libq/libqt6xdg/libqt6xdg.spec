#
# spec file for package libqt6xdg
#
# Copyright (c) 2023 SUSE LLC
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


%define _name libqtxdg
%define _sover 4.0.0
%define sover 4
Name:           libqt6xdg
Version:        4.0.0
Release:        0
Summary:        Qt implementation of freedesktop.org xdg specs
License:        LGPL-2.1-only AND SUSE-LGPL-2.1-with-digia-exception-1.1
Group:          Development/Libraries/C and C++
URL:            https://github.com/lxqt/libqtxdg
Source0:        %{url}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6Core) >= 6.6.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.41.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  xterm-bin

%description
Qt implementation of freedesktop.org XDG specs for LXQt

%package -n libQt6Xdg%{sover}
Summary:        Libraries for qtxdg
Group:          System/Libraries
Provides:       libqtxdg

%description -n libQt6Xdg%{sover}
QtXDG libraries for development

%package devel
Summary:        Devel files for libqtxdg
Group:          Development/Libraries/C and C++
Requires:       libQt6Xdg%{sover} = %{version}

%description devel
QtXDG libraries for development

%package -n libQt6XdgIconLoader%{sover}
Summary:        IconLoader library for QtXDG
Group:          System/Libraries
Provides:       libqtxdgiconloader

%description -n libQt6XdgIconLoader%{sover}
QtXDG icon loader libraries used in LXQt

%package -n libQt6XdgIconLoader-devel
Summary:        Devel files for libQt6XdgIconLoader
Group:          Development/Libraries/C and C++
Requires:       libQt6XdgIconLoader%{sover} = %{version}

%description -n libQt6XdgIconLoader-devel
Development files for QtXDG icon loader libraries used in LXQt

%prep
%autosetup -n %{_name}-%{version}

%build
%cmake_qt6
%qt6_build

%install
%qt6_install
%fdupes -s %{buildroot}/%{_datadir}/locale

%ldconfig_scriptlets -n libQt6Xdg%{sover}
%ldconfig_scriptlets -n libQt6XdgIconLoader%{sover}

%files -n libQt6Xdg%{sover}
%doc AUTHORS CHANGELOG README.md
%config %{_sysconfdir}/xdg/*qtxdg.conf
%{_libdir}/libQt6Xdg.so.*
%license COPYING Digia-Qt-LGPL-Exception-1.1

%files devel
%{_datadir}/cmake/qt6xdg
%{_includedir}/qt6xdg
%{_libdir}/pkgconfig/Qt6Xdg.pc
%{_libdir}/libQt6Xdg.so

%files -n libQt6XdgIconLoader%{sover}
%{_libdir}/libQt6XdgIconLoader.so.%{sover}
%{_libdir}/libQt6XdgIconLoader.so.%{_sover}
%dir %{_libdir}/qt6/plugins
%dir %{_libdir}/qt6/plugins/iconengines
%{_libdir}/qt6/plugins/iconengines/libQt6XdgIconPlugin.so

%files -n libQt6XdgIconLoader-devel
%dir %{_includedir}/qt6xdgiconloader
%dir %{_includedir}/qt6xdgiconloader/%{_sover}
%dir %{_includedir}/qt6xdgiconloader/%{_sover}/private
%dir %{_includedir}/qt6xdgiconloader/%{_sover}/private/xdgiconloader
%dir %{_datadir}/cmake/qt6xdgiconloader
%{_libdir}/libQt6XdgIconLoader.so
%{_includedir}/qt6xdgiconloader/%{_sover}/private/xdgiconloader/xdgiconloader_p.h
%{_includedir}/qt6xdgiconloader/xdgiconloader_export.h
%{_libdir}/pkgconfig/Qt6XdgIconLoader.pc
%{_datadir}/cmake/qt6xdgiconloader/qt6xdgiconloader-config-version.cmake
%{_datadir}/cmake/qt6xdgiconloader/qt6xdgiconloader-config.cmake
%{_datadir}/cmake/qt6xdgiconloader/qt6xdgiconloader-targets-*.cmake
%{_datadir}/cmake/qt6xdgiconloader/qt6xdgiconloader-targets.cmake

%changelog
