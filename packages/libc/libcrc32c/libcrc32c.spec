#
# spec file for package libcrc32c
#
# Copyright (c) 2022 SUSE LLC
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


%define rname crc32c
%define soname 1
Name:           libcrc32c
Version:        1.1.2
Release:        0
Summary:        CRC32C implementation with support for CPU-specific acceleration instructions
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/crc32c
Source:         %{url}/archive/%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
This project collects a few CRC32C implementations under an umbrella
that dispatches to a suitable implementation based on the host computer's
hardware capabilities.

CRC32C is specified as the CRC that uses the iSCSI polynomial in RFC 3720.
The polynomial was introduced by G. Castagnoli, S. Braeuer and M. Herrmann.

%package -n %{name}%{soname}
Summary:        CRC32C implementation with support for CPU-specific acceleration instructions
Group:          System/Libraries

%description -n %{name}%{soname}
This project collects a few CRC32C implementations under an umbrella
that dispatches to a suitable implementation based on the host computer's
hardware capabilities.

CRC32C is specified as the CRC that uses the iSCSI polynomial in RFC 3720.
The polynomial was introduced by G. Castagnoli, S. Braeuer and M. Herrmann.

%package  -n %{name}-devel
Summary:        C++ header files and library symbolic links for %{rname}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -n %{rname}-%{version}

%build
%cmake -DCRC32C_BUILD_TESTS=0 -DCRC32C_BUILD_BENCHMARKS=0 -DCRC32C_USE_GLOG=0
%cmake_build

%install
%cmake_install

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%license LICENSE
%{_libdir}/%{name}.so.1.1.0
%{_libdir}/%{name}.so.1

%files -n %{name}-devel
%doc AUTHORS CONTRIBUTING.md README.md
%{_includedir}/%{rname}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Crc32c

%changelog
