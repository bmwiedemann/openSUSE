#
# spec file for package python-torch
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


#
%define srcname pytorch
%define skip_python2 1
%define pname torch



Name:           python-torch
Version:        1.4.0
Release:        0
Summary:        Deep learning framework aka pytorch/Caffe2
License:        BSD-2-Clause AND BSD-3-Clause AND MIT AND Zlib AND BSL-1.0 AND Apache-2.0
Group:          Development/Languages/Python
URL:            https://pytorch.org
Source0:        https://github.com/pytorch/pytorch/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source1:        releases.html
#License10: BSD-3-Clause
Source10:       https://github.com/facebookincubator/gloo/archive/7c541247a6fa49e5938e304ab93b6da661823d0f.tar.gz#/gloo-7c541247a6fa49e5938e304ab93b6da661823d0f.tar.gz
#License12: BSD-2-Clause
Source12:       https://github.com/pytorch/cpuinfo/archive/89fe1695edf9ee14c22f815f24bac45577a4f135.tar.gz#/cpuinfo-89fe1695edf9ee14c22f815f24bac45577a4f135.tar.gz
#License13: BSL-1.0
Source13:       https://github.com/zdevito/sleef/archive/7f523de651585fe25cade462efccca647dcc8d02.tar.gz#/sleef-7f523de651585fe25cade462efccca647dcc8d02.tar.gz
#License14: BSD-3-Clause
Source14:       https://github.com/pybind/pybind11/archive/25abf7efba0b2990f5a6dfb0a31bc65c0f2f4d17.tar.gz#/pybind11-25abf7efba0b2990f5a6dfb0a31bc65c0f2f4d17.tar.gz
# License15: MIT
Source15:       https://github.com/onnx/onnx/archive/fea8568cac61a482ed208748fdc0e1a8e47f62f5.tar.gz#/onnx-fea8568cac61a482ed208748fdc0e1a8e47f62f5.tar.gz
#License16: BSD-2-Clause
Source16:       https://github.com/Maratyszcza/pthreadpool/archive/13da0b4c21d17f94150713366420baaf1b5a46f4.tar.gz#/pthreadpool-13da0b4c21d17f94150713366420baaf1b5a46f4.tar.gz
# License17: MIT
Source17:       https://github.com/Maratyszcza/FXdiv/archive/b742d1143724d646cd0f914646f1240eacf5bd73.tar.gz#/FXdiv-b742d1143724d646cd0f914646f1240eacf5bd73.tar.gz
# License18: MIT
Source18:       https://github.com/Maratyszcza/psimd/archive/90a938f30ba414ada2f4b00674ee9631d7d85e19.tar.gz#/psimd-90a938f30ba414ada2f4b00674ee9631d7d85e19.tar.gz
# License19: MIT
Source19:       https://github.com/Maratyszcza/FP16/archive/febbb1c163726b5db24bed55cc9dc42529068997.tar.gz#/FP16-febbb1c163726b5db24bed55cc9dc42529068997.tar.gz
#License20: Apache-2.0
Source20:       https://github.com/google/gemmlowp/archive/3fb5c176c17c765a3492cd2f0321b0dab712f350.tar.gz#/gemmlowp-3fb5c176c17c765a3492cd2f0321b0dab712f350.tar.gz
#License21: MIT
Source21:       https://github.com/houseroad/foxi/archive/97fe555430a857581b9b826ecd955e4f0a3653f0.tar.gz#/foxi-97fe555430a857581b9b826ecd955e4f0a3653f0.tar.gz
# License22: MIT
Source22:       https://github.com/pytorch/QNNPACK/archive/7d2a4e9931a82adc3814275b6219a03e24e36b4c.tar.gz#/QNNPACK-7d2a4e9931a82adc3814275b6219a03e24e36b4c.tar.gz

Patch0:         removed-peachpy-depedency.patch
Patch1:         skip-third-party-check.patch

# A python call to cmake fails with a return code of 1 on this arch, disable it for now.
ExcludeArch:    %ix86

BuildRequires:  %{python_module Gloo}
%ifarch x86_64
BuildRequires:  %{python_module PeachPy}
%endif
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module leveldb}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module opcodes}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module rpm-macros}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module typing}
BuildRequires:  %{pythons}
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glog-devel
BuildRequires:  gtest
BuildRequires:  leveldb-devel
BuildRequires:  libnuma-devel
BuildRequires:  libopenblas_pthreads-devel
BuildRequires:  lmdb-devel
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  openblas-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-c
BuildRequires:  protobuf-devel
BuildRequires:  python-py-cpuinfo
BuildRequires:  python-pybind11-devel
BuildRequires:  snappy-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python-future
Requires:       python-leveldb
Requires:       python-numpy
Requires:       python-protobuf
Requires:       python-six

Provides:       python-caffe2 = %version
Provides:       python-pytorch = %version

%python_subpackages

%description
PyTorch enables fast, flexible experimentation and efficient production through
a hybrid front-end, distributed training, and ecosystem of tools and libraries.
The library is developed by Facebook and other groups.
PyTorch provides two high-level features:
* Tensor computing (like NumPy) with strong acceleration via graphics
* processing units (GPU) Deep neural networks built on a tape-based autodiff
  system

%package devel
Summary:        Headers for C/C++, cmake build description and libraries needed for development
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description devel
Although the Python interface is more polished and the primary focus of
development, PyTorch also has a C++ frontend. This package contains the header
to access the C/C++ interface.

