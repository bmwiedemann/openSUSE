#
# spec file for package mkl-dnn
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define _lto_cflags %{nil}

Name:           mkl-dnn
Version:        1.1.3
Release:        0
Summary:        Intel(R) Math Kernel Library for Deep Neural Networks
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://01.org/mkl-dnn
Source0:        %{name}-v%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  texlive-dvips-bin
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

%description
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%package -n benchdnn
Summary:        Header files of Intel(R) Math Kernel Library
Group:          Development/Languages/C and C++
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
Group:          Development/Languages/C and C++
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
Group:          Documentation/HTML

%description doc
The reference documentation for the Intel(R) Math Kernel Library can be installed
with this package.

%package -n %{libname}
Summary:        Header files of Intel(R) Math Kernel Library
Group:          Development/Languages/C and C++

%description -n %{libname}
Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%prep
%setup -q -n %{name}-v%{version}

%build
# If ARCH_OPT_FLAGS is not 'unset', -march=native would be use what could
# lead to cryptic optimizations as build server may have different CPUs
export ARCH_OPT_FLAGS=""
export DNNL_CPU_RUNTIME=OMP
%cmake
%make_jobs
make doc

%install
%cmake_install
# move LICENSE to correct locations
mkdir -pv %{buildroot}%{_docdir}/%{name}
#mv %{buildroot}/usr/share/doc/mkldnn/LICENSE %{buildroot}%{_docdir}/%{name}
# move header files to correct location
mkdir -pv %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h* %{buildroot}%{_includedir}/%{name}
# install the benchmark
install -D build/tests/benchdnn/benchdnn %{buildroot}/%{_bindir}/benchdnn 
#install -D tests/benchdnn/README.md  %{buildroot}/%{_datadir}/benchdnn/README.md
#cp -vr build/tests/benchdnn/inputs %{buildroot}/%{_datadir}/benchdnn/
# move reference documentation to right place
mv %{buildroot}/usr/share/doc/dnnl %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_docdir}/%{name}
#move install shared lib
mv %{buildroot}/usr/usr/lib64/* %{buildroot}/usr/lib64/
rmdir -v %{buildroot}/usr/usr/lib64
rmdir -v %{buildroot}/usr/usr
mkdir -vp %{buildroot}%{_datadir}/benchdnn
cp -vr build/tests/benchdnn/inputs  %{buildroot}%{_datadir}/benchdnn
%check
cd build
#LD_LIBRARY_PATH=%{buildroot}/usr/lib64 make test

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n benchdnn
%defattr(-,root,root)
%{_bindir}/benchdnn
%{_datadir}/benchdnn

%files devel
%defattr(-,root,root)
%doc README.md 
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/cmake/dnnl

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}
%license LICENSE

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%changelog
