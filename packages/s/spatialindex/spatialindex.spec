#
# spec file for package spatialindex
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


Name:           spatialindex
Version:        2.1.0
Release:        0
Summary:        A library for spatial indexing
License:        MIT
URL:            https://libspatialindex.org/
Source0:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2
Source1:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2.sha512sum
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig

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

%package -n lib%{name}8
Summary:        A library for spatial indexing

%description -n lib%{name}8
libspatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and disk
based storage managers and a robust implementation of an R*-tree, an MVR-tree
and a TPR-tree.

%package        devel
Summary:        Development files for %{name}
Requires:       lib%{name}8 = %{version}
Provides:       lib%{name}-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-src-%{version}

%build
# Relative LIB/INCLUDE_INSTALL_DIR: upstream .pc template prefixes them
# with ${prefix}, absolute paths yield double slashes (rpmlint E)
%cmake -DLIB_INSTALL_DIR:PATH=%{_lib} -DINCLUDE_INSTALL_DIR:PATH=include -DBUILD_TESTING=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%ldconfig_scriptlets -n lib%{name}8

%files -n lib%{name}8
%license COPYING
%{_libdir}/*.so.8*

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/libspatialindex/
%{_libdir}/pkgconfig/libspatialindex.pc

%changelog
