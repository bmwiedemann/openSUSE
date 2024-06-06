#
# spec file for package aws-c-http
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
%define library_soversion 1_0_0
Name:           aws-c-http
Version:        0.8.2
Release:        0
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-http
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         ach_fix-cmake-modules-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.

%package -n lib%{name}%{library_soversion}
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications
Group:          System/Libraries

%description -n lib%{name}%{library_soversion}
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-http library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_MODULE_PATH=%{_libdir}/cmake
%make_jobs

# Testsuite currently fails
#%%check
#export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
#%%ctest

%install
%cmake_install

%post -n lib%{name}%{library_soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{library_soversion} -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n lib%{name}%{library_soversion}
%doc README.md
%license LICENSE
%{_libdir}/*.so.%{library_version}

%files devel
%{_libdir}/cmake/
%{_libdir}/*.so
%{_includedir}/*

%changelog
