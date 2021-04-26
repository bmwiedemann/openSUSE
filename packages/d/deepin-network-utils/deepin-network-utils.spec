#
# spec file for package deepin-network-utils
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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

%define _name dde-network-utils
%define sover 1

Name:           deepin-network-utils
Version:        5.3.0.8
Release:        0
License:        GPL-3.0+
Summary:        Deepin Network Utils
Url:            https://github.com/linuxdeepin/dde-network-utils
Group:          Productivity/Networking/System
Source:         https://github.com/linuxdeepin/dde-network-utils/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  gtest
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  cmake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Network Utils is an application repackage the DBus data which is provided
by network module of dde-daemon

%package -n lib%{_name}%{sover}
Summary:        Deepin Network Utils libraries 
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n lib%{_name}%{sover}
The  package contains the Libraries for deepin-network-utils.

%package devel
Summary:        Development tools for Deepin Network Utils
Group:          Development/Libraries/C and C++
Requires:       lib%{_name}%{sover} = %{version}-%{release}

%description devel
The deepin-network-utils-devel package contains the header files for
deepin-network-utils.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
sed -i "s/lrelease/lrelease-qt5/g" translate_generation.sh
sed -i 's|$$PREFIX/lib|$$LIBDIR|g' dde-network-utils/dde-network-utils.pro

%build
%qmake5 PREFIX=%{_prefix} LIBDIR=%{_libdir}
make %{?_smp_mflags}

%install
%qmake5_install

%post -n lib%{_name}%{sover} -p /sbin/ldconfig

%postun -n lib%{_name}%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md
%license LICENSE

%files -n lib%{_name}%{sover}
%defattr(-,root,root)
%{_libdir}/lib%{_name}.so.*

%files lang
%defattr(-,root,root)
%{_datadir}/%{_name}

%files devel
%defattr(-,root,root)
%{_includedir}/libddenetworkutils
%{_libdir}/lib%{_name}.so
%{_libdir}/pkgconfig/%{_name}.pc

%changelog

