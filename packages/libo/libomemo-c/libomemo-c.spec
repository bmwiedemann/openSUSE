#
# spec file for package libomemo-c
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


%define c_lib libomemo-c0
Name:           libomemo-c
Version:        0.5.0
Release:        0
Summary:        Fork of libsignal-protocol-c adding support for OMEMO XEP-0384 0.5.0+
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/dino/libomemo-c
Source:         https://github.com/dino/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  check-devel >= 0.9.10
BuildRequires:  cmake >= 2.8.4
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl) >= 1.0

%description
This is a fork of libsignal-protocol-c, an implementation of Signal's ratcheting forward secrecy protocol that works in synchronous and asynchronous messaging. The fork adds support for OMEMO as defined in XEP-0384 versions 0.3.0 and later.

%package -n libomemo-c-devel
Summary:        Development files for libomemo-c
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description -n libomemo-c-devel
Development files and headers for libomemo-c

%package -n %{c_lib}
Summary:        Omemo C Library
Group:          System/Libraries

%description -n %{c_lib}
The libomemo-c library is a forward secrecy protocol library written in C.

%prep
%setup -q

%build
%cmake \
    -DBUILD_TESTING=ON
%if 0%{?suse_version} > 1500
%cmake_build
%else
%make_jobs
%endif

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files -n %{c_lib}
%license LICENSE
%doc README.md
%{_libdir}/libomemo-c.so.0
%{_libdir}/libomemo-c.so.0.5.0

%files devel
%dir %{_includedir}/omemo
%{_includedir}/omemo/*.h
%{_libdir}/libomemo-c.so
%{_libdir}/pkgconfig/libomemo-c.pc

%changelog
