#
# spec file for package aws-c-cal
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define library_pkg 1_0
%define library_soversion 1.0
Name:           aws-c-cal
Version:        1.0.0
Release:        0
Summary:        AWS C99 wrapper for cryptography primitives
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-cal
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libcrypto)

%description
AWS Crypto Abstraction Layer is a C99 wrapper for cryptography primitives.

%package -n lib%{name}%{library_pkg}
Summary:        AWS C99 wrapper for cryptography primitives
Group:          System/Libraries
Provides:       lib%{name}0unstable = %{version}
Obsoletes:      lib%{name}0unstable < %{version}

%description -n lib%{name}%{library_pkg}
AWS Crypto Abstraction Layer is a C99 wrapper for cryptography primitives.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-cal library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_pkg} = %{version}

%description devel
AWS Crypto Abstraction Layer, a C99 wrapper for cryptography primitives.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/aws-c-common/modules
%make_jobs

%check
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
%ctest

%install
%cmake_install

%post -n lib%{name}%{library_pkg} -p /sbin/ldconfig
%postun -n lib%{name}%{library_pkg} -p /sbin/ldconfig

%files -n lib%{name}%{library_pkg}
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{library_soversion}
%{_libdir}/lib%{name}.so.%{library_version}
%{_libdir}/lib%{name}.so.1.0

%files devel
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%dir %{_includedir}/aws/cal
%{_includedir}/aws/cal/*

%changelog
