#
# spec file for package mimalloc
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%global sover   2
%global libname libmimalloc%{sover}
Name:           mimalloc
Version:        2.0.9
Release:        0
Summary:        A compact general purpose allocator
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/microsoft/mimalloc
Source:         https://github.com/microsoft/mimalloc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
This is a general purpose allocator. It is a drop-in replacement for
malloc and can be used in other programs without code changes.

Performance characteristics in comparison to allocators like tcmalloc 2.7,
jemalloc 5.2.1 and glibc 2.31 is favorable, with generally 6%% or better in
timing, depending on the particular workload.

%package -n %{libname}
Summary:        A compact general purpose allocator
Group:          System/Libraries
Obsoletes:      libmimalloc2_0

%description -n %{libname}
This is a general purpose allocator. It is a drop-in replacement for
malloc and can be used in other programs without code changes.

Performance characteristics in comparison to allocators like tcmalloc 2.7,
jemalloc 5.2.1 and glibc 2.31 is favorable, with generally 6%% or better in
timing, depending on the particular workload.

%package devel
Summary:        Development files for mimalloc
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This is a general purpose allocator.
It is a drop-in replacement for malloc and can be used in other
programs without code changes.

This subpackage contains libraries and header files for developing
applications that want to make use of mimalloc.

%prep
%setup

%build
%cmake -DMI_INSTALL_TOPLEVEL=ON -DMI_BUILD_OBJECT=OFF -DMI_BUILD_STATIC=OFF
%make_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc readme.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%changelog
