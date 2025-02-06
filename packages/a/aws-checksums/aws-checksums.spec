#
# spec file for package aws-checksums
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
%define library_soversion 1
Name:           aws-checksums
Version:        0.2.3
Release:        0
Summary:        Checksums package for AWS SDK for C
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-checksums
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         ac_re-add-so-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  cmake(aws-c-common)

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

%package -n %{name}-bin
Summary:        Binary files for aws-checksums library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description -n %{name}-bin
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

This package contains the binary files.

%package -n lib%{name}%{library_soversion}
Summary:        Shared library files for aws-checksums library
Group:          Development/Libraries/C and C++

%description -n lib%{name}%{library_soversion}
Cross-Platform hardware-accelerated CRC32c and CRC32 with fallback to
efficient software implementations. C interface with language bindings
for each of the AWS SDKs.

This package contains the dynamically linked library.

%package -n lib%{name}-devel
Summary:        Development files for aws-checksums library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description -n lib%{name}-devel
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

%check
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/build
%ctest

%install
%cmake_install

%post -n lib%{name}%{library_soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{library_soversion} -p /sbin/ldconfig

%files -n %{name}-bin
%{_bindir}/checksum-profile

%files -n lib%{name}%{library_soversion}
%doc README.md
%license LICENSE
%{_libdir}/*.so.%{library_soversion}
%{_libdir}/*.so.%{library_version}

%files -n lib%{name}-devel
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_includedir}/*

%changelog
