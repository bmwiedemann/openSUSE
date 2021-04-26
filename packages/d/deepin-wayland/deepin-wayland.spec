#
# spec file for package deepin-wayland
#
# Copyright (c) 2020 SUSE LLC
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


%define _name dde-wayland
%define sover 0

Name:           deepin-wayland
Version:        1.0.0
Release:        0
Summary:        Deepin Wayland
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dde-wayland
Source0:        https://github.com/linuxdeepin/dde-wayland/archive/%{version}/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM add-wayland-includedir.patch hillwood@opensuse.org
# Make sure development files of wayland can be found and link wayland libraries
Patch0:         add-wayland-includedir.patch
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(xkbcommon)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DDE wayland client and server libraries with DDE custom protocol.

%package -n lib%{_name}-client%{sover}
Summary:        Deepin Wayland client
Group:          System/Libraries

%description -n lib%{_name}-client%{sover}
DDE wayland client library with DDE custom protocol.

%package -n lib%{_name}-server%{sover}
Summary:        Deepin Wayland Server
Group:          System/Libraries

%description -n lib%{_name}-server%{sover}
DDE wayland server library with DDE custom protocol.

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/X11
Requires:       lib%{_name}-server%{sover} = %{version}-%{release}
Requires:       lib%{_name}-client%{sover} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%qmake5 PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install

%post -n lib%{_name}-client%{sover} -p /sbin/ldconfig

%postun -n lib%{_name}-client%{sover} -p /sbin/ldconfig

%post -n lib%{_name}-server%{sover} -p /sbin/ldconfig

%postun -n lib%{_name}-server%{sover} -p /sbin/ldconfig

%files -n lib%{_name}-client%{sover}
%{_libdir}/lib%{_name}-client.so.*

%files -n lib%{_name}-server%{sover}
%{_libdir}/lib%{_name}-server.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{_name}-*
%{_libdir}/lib%{_name}-*.so
%{_libdir}/pkgconfig/%{_name}-*.pc

%changelog
