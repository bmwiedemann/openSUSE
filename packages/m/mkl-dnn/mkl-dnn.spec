#
# spec file for package mkl-dnn
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libdnnl1
Name:           mkl-dnn
Version:        1.1.3
Release:        0
Summary:        Intel(R) Math Kernel Library for Deep Neural Networks
License:        Apache-2.0
URL:            https://01.org/mkl-dnn
Source0:        https://github.com/intel/mkl-dnn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cmake-no-install-ocl-cmake.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  texlive-dvips-bin
BuildRequires:  pkgconfig(OpenCL)
ExclusiveArch:  x86_64

%description
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%package -n benchdnn
Summary:        Header files of Intel(R) Math Kernel Library
Requires:       %{libname} = %{version}

%description -n benchdnn
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package only includes the benchmark utility including its input files.

%package devel
Summary:        Header files of Intel(R) Math Kernel Library
Requires:       %{libname} = %{version}

%description devel
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package includes the required headers and library files to develop software
with the Intel(R) MKL-DNN.

%package doc
Summary:        Reference documentation for the Intel(R) Math Kernel Library
BuildArch:      noarch

%description doc
The reference documentation for the Intel(R) Math Kernel Library can be installed
with this package.

%package -n %{libname}
Summary:        Header files of Intel(R) Math Kernel Library

%description -n %{libname}
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DMKLDNN_ARCH_OPT_FLAGS="" \
  -DDNNL_CPU_RUNTIME=OMP \
  -DDNNL_GPU_RUNTIME=OCL \
  -DDNNL_INSTALL_MODE=DEFAULT \
  -DDNNL_BUILD_TESTS=ON \
  -DDNNL_WERROR=OFF
%cmake_build
%cmake_build doc

%install
%cmake_install
# move the built doxygen data to normal location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/dnnl/reference/* %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_docdir}/%{name}
# do use macros to install license/docu
rm -r %{buildroot}%{_datadir}/doc/dnnl
# move header files to correct location
mkdir -pv %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h* %{buildroot}%{_includedir}/%{name}
# install the benchmark
install -D build/tests/benchdnn/benchdnn %{buildroot}/%{_bindir}/benchdnn
#move install shared lib
mkdir -vp %{buildroot}%{_datadir}/benchdnn
cp -vr build/tests/benchdnn/inputs  %{buildroot}%{_datadir}/benchdnn

%check
# do not use macro so we can exclude all gpu and cross (gpu and cpu) tests (they need gpu set up)
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
ctest --output-on-failure --force-new-ctest-process %{_smp_mflags} -E '(gpu|cross)'
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n benchdnn
%{_bindir}/benchdnn
%{_datadir}/benchdnn

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/dnnl

%files doc
%{_docdir}/%{name}

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%changelog