%package -n pytorch-converters
Summary:        Converters for onnx and caffe2
Group:          Development/Languages/Python
BuildArch:      noarch
Requires:       python3-click
Requires:       python3-onnx
Requires:       python3-pip
Requires:       python3-pname

%description -n pytorch-converters
Converter from caffe2 to onnx and from caffe2 to onnx formated files.

%package -n pytorch-examples
Summary:        Examples which can be used for testing
Group:          Development/Languages/Python
BuildArch:      noarch
Recommends:     python3-lmdb
Recommends:     python3-networkx

%description -n pytorch-examples
This example files can be used to start an own pytorch/caffe2 project.

%package -n libtorch
Summary:        Library which used by %{name}
Group:          Development/Libraries/Python

%description -n libtorch 
Library which is used by %{name}

%prep
%define make_depend_src() test -e $(basename %1| sed 's/-.*//') && rmdir %{?2}%{!?2:$(basename %1| sed 's/-.*//')}; tar xzf %1; mv $(basename %1 | sed 's/\.tar\.gz//' ) %{?2}%{!?2:$(basename %1| sed 's/-.*//')}
%define make_depend_src_uppercase() rmdir -p $(basename %1| sed 's/-.*//'| tr '[:upper:]' '[:lower:]'); tar xzf %1; mv $(basename %1 | cut -f 1 -d '.' ) $(basename %1| sed 's/-.*//'| tr '[:upper:]' '[:lower:]') 
%setup -q -n %{srcname}-%{version}
cp %{S:1} releases.html
%autopatch -p 1
cd third_party
rmdir python-peachpy/
%make_depend_src %{SOURCE10}
%make_depend_src %{SOURCE12}
%make_depend_src %{SOURCE13}
%make_depend_src %{SOURCE14}
%make_depend_src %{SOURCE15}
%make_depend_src %{SOURCE16}
%make_depend_src %{SOURCE17}
%make_depend_src %{SOURCE18}
%make_depend_src %{SOURCE19}
%make_depend_src %{SOURCE20} gemmlowp/gemmlowp
%make_depend_src %{SOURCE21}
%make_depend_src %{SOURCE22}
# link system eigen to right place
rmdir eigen
ln -s /usr/include/eigen3 eigen
cd ..

%build
#export CC=gcc-7
#export CXX=g++-7
export USE_NNPACK=0
export USE_CUDNN=0
export USE_TEST=0
export USE_LEVELDB=ON
export USE_LMDB=ON
export USE_FBGEMM=0
export USE_SYSTEM_LIB="tbb,fbgemm,fbgemm/third_party/asmjit,onnx/third_party/benchmark"
export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_TEST=0
%limit_build -m 2000
export MAX_JOBS=%{?jobs}
%python_build

%install
export USE_NNPACK=0
export USE_CUDNN=0
export USE_TEST=0
export USE_LEVELDB=ON
export USE_LMDB=ON
export USE_FBGEMM=0
export USE_SYSTEM_LIB="tbb,fbgemm,fbgemm/third_party/asmjit,onnx/third_party/benchmark"
export BUILD_CUSTOM_PROTOBUF=OFF
export BUILD_TEST=1
%limit_build -m 2000
export MAX_JOBS=%{?jobs}
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitearch}

install -m 755 -D caffe2/python/examples/* -t %{buildroot}%{_docdir}/%{name}/
install -m 644 -D %{buildroot}%{python_sitearch}/torch/lib/* %{buildroot}/%{_libdir}
#rm -r %{buildroot}%{python_sitearch}/torch/lib
#cd %{buildroot}/%{_libdir}
#rm libtorch.so
#ln -s libtorch.so.1 libtorch.so
#cd -
#for file in  $(find %{buildroot}%{python_sitearch} -type f -name \*.py -perm 644 -size +1b); do
#%{__grep} '/usr/bin/env ' $file && sed -i 's@/usr/bin/env python@/usr/bin/python@' $file && chmod 755 $file 
#done
#
#%check
#export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test/run_test.py

%post -n libtorch -p /sbin/ldconfig
%postun -n libtorch -p /sbin/ldconfig

%files %{python_files}
%defattr(-,root,root)
%doc README.md NOTICE releases.html
%license LICENSE
%{python_sitearch}/torch/
%{python_sitearch}/caffe2/
%{python_sitearch}/torch-*.egg-info/
# excluding nearly all headersm except THNN.h and THCUNN.h as they
# are read in by the python init
%exclude %{python_sitearch}/torch/share
%exclude %{python_sitearch}/torch/include/TH
%exclude %{python_sitearch}/torch/include/c10
%exclude %{python_sitearch}/torch/include/ATen
%exclude %{python_sitearch}/torch/include/pybind11
%exclude %{python_sitearch}/torch/include/caffe2
%exclude %{python_sitearch}/torch/include/torch/csrc
%exclude %{python_sitearch}/torch/include/torch/*.h

%files %{python_files devel}
%{python_sitearch}/torch/share
%{python_sitearch}/torch/include/TH/
%{python_sitearch}/torch/include/c10
%{python_sitearch}/torch/include/ATen
%{python_sitearch}/torch/include/pybind11
%{python_sitearch}/torch/include/caffe2
%{python_sitearch}/torch/include/torch/csrc
%{python_sitearch}/torch/include/torch/*.h

%files -n pytorch-converters
%{_bindir}/convert-caffe2-to-onnx
%{_bindir}/convert-onnx-to-caffe2

%files -n pytorch-examples
%{_docdir}/%{name}

%files -n libtorch
%{_libdir}/*.so*

%changelog
