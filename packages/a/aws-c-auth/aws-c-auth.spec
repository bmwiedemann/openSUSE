#
# spec file for package aws-c-auth
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
%define library_pkg 1_0_0
%define library_soversion 1
Name:           aws-c-auth
Version:        0.7.22
Release:        0
Summary:        AWS C99 library implementation of AWS client-side authentication
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-auth
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         aca_fix-cmake-modules-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-http)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-c-sdkutils)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
C99 library implementation of AWS client-side authentication: standard
credentials providers and signing.

From a cryptographic perspective, only functions with the suffix "_constant_time"
should be considered constant time.

%package -n lib%{name}%{library_pkg}
Summary:        Shared library files for aws-c-auth library
Group:          Development/Libraries/C and C++
Provides:       lib%{name}%{library_soversion} = %{version}
Obsoletes:      lib%{name}%{library_soversion} <= %{version}

%description -n lib%{name}%{library_pkg}
AWS C99 library implementation of AWS client-side authentication:
standard credentials providers and signing.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-auth library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_pkg} = %{version}

%description devel
AWS C99 library implementation of AWS client-side authentication:
standard credentials providers and signing.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

# Testsuite currently hangs
# see: https://github.com/awslabs/aws-c-auth/issues/147
#%%check
#export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
#%%ctest

%install
%cmake_install
ln -s lib%{name}.so.%{library_version} %{buildroot}%{_libdir}/lib%{name}.so.%{library_soversion}

%post -n lib%{name}%{library_pkg} -p /sbin/ldconfig
%postun -n lib%{name}%{library_pkg} -p /sbin/ldconfig

%files -n lib%{name}%{library_pkg}
%doc README.md
%license LICENSE
%{_libdir}/*.so.%{library_soversion}
%{_libdir}/*.so.%{library_version}

%files devel
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_includedir}/*

%changelog
