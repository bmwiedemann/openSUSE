#
# spec file for package deepin-qt-dbus-factory
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libver 2
%define _name  dde-qt-dbus-factory

Name:           deepin-qt-dbus-factory
Version:        1.1.6
Release:        0
Summary:        A repository storing auto-generated Qt5 D-Bus code
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source:         https://github.com/linuxdeepin/dde-qt-dbus-factory/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  dtkcore
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

%description
dde-qt-dbus-factory is a repository storing auto-generated Qt5 D-Bus
code.

%package -n libdframeworkdbus%{libver}
Summary:        A repository storing auto-generated Qt5 D-Bus code
Group:          System/Libraries

%description -n libdframeworkdbus%{libver}
dde-qt-dbus-factory is a repository storing auto-generated Qt5 D-Bus
code. This can help DDE developers not having to copy code from other
projects or re-generate code for the same D-Bus interface for new
projects.

%package -n libdframeworkdbus-devel
Summary:        Development tools for libdframeworkdbus - deepin-qt-dbus-factory
Group:          Development/Libraries/C and C++
Requires:       libdframeworkdbus%{libver} = %{version}

%description -n libdframeworkdbus-devel
de-qt-dbus-factory is a repository storing auto-generated Qt5 D-Bus
code.

The libdbusextended-devel package contains the header files and developer
docs for libdbusextended(deepin-qt-dbus-factory).

%prep
%setup -q -n %{_name}-%{version}

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
make %{?_smp_mflags}

%install
%qmake5_install

%post -n libdframeworkdbus%{libver} -p /sbin/ldconfig
%postun -n libdframeworkdbus%{libver} -p /sbin/ldconfig

%files -n libdframeworkdbus%{libver}
%{_libdir}/libdframeworkdbus.so.*

%files -n libdframeworkdbus-devel
%license LICENSE
%doc README.md CHANGELOG.md
%{_includedir}/libdframeworkdbus-*
%{_libdir}/libdframeworkdbus.so
%dir %{_libdir}/cmake/DFrameworkdbus
%{_libdir}/cmake/DFrameworkdbus/DFrameworkdbusConfig.cmake
%{_libdir}/pkgconfig/dframeworkdbus.pc

%changelog
