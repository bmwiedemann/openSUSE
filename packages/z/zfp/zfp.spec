#
# spec file for package zfp
#
# Copyright (c) 2020 SUSE LLC
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


%define major 0
%define minor 5
%define libname libzfp%{major}
Name:           zfp
Version:        %{major}.%{minor}.5
Release:        0
Summary:        Read and write numerical arrays
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
URL:            https://github.com/LLNL/zfp
Source0:        https://github.com/LLNL/zfp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
ExcludeArch:    i586

%description
Library for compressed numerical arrays that support high
throughput read and write random access.

%package -n %{libname}
Summary:        Read and write numerical arrays
Group:          System/Libraries

%description -n %{libname}
Library for compressed numerical arrays that support high
throughput read and write random access.

This subpackage contains the implementation as a shared library.

%package -n %{name}-devel
Summary:        Development files for zfp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{name}-devel
Development package for zfp.

%prep
%autosetup

%build
%cmake

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.%{major}

%files -n %{name}-devel
%doc README.md
%license LICENSE
%{_includedir}/*.h
%{_includedir}/zfp/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/zfp/

%changelog
