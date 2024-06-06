#
# spec file for package aws-c-io
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

%bcond_with test

%define library_version 1.0.0
%define library_soversion 0unstable
Name:           aws-c-io
Version:        0.14.9
Release:        0
Summary:        I/O and TLS package AWS SDK for C
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-io
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         aci_fix-cmake-modules-path.patch
Patch1:         aci_add-so-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  cmake(s2n)
BuildRequires:  ninja

%description
This is a module for the AWS SDK for C. It handles all I/O
and TLS work for application protocols.

%package -n lib%{name}%{library_soversion}
Summary:        Shared library files for aws-c-io library
Group:          Development/Libraries/C and C++

%description -n lib%{name}%{library_soversion}
This is a module for the AWS SDK for C. It handles all I/O
and TLS work for application protocols.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-io library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
This is a module for the AWS SDK for C. It handles all I/O
and TLS work for application protocols.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

# Testsuite requires internet connection, so it won't work
%check
%if %{with test}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
%ctest
%endif

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
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_includedir}/*

%changelog
