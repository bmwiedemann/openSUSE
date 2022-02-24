#
# spec file for package dmlc-core
#
# Copyright (c) 2022 SUSE LLC
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


%define libname libdmlc
Name:           dmlc-core
Version:        0.5
Release:        0
Summary:        Distributed Machine Learning Common Codebase
License:        Apache-2.0
URL:            https://github.com/dmlc/dmlc-core
Source:         https://github.com/dmlc/dmlc-core/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  azure-storage-cpp-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)

%description
DMLC-Core is the backbone library to support all DMLC projects, offers the bricks to build efficient and scalable distributed machine learning libraries.

%package devel
Summary:        Devel files for dmlc-core
Requires:       %{libname} = %{version}

%description devel
DMLC-Core is the backbone library to support all DMLC projects, offers the bricks to build efficient and scalable distributed machine learning libraries.

%package -n %{libname}
Summary:        Distributed Machine Learning Common Codebase

%description -n %{libname}
DMLC-Core is the backbone library to support all DMLC projects, offers the bricks to build efficient and scalable distributed machine learning libraries.

%prep
%setup -q
# Do not include MSVC helper header
sed -i -e '/stdafx.h/d' src/io/azure_filesys.cc

%build
# Azure - fails to compile
# HDFS - hadoop not packaged at the moment
%cmake \
  -DUSE_AZURE:BOOL=OFF \
  -DUSE_CXX14_IF_AVAILABLE:BOOL=ON \
  -DUSE_HDFS:BOOL=OFF \
  -DUSE_OPENMP:BOOL=ON \
  -DUSE_S3:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/*.so

%files devel
%dir %{_includedir}/dmlc
%{_includedir}/dmlc/*
%dir %{_libdir}/cmake/dmlc/
%{_libdir}/cmake/dmlc/*

%changelog
