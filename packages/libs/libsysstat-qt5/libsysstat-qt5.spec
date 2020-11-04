#
# spec file for package libsysstat-qt5
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


%define         _name libsysstat
Name:           libsysstat-qt5
Version:        0.4.4
Release:        0
Summary:        Library used to query system info and statistics
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/libsysstat/releases/download/%{version}/libsysstat-%{version}.tar.xz
Source1:        https://github.com/lxqt/libsysstat/releases/download/%{version}/libsysstat-%{version}.tar.xz.asc
Source2:        libsysstat-qt5.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.12.0

%description
Library used to query system info and statistics.

%package -n libsysstat-qt5-0
Summary:        Library used to query system info and statistics
Group:          System/Libraries
Provides:       libsysstat

%description -n libsysstat-qt5-0
Development libraries for libsysstat.

%package devel
Summary:        Devel files for libsysstat
Group:          Development/Libraries/C and C++
Requires:       libsysstat-qt5-0 = %{version}
Requires:       pkgconfig

%description devel
sysstat libraries for development.

%prep
%setup -q -n %{_name}-%{version}

%build
%cmake -DUSE_QT5=ON
%make_build

%install
%cmake_install

%post -n libsysstat-qt5-0 -p /sbin/ldconfig
%postun -n libsysstat-qt5-0 -p /sbin/ldconfig

%files -n libsysstat-qt5-0
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%{_includedir}/sysstat-qt5
%{_datadir}/cmake/sysstat-qt5
%{_libdir}/pkgconfig/sysstat-qt5.pc
%{_libdir}/%{name}.so

%changelog
