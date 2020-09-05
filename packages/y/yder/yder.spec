#
# spec file for package yder
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018-2020, Martin Hauke <mardnh@gmx.de>
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


%define sover 1_4
Name:           yder
Version:        1.4.12
Release:        0
Summary:        Logging library written in C
# Example programs in subfolder examples/ are licensed under MIT
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/babelouest/yder
Source:         https://github.com/babelouest/yder/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liborcania) >= 2.0.0
BuildRequires:  pkgconfig(libsystemd)

%description
Yder is a logging library where messages can be logged to console,
files, syslog or journald.

Yder is single-threaded, which means that only one instance of yder
logging can be used at the same time in a program.

%package -n libyder%{sover}
Summary:        Logging library written in C
Group:          System/Libraries

%description -n libyder%{sover}
Yder is a logging library where messages can be logged to console,
files, syslog or journald.

Yder is single-threaded, which means that only one instance of yder
logging can be used at the same time in a program.

%package devel
Summary:        Header files for yder
Group:          Development/Libraries/C and C++
Requires:       libyder%{sover} = %{version}

%description devel
Development and header files for yder.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/
make %{?_smp_mflags}

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc/

%post   -n libyder%{sover} -p /sbin/ldconfig
%postun -n libyder%{sover} -p /sbin/ldconfig

%files -n libyder%{sover}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/libyder.so.*

%files devel
%{_includedir}/yder.h
%{_includedir}/yder-cfg.h
%{_libdir}/libyder.so
%{_libdir}/pkgconfig/libyder.pc

%changelog
