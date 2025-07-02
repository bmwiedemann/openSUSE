#
# spec file for package python-faiss
#
# Copyright (c) 2025 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == ""
%bcond_with cuda
%endif
%if "%flavor" == "cuda"
%bcond_without cuda
%define psuffix -cuda
%define cudavers -12-4
%endif

%if 0%{?sle_version} && 0%{?sle_version} < 160000
%global force_gcc_version 12
%endif


%{?sle15_python_module_pythons}

Name:           python-faiss%{?psuffix}
Version:        1.10.0
Release:        0
Summary:        A library for efficient similarity search and clustering of dense vectors
License:        MIT
URL:            https://ai.meta.com/tools/faiss/
Source0:        faiss-%{version}.tar
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  libopenblas_openmp-devel
BuildRequires:  onednn-devel
BuildRequires:  openblas-common-devel
%if %{with cuda}
BuildRequires:  cuda-cudart-devel%cudavers
BuildRequires:  cuda-nvcc%cudavers
BuildRequires:  cuda-profiler-api%cudavers
BuildRequires:  libcublas-devel%cudavers
BuildRequires:  libcurand-devel%cudavers
%endif
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  ffcall
BuildRequires:  lapack-devel
BuildRequires:  python-rpm-macros
BuildRequires:  suse-module-tools
BuildRequires:  swig
Requires:       python-numpy
Requires:       python-packaging
%python_subpackages

%description
Faiss is a library for efficient similarity search and clustering of dense
vectors. It contains algorithms that search in sets of vectors of any size,
 up to ones that possibly do not fit in RAM. It also contains supporting
code for evaluation and parameter tuning. Faiss is written in C++ with
complete wrappers for Python/numpy. Some of the most useful algorithms
are implemented on the GPU. It is developed by Facebook AI Research.

%package -n faiss-devel
Summary:        Development headers for faiss
Requires:       libfaiss

%description -n faiss-devel
These are the header for C and C++ of faiss

%package -n libfaiss
Summary:        faiss library

%description -n libfaiss
Faiss is a library for efficient similarity search and clustering of dense
vectors. It contains algorithms that search in sets of vectors of any size,
 up to ones that possibly do not fit in RAM. It also contains supporting
code for evaluation and parameter tuning. Faiss is written in C++ with
complete wrappers for Python/numpy. Some of the most useful algorithms
are implemented on the GPU. It is developed by Facebook AI Research.

%prep
%autosetup -p1 -n faiss-%{version}

%build
%if %{with cuda}
export PATH=/usr/local/cuda-12.4/bin:${PATH}
export CC=gcc-12
export CXX=g++-12
%endif
%if 0%{?sle_version} == 150600
export CC=gcc-12
export CXX=g++-12
%endif

# Always compile with AVX512 as seperate libaries will be built
%cmake \
  -DCMAKE_SKIP_RPATH=ON \
%if %{with cuda}
  -DFAISS_ENABLE_GPU=ON \
  -DCMAKE_CUDA_FLAGS="-allow-unsupported-compiler" \
%else
  -DFAISS_ENABLE_GPU=OFF \
%endif
  -DFAISS_ENABLE_C_API=ON \
  -DFAISS_ENABLE_PYTHON=OFF \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_STATIC_LIBS=OFF \
  -DBUILD_TESTING=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DFAISS_ENABLE_DNNL=ON \
  -DFAISS_OPT_LEVEL=avx512

%cmake_build faiss
cd ..
%{python_expand # need to disable the standard eror from the linker for
# undefined symbols as swig doesn't create all the functions
%if %{with cuda}
export PATH=/usr/local/cuda-12.1/bin:${PATH}
%endif
%cmake \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_SKIP_RPATH=ON \
%if %{with cuda}
  -DFAISS_ENABLE_GPU=ON \
  -DCMAKE_CUDA_FLAGS="-allow-unsupported-compiler" \
%else
  -DFAISS_ENABLE_GPU=OFF \
%endif
  -DFAISS_ENABLE_C_API=ON \
  -DFAISS_ENABLE_PYTHON=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_STATIC_LIBS=OFF \
  -DBUILD_TESTING=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DFAISS_ENABLE_DNNL=ON \
%ifarch x86_64
  -DFAISS_OPT_LEVEL=avx512 \
%endif
  %{nil}

%cmake_build \
        faiss \
        swigfaiss \
        c_api \
%ifarch x86_64
         swigfaiss_avx2 \
         swigfaiss_avx512 \
%endif
         %{nil}
cd faiss/python
%pyproject_wheel
cd ../../..
}
cd %{__builddir}/faiss/python

%install
%cmake_install
# c lib is build not installed
install -D ./build/c_api/libfaiss_c.so %{buildroot}%{_libdir}/libfaiss_c.so
cd %{__builddir}/faiss/python
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%{python_expand test -e %{_libdir}/libfaiss_python_callbacks.so || ln -s %{$python_sitelib}/faiss/libfaiss_python_callbacks.so %{_libdir}/libfaiss_python_callbacks.so}

%postun
%{python_expand test -e %{_libdir}/libfaiss_python_callbacks.so || rm -f %{_libdir}/libfaiss_python_callbacks.so}

%files %{python_files}
%{python_sitelib}/faiss
%{python_sitelib}/faiss-%{version}.dist-info
%ghost %{_libdir}/libfaiss_python_callbacks.so

%files -n faiss-devel
%{_includedir}/faiss/*
%dir %{_includedir}/faiss
%{_datadir}/faiss

%files -n libfaiss
%{_libdir}/libfaiss.so
%{_libdir}/libfaiss_c.so
%ifarch x86_64
%{_libdir}/libfaiss_avx2.so
%{_libdir}/libfaiss_avx512.so
%endif

%changelog
