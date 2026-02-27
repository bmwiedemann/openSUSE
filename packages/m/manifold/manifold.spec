#
# spec file for package manifold
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


%bcond_with manifold_testing
%if 0%{?suse_version} >= 1600
%bcond_without python_bindings
%else
%bcond_with python_bindings
%endif

%if 0%{?suse_version} == 1500
%global force_gcc_version   14
%endif

%global sh_lib   libmanifold3
%global sh_c_lib libmanifoldc3

Name:           manifold
Version:        3.4.0
Release:        0
Summary:        Geometry library for topological robustness
License:        Apache-2.0
URL:            https://github.com/elalish/manifold
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  gtest
BuildRequires:  openvdb-devel >= 11
BuildRequires:  cmake(Clipper2)
BuildRequires:  cmake(TBB)
BuildRequires:  cmake(assimp)
%if %{with python_bindings}
BuildRequires:  python3-nanobind-devel
%endif

%description
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package -n %{sh_lib}
Summary:        Shared library for manifold

%description -n %{sh_lib}
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package -n %{sh_c_lib}
Summary:        Shared library for manifold

%description -n %{sh_c_lib}
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package devel
Summary:        Development files for manifold
Requires:       %{sh_c_lib} = %{version}
Requires:       %{sh_lib} = %{version}
Requires:       cmake(Clipper2)
Requires:       cmake(assimp)

%description devel
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package -n python3-manifold
Summary:        Python bindings for manifold

%description -n python3-manifold
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%prep
%autosetup -p1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif

%cmake \
  -DMANIFOLD_USE_BUILTIN_manifold=OFF \
  -DMANIFOLD_EXPORT:BOOL=ON \
  -DMANIFOLD_PAR:BOOL=ON \
  %if %{with python_bindings}
  -DMANIFOLD_PYBIND:BOOL=ON \
  %else
  -DMANIFOLD_PYBIND:BOOL=OFF \
  %endif
  -DMANIFOLD_CBIND:BOOL=ON
%cmake_build

%install
%cmake_install

%if %{with manifold_testing}
%check
%ctest
%endif

%ldconfig_scriptlets -n %{sh_lib}
%ldconfig_scriptlets -n %{sh_c_lib}

%files -n %{sh_lib}
%license LICENSE
%{_libdir}/libmanifold.so.*

%files -n %{sh_c_lib}
%license LICENSE
%{_libdir}/libmanifoldc.so.*

%files devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmanifold.so
%{_libdir}/libmanifoldc.so
%{_includedir}/manifold/
%{_libdir}/cmake/manifold/
%{_libdir}/pkgconfig/manifold.pc

%if %{with python_bindings}
%files -n python3-manifold
%license LICENSE
%{python3_sitearch}/manifold3d.*.so
%{python3_sitearch}/manifold3d.pyi
%endif

%changelog
