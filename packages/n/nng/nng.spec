#
# spec file for package nng
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018-2024, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           nng
Version:        1.9.0
Release:        0
Summary:        Nanomsg NG - brokerless messaging
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://nanomsg.github.io/nng/
Source:         https://github.com/nanomsg/nng/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
nng (nanomsg next-generation) is a C socket library providing
several common communication patterns.

%package -n libnng%{sover}
Summary:        Shared library for nng
Group:          System/Libraries

%description -n libnng%{sover}
nng (nanomsg next-generation) is a C socket library providing
several common communication patterns.

%package devel
Summary:        Header files for nng
Group:          Development/Libraries/C and C++
Requires:       libnng%{sover} = %{version}

%description devel
Development and header files for nng (nanomsg next-generation).

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post   -n libnng%{sover} -p /sbin/ldconfig
%postun -n libnng%{sover} -p /sbin/ldconfig

%files -n libnng%{sover}
%doc README.adoc
%license LICENSE.txt
%{_libdir}/libnng.so.*

%files devel
%{_includedir}/nng
%{_libdir}/libnng.so
%{_bindir}/nngcat
#%%{_libdir}/pkgconfig/nng.pc
%dir %{_libdir}/cmake/nng
%{_libdir}/cmake/nng/nng-*.cmake

%changelog
