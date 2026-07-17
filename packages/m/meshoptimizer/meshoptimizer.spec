#
# spec file for package meshoptimizer
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

%define shlibname lib%{name}-1_2
Name:           meshoptimizer
Version:        1.2
Release:        0
Summary:        Mesh optimization library that makes meshes smaller and faster to render
License:        MIT
URL:            https://meshoptimizer.org/
Source0:        https://github.com/zeux/meshoptimizer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
When a GPU renders triangle meshes, various stages of the GPU pipeline have to
process vertex and index data. The efficiency of these stages depends on the
data you feed to them; this library provides algorithms to help optimize meshes
for these stages, as well as algorithms to reduce the mesh complexity and
storage overhead.

The library provides a C and C++ interface for all algorithms; you can use it
from C/C++ or from other languages via FFI (such as P/Invoke). If you want to
use this library from Rust, you should use meshopt crate. JavaScript interface
for some algorithms is available through meshoptimizer.js.

Two companion projects are developed and distributed alongside the library:
gltfpack, a command-line tool that automatically optimizes glTF files, and
clusterlod.h, a single-header C/C++ library for continuous level of detail
using clustered simplification.

%package devel
Summary:        Development files for meshoptimizer
Requires:       %{shlibname} = %{version}

%description devel
Mesh optimization library that makes meshes smaller and faster to render

This package holds the development files.

%package -n %{shlibname}
Summary:        Shared library for for meshoptimizer

%description -n %{shlibname}
Mesh optimization library that makes meshes smaller and faster to render

This package holds the shared library files.

%prep
%autosetup -p1

%build
%cmake \
 -DMESHOPT_BUILD_GLTFPACK:BOOL=ON \
 -DMESHOPT_BUILD_SHARED_LIBS:BOOL=ON \
 -DMESHOPT_SOVERSION=%{version}
# -DMESHOPT_STABLE_EXPORTS=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{shlibname}

%files
%license LICENSE.md
%doc README.md CONTRIBUTING.md
%{_bindir}/gltfpack

%files devel
%{_includedir}/meshoptimizer.h
%{_libdir}/cmake/meshoptimizer/
%{_libdir}/libmeshoptimizer.so

%files -n %{shlibname}
%{_libdir}/libmeshoptimizer.so.1.2

%changelog
