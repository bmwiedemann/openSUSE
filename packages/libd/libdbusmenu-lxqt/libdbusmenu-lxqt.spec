#
# spec file for package libdbusmenu-lxqt
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


%define  _ver   0
Name:           libdbusmenu-lxqt
Version:        0.1.0
Release:        0
Summary:        A Qt implementation of the DBusMenu protocol
License:        LGPL-2.0-or-later
Group:          System/Libraries
URL:            https://github.com/lxqt/libdbusmenu-lxqt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
#uildRequires:  libqjson-devel
BuildRequires:  cmake(Qt6Core) >= 6.3.0
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  gcc-c++

%description
This library provides a Qt implementation of the DBusMenu protocol. The
DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n %{name}%{_ver}
Summary:        Development package for dbusmenu-lxqt-qt6
Group:          System/Libraries

%description -n %{name}%{_ver}
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus. Qt5 library

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{_ver} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake_qt6 \
    -DWITH_DOC=OFF
%qt6_build

%install
%qt6_install

%ldconfig_scriptlets -n %{name}%{_ver}

%files -n %{name}%{_ver}
%doc CHANGELOG NEWS README
%{_libdir}/%{name}.so.*
%license COPYING

%files devel
%{_includedir}/dbusmenu-lxqt
%{_libdir}/%{name}.so
%{_libdir}/cmake/dbusmenu-lxqt
%{_libdir}/pkgconfig/dbusmenu-lxqt.pc

%changelog
