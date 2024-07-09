#
# spec file for package s2n
#
# Copyright (c) 2024 SUSE LLC
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


%define library_version 1.0.0
%define library_soversion 0unstable
Name:           s2n
Version:        1.4.17
Release:        0
Summary:        AWS implementation of the TLS/SSL protocols
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/s2n
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch1:         s2n_add-so-version.patch
Patch2:         s2n_fix-cmake-modules-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(libssl)
BuildRequires:  ninja

%description
s2n is a C99 implementation of the TLS/SSL protocols.

%package -n lib%{name}%{library_soversion}
Summary:        AWS implementation of the TLS/SSL protocol
Group:          System/Libraries

%description -n lib%{name}%{library_soversion}
s2n is a C99 implementation of the TLS/SSL protocols.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for s2n library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
s2n is a C99 implementation of the TLS/SSL protocols.

This package contains the development files.

%prep
%autosetup -p1 -n %{name}-tls-%{version}

%build
%if 0%{?suse_version} < 1500
export S2N_LIBCRYPTO=openssl-1.0.2
%endif
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

%check
exit 0
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build/lib
%ctest

%install
%cmake_install

%post -n lib%{name}%{library_soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{library_soversion} -p /sbin/ldconfig

%files -n lib%{name}%{library_soversion}
%doc README.md
%license LICENSE
%{_libdir}/*.so.%{library_soversion}
%{_libdir}/*.so.%{library_version}

%files devel
%{_libdir}/cmake/
%{_libdir}/*.so
%{_includedir}/*

%changelog
