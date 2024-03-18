#
# spec file for package aws-c-event-stream
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
%define library_soversion 1
Name:           aws-c-event-stream
Version:        0.4.2
Release:        0
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/awslabs/aws-c-event-stream
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz
Patch0:         aces_fix-cmake-modules-path.patch
Patch1:         aces_re-add-so-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  ninja

%description
C99 implementation of the vnd.amazon.eventstream content-type.

%package -n lib%{name}%{library_soversion}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
Group:          System/Libraries

%description -n lib%{name}%{library_soversion}
C99 implementation of the vnd.amazon.eventstream content-type.

This package contains the dynamically linked library.

%package devel
Summary:        Development files for aws-c-event-stream library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
C99 implementation of the vnd.amazon.eventstream content-type.

This package contains the development files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%fdupes -s %{buildroot}%{_libdir}/cmake

%post -n lib%{name}%{library_soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{library_soversion} -p /sbin/ldconfig

%files -n lib%{name}%{library_soversion}
%doc NOTICE README.md
%license LICENSE
%{_libdir}/*.so.%{library_soversion}
%{_libdir}/*.so.%{library_version}

%files devel
%{_libdir}/cmake/
%{_libdir}/*.so
%{_includedir}/aws/

%changelog
