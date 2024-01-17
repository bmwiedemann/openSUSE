#
# spec file for package dtkgui
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Hillwood Yang <hillwood@opensuse.org>
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


%define libver  5
%define apiver  5.5.0
# %define pkg_ver 5.5

Name:           dtkgui
Version:        5.5.25
Release:        0
Summary:        Deepin Toolkit GUI
License:        LGPL-3.0
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin/dtkgui
Source0:        https://github.com/linuxdeepin/dtkgui/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX_UPSTREAM fix-library-link.patch hillwood@opensuse.org - Should link glib-2.0
Patch0:         fix-library-link.patch
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  dtkcommon
BuildRequires:  pkgconfig(dtkcore) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Widgets)
# BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A GUI module for DDE look and feel for the Deepin Toolkit.

%package -n lib%{name}%{libver}
Summary:        Deepin Toolkit GUI libraries
Group:          System/Libraries

%description -n lib%{name}%{libver}
Deepint Tool Kit (Dtk) GUI is the base devlopment tool of all C++/Qt developer
work on Deepin.

%package devel
Summary:        Development tools for dtkgui
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
The dtkgui-devel package contains the header files and developer docs for
dtkgui.

You should first read the "Deepin Application Specification".

%prep
%autosetup -p1

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}

%install
%qmake5_install

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%dir %{_libdir}/libdtk-%{apiver}
%dir %{_libdir}/libdtk-%{apiver}/DGui
%dir %{_libdir}/libdtk-%{apiver}/DGui/bin
%{_libdir}/libdtk-%{apiver}/DGui/bin/deepin-gui-settings
%{_libdir}/libdtk-%{apiver}/DGui/bin/dde-kwin-debug
%{_libdir}/libdtk-%{apiver}/DGui/bin/dnd-test-*

%files -n lib%{name}%{libver}
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/libdtk-%{apiver}/DGui
%{_libdir}/cmake/DtkGui
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
# %{_libdir}/pkgconfig/%{name}%{pkg_ver}.pc
# %dir %{_libdir}/cmake/DtkGui%{pkg_ver}
# %{_libdir}/cmake/DtkGui%{pkg_ver}/DtkGui%{pkg_ver}Config.cmake
%{_libdir}/qt5/mkspecs/modules/qt_lib_%{name}.pri
#%{_libdir}/qt5/mkspecs/modules/qt_lib_%{name}%{pkg_ver}.pri

%changelog

