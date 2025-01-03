#
# spec file for package tbb
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Alessandro de Oliveira Faria (A.K.A. CABELO)
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


%define so_ver 12
%define so_ver_malloc 2
%define so_ver_irml 1
%define so_ver_bind 3
%if %{pkg_vcmp hwloc-devel >= 2.5}
%define tbbbind_suffix _2_5
%else
%if %{pkg_vcmp hwloc-devel >= 2}
%define tbbbind_suffix _2_0
%else
%define tbbbind_suffix %{nil}
%endif
%endif
# by default, don't compile all the tests
%bcond_with test

%if 0%{suse_version} >= 1500
%{?!python_module:%define python_module() python3-%{**}}
%bcond_without python3
%define skip_python2 1
%else
%bcond_with python3
%endif
Name:           tbb
Version:        2022.0.0
Release:        0
Summary:        oneAPI Threading Building Blocks (oneTBB)
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://oneapi-src.github.io/oneTBB/
Source0:        https://github.com/oneapi-src/oneTBB/archive/v%{version}.tar.gz#/tbb-%{version}.tar.gz
Source99:       tbb-rpmlintrc
# PATCH-FIX-OPENSUSE cmake-remove-include-path.patch -- openCV include error
Patch2:         cmake-remove-include-path.patch
Patch4:         add-cmake-check-for-libatomic-requirement-when-build.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
%if %{with python3}
BuildRequires:  %{python_module devel >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  swig >= 3.0.6
%endif
%if 0%{?suse_version} > 1500
# if python multiflavor is available (Tumbleweed), use it to generate subpackages
%define python_subpackage_only 1
%python_subpackages
%else
# unified defaults for the package file list
%define pycache_only %{nil}
%define python_sitearch %{python3_sitearch}
%define python_files() -n python3-%{**}
%endif

%description
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

%package -n libtbb%{so_ver}
Summary:        Core library for oneAPI Threading Building Blocks
Group:          System/Libraries
Provides:       %{name} = %{version}
Provides:       onetbb = %{version}
Obsoletes:      %{name} < %{version}

%description -n libtbb%{so_ver}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This package provides the core shared library corresponding to oneTBB.

%package -n libtbbmalloc%{so_ver_malloc}
Summary:        Memory allocator library for oneAPI Threading Building Blocks
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libtbbmalloc%{so_ver_malloc}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This package provides the oneTBB memory allocator shared library.

%package -n libirml%{so_ver_irml}
Summary:        IPC library for oneAPI Threading Building Blocks
Group:          System/Libraries

%description -n libirml%{so_ver_irml}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This subpackage provides the library required in order to enable inter-process
(IPC) coordination between oneTBB schedulers for the oneTBB python module.

%package -n libtbbbind%{tbbbind_suffix}-%{so_ver_bind}
Summary:        NUMA support library for oneAPI Threading Building Blocks
Group:          System/Libraries

%description -n libtbbbind%{tbbbind_suffix}-%{so_ver_bind}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

The NUMA support library for oneTBB.

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Summary:        Python bindings for oneAPI Threading Building Blocks
Group:          Development/Languages/Python
Requires:       libirml%{so_ver_irml}

%description -n python-%{name}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This package contains python %{python_version} bindings for oneTBB.

%else

%package -n python3-%{name}
Summary:        Python 3 bindings for oneAPI Threading Building Blocks
Group:          Development/Languages/Python
Requires:       libirml%{so_ver_irml}

%description -n python3-%{name}
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This package contains python 3 bindings for oneAPI Threading Building Blocks
(oneTBB).
%endif

%package devel
Summary:        Development Files for oneAPI Threading Building Blocks (oneTBB)
Group:          Development/Libraries/C and C++
Requires:       c++_compiler
Requires:       libirml%{so_ver_irml} = %{version}
Requires:       libtbb%{so_ver} = %{version}
Requires:       libtbbbind%{tbbbind_suffix}-%{so_ver_bind} = %{version}
Requires:       libtbbmalloc%{so_ver_malloc} = %{version}

%description devel
oneTBB (previously known as TBB) is a flexible C++ library that simplifies the
work of adding parallelism to complex applications. The library lets you easily
write parallel programs that take full advantage of the multi-core performance.
oneTBB provides you with functions, interfaces, and classes to parallelize and
scale the code.

This package contains the header files needed for development with oneTBB.

%prep
%setup -q -n oneTBB-%{version}
%autopatch -p1

# fix python version
sed -i 's/version\s*="0.2"/version = "%{version}"/' python/setup.py
sed -i '1{/^#!.*env python/ d}' python/TBB.py python/tbb/*.py

%build
# HWLOC: no automatic find on SLE-12 (older cmake)
# TBB_TEST: don't compile by default
# TBB4PY: use cmake build system to build libirml in the python tree
%cmake \
%if 0%{suse_version} < 1500
  -DCMAKE_HWLOC_2_LIBRARY_PATH=%{_libdir}/libhwloc.so \
  -DCMAKE_HWLOC_2_INCLUDE_PATH=%{_includedir}/hwloc \
%endif
%if ! %{with test}
  -DTBB_TEST:BOOL=OFF \
%endif
%if %{with python3}
  -DTBB4PY_BUILD:BOOL=ON \
%endif

# Leap 15.2 encounters oom during compilation
%cmake_build \
%if 0%{?sle_version} == 150200
  -j 4
%endif

source */vars.sh
cd ..

# rebuild for every python flavor
%if %{with python3}
pushd python
%python_build
popd
%endif

%install
# create empty python build dir (?)
mkdir -p build/python/build
%cmake_install

source build/*/vars.sh

%if %{with python3}
pushd python
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
popd
%endif

# we install it into the devel package docdir
rm -rf %{buildroot}%{_datadir}/doc/

# Rename tbb32.pc to tbb.pc (same as 64-bit) so that applications depending on tbb
# do not have to call different pkgconfig modules based on arch
test -f %{buildroot}%{_libdir}/pkgconfig/tbb32.pc && mv %{buildroot}%{_libdir}/pkgconfig/tbb32.pc %{buildroot}%{_libdir}/pkgconfig/tbb.pc

%check
%if %{with test}
%ctest --exclude-regex python_test
%endif
# always test python modules, if they are built
%if %{with python3}
# avoid shuffling the existing build dir
mkdir python-test
pushd python-test
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} timeout 5m $python -m tbb test -v
popd
%endif

%post -n libtbb%{so_ver} -p /sbin/ldconfig
%postun -n libtbb%{so_ver} -p /sbin/ldconfig
%post -n libtbbmalloc%{so_ver_malloc} -p /sbin/ldconfig
%postun -n libtbbmalloc%{so_ver_malloc} -p /sbin/ldconfig
%post -n libirml%{so_ver_irml} -p /sbin/ldconfig
%postun -n libirml%{so_ver_irml} -p /sbin/ldconfig
%post -n libtbbbind%{tbbbind_suffix}-%{so_ver_bind} -p /sbin/ldconfig
%postun -n libtbbbind%{tbbbind_suffix}-%{so_ver_bind} -p /sbin/ldconfig

%files -n libtbb%{so_ver}
%{_libdir}/libtbb.so.%{so_ver}*

%files -n libtbbmalloc%{so_ver_malloc}
%{_libdir}/libtbbmalloc.so.%{so_ver_malloc}*
%{_libdir}/libtbbmalloc_proxy.so.%{so_ver_malloc}*

%files -n libtbbbind%{tbbbind_suffix}-%{so_ver_bind}
%{_libdir}/libtbbbind%{tbbbind_suffix}.so.%{so_ver_bind}*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/tbb/
%{_includedir}/oneapi/
%{_libdir}/cmake/TBB
%{_libdir}/pkgconfig/tbb.pc
%{_libdir}/libtbb.so
%{_libdir}/libtbbmalloc.so
%{_libdir}/libtbbmalloc_proxy.so
%{_libdir}/libtbbbind%{tbbbind_suffix}.so
%if %{with python3}
%{_libdir}/libirml.so
%endif

%if %{with python3}
%files -n libirml%{so_ver_irml}
%{_libdir}/libirml.so.%{so_ver_irml}*

%files %{python_files %{name}}
%{python_sitearch}/tbb
%{python_sitearch}/TBB.py
%{python_sitearch}/TBB-*py3*
%{python_sitearch}/TBB-%{version}*-info
%pycache_only %{python_sitearch}/__pycache__/TBB*
%endif

%changelog
