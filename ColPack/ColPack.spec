#
# spec file for package ColPack
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lname	libColPack0
Name:           ColPack
Version:        1.0.10
Release:        0
Summary:        Graph Coloring Library for C/C++
License:        LGPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://cscapes.cs.purdue.edu/coloringpage/
Source:         https://github.com/CSCsw/ColPack/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool

%description
This package provides algorithms for efficient solution of partitioning
problems occuring in the analysis of sparsity patterns in derivative
computations formulated as Graph Coloring problems.

For details see http://www.cscapes.org/coloringpage/software.htm

%package -n %{lname}
Summary:        Graph Coloring Library for C/C++
Group:          System/Libraries

%description -n %{lname}
This package provides algorithms for efficient solution of partitioning
problems occuring in the analysis of sparsity patterns in derivative
computations formulated as Graph Coloring problems.

For details see http://www.cscapes.org/coloringpage/software.htm

%package devel
Summary:        Graph Coloring Library for C/C++ -- development files
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package provides algorithms for efficient solution of partitioning
problems occuring in the analysis of sparsity patterns in derivative
computations formulated as Graph Coloring problems.

For details see http://www.cscapes.org/coloringpage/software.htm

This package provides the development environment for ColPack

%prep
%setup -q

%build
autoreconf -v --install --force
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete;
rm -rf %{buildroot}%{_builddir}/%{name}-%{version}/progs
rm -rf %{buildroot}%{_prefix}/examples/Basic

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libColPack.so.*

%files devel
%dir %{_includedir}/ColPack
%{_includedir}/ColPack/*.h
%{_libdir}/libColPack.so

%changelog
