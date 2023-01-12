#
# spec file for package orcania
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018-2023, Martin Hauke <mardnh@gmx.de>
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


%define sover 2_3
Name:           orcania
Version:        2.3.2
Release:        0
Summary:        MISC function Library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/babelouest/orcania
Source:         https://github.com/babelouest/orcania/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Different functions for different purposes but that can be shared
between other projects.

%package -n liborcania%{sover}
Summary:        MISC function library
Group:          System/Libraries

%description -n liborcania%{sover}
Different functions for different purposes but that can be shared
between other projects.

%package devel
Summary:        Header files for orcania
Group:          Development/Libraries/C and C++
Requires:       liborcania%{sover} = %{version}

%description devel
Development and header files for orcania.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post   -n liborcania%{sover} -p /sbin/ldconfig
%postun -n liborcania%{sover} -p /sbin/ldconfig

%files -n liborcania%{sover}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/liborcania.so.*

%files devel
%{_bindir}/base64url
%{_mandir}/man1/base64url.1.gz
%{_includedir}/orcania.h
%{_includedir}/orcania-cfg.h
%{_libdir}/liborcania.so
%{_libdir}/pkgconfig/liborcania.pc
%{_libdir}/cmake/Orcania

%changelog
