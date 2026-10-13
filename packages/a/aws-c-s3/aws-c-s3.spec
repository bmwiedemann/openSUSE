#
# spec file for package aws-c-s3
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


%define library_version 1.3.1
%define library_soversion 1.3
Name:           aws-c-s3
Version:        1.3.1
Release:        0
Summary:        AWS Cross-Platform, C99 wrapper for cryptography primitives
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-s3
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(aws-c-auth)
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-http)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-c-sdkutils)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(numa)

%description
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.

%package -n %{name}-bin
Summary:        Binary files for aws-c-s3 library
Group:          Development/Libraries/C and C++
# both provide /usr/bin/s3
Conflicts:      libs3-tools

%description -n %{name}-bin
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.

This package contains the command line utilities.

%package -n lib%{name}1_3
Summary:        Shared library files for aws-c-s3 library
Group:          Development/Libraries/C and C++
Obsoletes:      lib%{name}-0unstable < %{version}

%description -n lib%{name}1_3
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-s3 library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}1_3 = %{version}

%description devel
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography primitives.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/aws-c-common/modules
%make_jobs

# Testsuite currently fails
#%%check
#export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
#%%ctest

%install
%cmake_install

%post -n lib%{name}1_3 -p /sbin/ldconfig
%postun -n lib%{name}1_3 -p /sbin/ldconfig

%files -n %{name}-bin
%{_bindir}/s3

%files -n lib%{name}1_3
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{library_soversion}
%{_libdir}/lib%{name}.so.%{library_version}

%files devel
%{_libdir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%dir %{_includedir}/aws/s3
%{_includedir}/aws/s3/*

%changelog
