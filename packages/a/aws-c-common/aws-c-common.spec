#
# spec file for package aws-c-common
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
Name:           aws-c-common
Version:        0.12.2
Release:        0
Summary:        Core C99 package for AWS SDK for C
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-common
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ninja
# https://github.com/awslabs/aws-c-common/issues/1175
ExcludeArch:    s390x

%description
Core C99 package for AWS SDK for C. It includes cross-platform primitives,
configuration, data structures, and error handling.

%package -n lib%{name}%{library_soversion}
Summary:        Core C99 package for AWS SDK for C
Group:          System/Libraries

%description -n lib%{name}%{library_soversion}
Core C99 package for AWS SDK for C. It includes cross-platform primitives,
configuration, data structures, and error handling.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-common library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
Core C99 package for AWS SDK for C. It includes cross-platform primitives,
configuration, data structures, and error handling.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%make_jobs

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n lib%{name}%{library_soversion}

%files -n lib%{name}%{library_soversion}
%doc NOTICE README.md
%license LICENSE
%{_libdir}/*.so.%{library_soversion}
%{_libdir}/*.so.%{library_version}

%files devel
%license LICENSE
%{_libdir}/cmake/
%{_libdir}/*.so
%{_includedir}/*

%changelog
