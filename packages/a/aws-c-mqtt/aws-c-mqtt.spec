#
# spec file for package aws-c-mqtt
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


%global library_version 1_0_0
Name:           aws-c-mqtt
Version:        0.10.4
Release:        0
Summary:        AWS C99 implementation of the MQTT 3.1.1 specification
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-mqtt
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         acm_fix-cmake-modules-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-http)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libssl)

%description
AWS C99 implementation of the MQTT 3.1.1 specification.

%package -n lib%{name}%{library_version}
Summary:        Shared library files for aws-c-mqtt library
Group:          Development/Libraries/C and C++
Provides:       lib%{name}1 = %{version}
Obsoletes:      lib%{name}1 < %{version}

%description -n lib%{name}%{library_version}
AWS C99 implementation of the MQTT 3.1.1 specification.

This package contains the dynamically linked library.

%package bin
Summary:        Application binaries for aws-c-mqtt library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_version} = %{version}

%description bin
AWS C99 implementation of the MQTT 3.1.1 specification.

This package contains the application binaries.

%package devel
Summary:        Development files for aws-c-mqtt library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_version} = %{version}

%description devel
AWS C99 implementation of the MQTT 3.1.1 specification.

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

%post -n lib%{name}%{library_version} -p /sbin/ldconfig
%postun -n lib%{name}%{library_version} -p /sbin/ldconfig

%files -n lib%{name}%{library_version}
%doc README.md
%license LICENSE
%{_libdir}/*.so.1.0.0

%files bin
%{_bindir}/*

%files devel
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_includedir}/*

%changelog
