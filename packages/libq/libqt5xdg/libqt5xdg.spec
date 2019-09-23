#
# spec file for package libqt5xdg
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


%define _name libqtxdg
Name:           libqt5xdg
Version:        3.3.1
Release:        0
Summary:        Qt implementation of xdg specs for lxqt
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            https://lxqt.org
Source:         https://github.com/lxde/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        https://github.com/lxde/%{_name}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  lxqt-build-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.7.1
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt implementation of freedesktop.org XDG specs for LXQt

%package -n libQt5Xdg3
Summary:        Libraries for qtxdg
Group:          System/Libraries
Provides:       libqtxdg

%description -n libQt5Xdg3
QtXDG libraries for development

%package devel
Summary:        Devel files for libqtxdg
Group:          Development/Libraries/C and C++
Requires:       libQt5Xdg3 = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(Qt5UiTools)

%description devel
QtXDG libraries for development

%package -n libQt5XdgIconLoader3
Summary:        IconLoader library for QtXDG
Group:          System/Libraries
Provides:       libqtxdgiconloader

%description -n libQt5XdgIconLoader3
QtXDG icon loader libraries used in LXQt

%package -n libQt5XdgIconLoader-devel
Summary:        Devel files for libQt5XdgIconLoader
Group:          Development/Libraries/C and C++
Requires:       libQt5XdgIconLoader3 = %{version}

%description -n libQt5XdgIconLoader-devel
Development files for QtXDG icon loader libraries used in LXQt

%prep
%setup -q -n %{_name}-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}/%{_datadir}/locale

%post -n libQt5Xdg3 -p /sbin/ldconfig
%postun -n libQt5Xdg3 -p /sbin/ldconfig
%post -n libQt5XdgIconLoader3 -p /sbin/ldconfig
%postun -n libQt5XdgIconLoader3 -p /sbin/ldconfig

%files -n libQt5Xdg3
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/libQt5Xdg.so.*

%files devel
%defattr(-,root,root)
%{_datadir}/cmake/qt5xdg
%{_includedir}/qt5xdg
%{_libdir}/pkgconfig/Qt5Xdg.pc
%{_libdir}/libQt5Xdg.so

%files -n libQt5XdgIconLoader3
%defattr(-,root,root)
%{_libdir}/libQt5XdgIconLoader.so.3
%{_libdir}/libQt5XdgIconLoader.so.3.*

%files -n libQt5XdgIconLoader-devel
%defattr(-,root,root)
%dir %{_includedir}/qt5xdgiconloader
%dir %{_includedir}/qt5xdgiconloader/%{version}
%dir %{_includedir}/qt5xdgiconloader/%{version}/private
%dir %{_includedir}/qt5xdgiconloader/%{version}/private/xdgiconloader
%dir %{_datadir}/cmake/qt5xdgiconloader
%{_libdir}/libQt5XdgIconLoader.so
%{_libdir}/qt5/plugins/iconengines/libQt5XdgIconPlugin.so
%{_includedir}/qt5xdgiconloader/xdgiconloader_export.h
%{_includedir}/qt5xdgiconloader/%{version}/private/xdgiconloader/xdgiconloader_p.h
%{_libdir}/pkgconfig/Qt5XdgIconLoader.pc
%{_datadir}/cmake/qt5xdgiconloader/qt5xdgiconloader-config-version.cmake
%{_datadir}/cmake/qt5xdgiconloader/qt5xdgiconloader-config.cmake
%{_datadir}/cmake/qt5xdgiconloader/qt5xdgiconloader-targets-*.cmake
%{_datadir}/cmake/qt5xdgiconloader/qt5xdgiconloader-targets.cmake

%changelog
