#
# spec file for package reproc
#
# Copyright (c) 2023 SUSE LLC
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


%define lib_name libreproc14
%define libpp_name libreproc++14
Name:           reproc
Version:        14.2.4
Release:        0
Summary:        A cross-platform (C99/C++11) process library
License:        MIT
URL:            https://github.com/DaanDeMeyer/reproc
Source:         https://github.com/DaanDeMeyer/reproc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies starting, stopping and communicating with external programs. The main use case is executing command line applications directly from C or C++ code and retrieving their output.

%package -n %{lib_name}
Summary:        Shared library for reproc

%description -n %{lib_name}
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies starting, stopping and communicating with external programs. The main use case is executing command line applications directly from C or C++ code and retrieving their output.

This package holds the shared library for reproc.

%package -n %{libpp_name}
Summary:        Shared library for reproc

%description -n %{libpp_name}
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies starting, stopping and communicating with external programs. The main use case is executing command line applications directly from C or C++ code and retrieving their output.

This package holds the shared library for reproc.

%package devel
Summary:        Development files for reproc
Requires:       %{lib_name} = %{version}
Requires:       %{libpp_name} = %{version}

%description devel
reproc (Redirected Process) is a cross-platform C/C++ library that simplifies starting, stopping and communicating with external programs. The main use case is executing command line applications directly from C or C++ code and retrieving their output.

This package holds the development files for reproc.

%prep
%autosetup -p1

%build
%cmake -DREPROC++:BOOL=ON -DREPROC_TEST=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig
%post   -n %{libpp_name} -p /sbin/ldconfig
%postun -n %{libpp_name} -p /sbin/ldconfig

%files -n %{lib_name}
%license LICENSE
%doc *.md
%{_libdir}/libreproc.so.*

%files -n %{libpp_name}
%license LICENSE
%doc *.md
%{_libdir}/libreproc++.so.*

%files devel
%{_libdir}/libreproc*.so
%{_includedir}/reproc*/
%{_libdir}/cmake/reproc*/
%{_libdir}/pkgconfig/reproc*.pc

%changelog
