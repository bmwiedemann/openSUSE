#
# spec file for package arm-ml-examples
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


# Disable CAFFE and Tensorflow since it has been dropped in latest armnn
%bcond_with armnn_caffe
%bcond_with armnn_tf

# Disable ONNX due to https://github.com/ARM-software/armnn/issues/292
%bcond_with armnn_onnx

# Enable TensorFlowLite
%bcond_without armnn_tflite

Name:           arm-ml-examples
Version:        0.0~git20200114.7f6276c
Release:        0
Summary:        Machine learning examples used in Arm's ML developer space
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            https://developer.arm.com/products/processors/machine-learning/arm-nn
Source0:        ML-examples-%{version}.tar.xz
BuildRequires:  armnn-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_test-devel
%if %{with armnn_tflite} && %{with armnn_onnx}
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%endif
# Examples are useful only with the data
Requires:       arm-ml-examples-data
ExcludeArch:    %ix86

%description
Source code for machine learning tutorials and examples used in Arm's ML developer space.

%package data
Summary:        Data files for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description data
Data used by machine learning tutorials and examples from Arm's ML developer space.

%prep
%setup -q -n ML-examples-%{version}

%build
export ARMNN_LIB=/usr/lib
export ARMNN_INC=%{_includedir}
%if %{with armnn_tflite} && %{with armnn_onnx}
export BOOST_ROOT=%{_libdir}/..
pushd armnn-mobilenet-quant
%if "%{_libdir}" == "/usr/lib64"
sed -i -e 's#BOOST_ROOT)/lib#BOOST_ROOT)/lib64#' Makefile
%endif
make
popd
%endif
pushd armnn-mnist
# Needs CaffeParser and/or TensorFlowParser enabled in armnn
%if %{with armnn_caffe}
make mnist_caffe
%endif
%if %{with armnn_tf}
make mnist_tf
%endif
popd

%install
install -d %{buildroot}%{_bindir}
%if %{with armnn_tflite} && %{with armnn_onnx}
pushd armnn-mobilenet-quant
cp mobilenetv1_quant_tflite %{buildroot}%{_bindir}/
popd
%endif
pushd armnn-mnist
%if %{with armnn_caffe}
cp mnist_caffe %{buildroot}%{_bindir}/
%endif
%if %{with armnn_tf}
cp mnist_tf %{buildroot}%{_bindir}/
%endif
# Install examples data
mkdir -p  %{buildroot}%{_datadir}/armnn-mnist/
cp -r data/ model/  %{buildroot}%{_datadir}/armnn-mnist/
popd

%check
pushd armnn-mnist
%if %{with armnn_caffe}
./mnist_caffe
%endif
%if %{with armnn_tf}
./mnist_tf
%endif
popd

%if %{with armnn_caffe} || %{with armnn_tf}
%files
%defattr(-,root,root)
%{_bindir}/*
%endif

%files data
%dir %{_datadir}/armnn-mnist
%dir %{_datadir}/armnn-mnist/data
%dir %{_datadir}/armnn-mnist/model
%{_datadir}/armnn-mnist/data/*
%{_datadir}/armnn-mnist/model/*

%changelog
