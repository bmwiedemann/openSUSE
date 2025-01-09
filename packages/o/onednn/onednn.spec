#
# spec file for package onednn
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


%define libname libdnnl3
%ifarch x86_64
%bcond_without opencl
%else
# Build broken on non-x86, with openCL
%bcond_with opencl
%endif
%ifarch aarch64
# Disable ACL until fixed upstream - https://github.com/oneapi-src/oneDNN/issues/2137
%bcond_with acl
%else
%bcond_with acl
%endif
Name:           onednn
Version:        3.6.2
Release:        0
Summary:        oneAPI Deep Neural Network Library (oneDNN)
License:        Apache-2.0
URL:            https://github.com/oneapi-src/oneDNN
Source0:        https://github.com/oneapi-src/oneDNN/archive/v%{version}/oneDNN-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  ninja
BuildRequires:  texlive-dvips-bin
Provides:       mkl-dnn = %{version}
Obsoletes:      mkl-dnn <= %{version}
Provides:       oneDNN = %{version}
ExclusiveArch:  x86_64 aarch64 ppc64le
%if %{with acl}
BuildRequires:  ComputeLibrary-devel >= 24.08.1
%endif
%if %{with opencl}
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
%endif

%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.

oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

%package -n benchdnn
Summary:        Header files of Intel Math Kernel Library
Requires:       %{libname} = %{version}

%description -n benchdnn
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package only includes the benchmark utility including its input files.

%package devel
Summary:        Header files of Intel Math Kernel Library
Requires:       %{libname} = %{version}
Provides:       mkl-dnn-devel = %{version}
Obsoletes:      mkl-dnn-devel <= %{version}
Provides:       oneDNN-devel = %{version}
%if %{with opencl}
Requires:       opencl-headers
Requires:       pkgconfig(OpenCL)
%endif

%description devel
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package includes the required headers and library files to develop software
with the Intel MKL-DNN.

%package doc
Summary:        Reference documentation for the Intel Math Kernel Library
BuildArch:      noarch

%description doc
The reference documentation for the Intel Math Kernel Library can be installed
with this package.

%package -n %{libname}
Summary:        Header files of Intel Math Kernel Library

%description -n %{libname}
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%prep
%autosetup -p1 -n oneDNN-%{version}

%build
%define __builder ninja
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DMKLDNN_ARCH_OPT_FLAGS="" \
  -DDNNL_CPU_RUNTIME=OMP \
%if %{with acl}
  -DDNNL_AARCH64_USE_ACL=ON \
  -DACL_INCLUDE_DIR=%{_includedir} \
  -DACL_LIBRARY=%{_libdir}/libarm_compute.so  \
%endif
%if %{with opencl}
  -DDNNL_GPU_RUNTIME=OCL \
%endif
  -DDNNL_INSTALL_MODE=DEFAULT \
  -DDNNL_BUILD_TESTS=ON \
  -DONEDNN_BUILD_GRAPH=ON \
  -DDNNL_WERROR=OFF
%cmake_build
%cmake_build doc_doxygen

%install
%cmake_install
# move the built doxygen data to normal location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/dnnl/reference/* %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_docdir}/%{name}
# do use macros to install license/docu
rm -r %{buildroot}%{_datadir}/doc/dnnl
# Keep compatibility with mkl-dnn
pushd %{buildroot}%{_includedir}
ln -s . mkl-dnn
popd
# install the benchmark
install -D build/tests/benchdnn/benchdnn %{buildroot}/%{_bindir}/benchdnn
# move install shared lib
mkdir -vp %{buildroot}%{_datadir}/benchdnn
cp -vr build/tests/benchdnn/inputs  %{buildroot}%{_datadir}/benchdnn

chrpath -d %{buildroot}/%{_bindir}/benchdnn

%check
# do not use macro so we can exclude all gpu and cross (gpu and cpu) tests (they need gpu set up)
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} -E '(gpu|cross)'
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n benchdnn
%{_bindir}/benchdnn
%{_datadir}/benchdnn

%files devel
%doc README.md
%license LICENSE
%{_includedir}/mkl-dnn
%{_includedir}/dnnl*.h*
%dir %{_includedir}/oneapi
%dir %{_includedir}/oneapi/dnnl
%{_includedir}/oneapi/dnnl/dnnl*.h*
%{_libdir}/libdnnl.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake

%files doc
%{_docdir}/%{name}

%files -n %{libname}
%license LICENSE
%{_libdir}/libdnnl.so.*

%changelog
