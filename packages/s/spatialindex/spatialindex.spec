#
# spec file for package spatialindex
#
# Copyright (c) 2021 SUSE LLC
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


Name:           spatialindex
Version:        1.9.3
Release:        0
Summary:        A library for spatial indexing
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://libspatialindex.org/
Source0:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2
Source1:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2.sha512sum
# PATCH-FIX-OPENSUSE restore-pkg-config-functionality.patch -- pkg-config: restore functionality (via CMake), change Cflags
Patch0:         restore-pkg-config-functionality.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkg-config

%description
An extensible framework that will support robust spatial indexing methods.

Support for sophisticated spatial queries. Range, point location, nearest
neighbor and k-nearest neighbor as well as parametric queries (defined by
spatial constraints) should be easy to deploy and run.

Easy to use interfaces for inserting, deleting and updating information.

Wide variety of customization capabilities. Basic index and storage
characteristics like the page size, node capacity, minimum fan-out, splitting
algorithm, etc. should be easy to customize.

Index persistence. Internal memory and external memory structures should be
supported. Clustered and non-clustered indices should be easy to be persisted.

%package -n lib%{name}6
Summary:        A library for spatial indexing
Group:          Productivity/Graphics/Other
# Version 1.9.3 of spatialindex was wrongly shipping the .so.6 in libspatialindex4
# Help tp replace this package version
Obsoletes:      libspatialindex4 = 1.9.3

%description -n lib%{name}6
libspatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and disk
based storage managers and a robust implementation of an R*-tree, an MVR-tree
and a TPR-tree.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       lib%{name}6 = %{version}
Provides:       lib%{name}-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n lib%{name}6 -p /sbin/ldconfig

%postun -n lib%{name}6 -p /sbin/ldconfig

%files -n lib%{name}6
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.6*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspatialindex.pc

%changelog
