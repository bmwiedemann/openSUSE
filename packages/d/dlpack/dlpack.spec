#
# spec file for package dlpack
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


Name:           dlpack
Version:        0.8
Release:        0
Summary:        DLPack: Open In Memory Tensor Structure
License:        Apache-2.0
URL:            https://github.com/dmlc/dlpack
Source0:        https://github.com/dmlc/dlpack/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
DLPack is an open in-memory tensor structure to for sharing tensor among frameworks. DLPack enables:
 * Easier sharing of operators between deep learning frameworks.
 * Easier wrapping of vendor level operator implementations, allowing collaboration when introducing new devices/ops.
 * Quick swapping of backend implementations, like different version of BLAS
 * For final users, this could bring more operators, and possibility of mixing usage between frameworks.

%package devel
Summary:        DLPack: Open In Memory Tensor Structure

%description devel
DLPack is an open in-memory tensor structure to for sharing tensor among frameworks. DLPack enables:
 * Easier sharing of operators between deep learning frameworks.
 * Easier wrapping of vendor level operator implementations, allowing collaboration when introducing new devices/ops.
 * Quick swapping of backend implementations, like different version of BLAS
 * For final users, this could bring more operators, and possibility of mixing usage between frameworks.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%defattr(-,root,root)
%dir %{_includedir}/dlpack
%{_includedir}/dlpack/*
%dir %{_libdir}/cmake/dlpack/
%{_libdir}/cmake/dlpack/*.cmake

%changelog
