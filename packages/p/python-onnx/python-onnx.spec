#
# spec file for package python-onnx
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-onnx
Version:        1.6.0
Release:        0
Summary:        Open Neural Network eXchange
License:        MIT
URL:            https://onnx.ai/
Source0:        https://github.com/onnx/onnx/archive/v%{version}.tar.gz#/onnx-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pybind11}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel
BuildRequires:  python-pybind11-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-protobuf
Requires:       python-six
Requires:       python-typing_extensions >= 3.6.2.1
%python_subpackages

%description
Open format to represent deep learning models. With ONNX, AI developers can more easily move models between state-of-the-art tools and choose the combination that is best for them. ONNX is developed and supported by a community of partners.

%package devel
Summary:        C/C++ - header files which are used for development
Requires:       %{name} = %{version}

%description devel
The headers and other files needed for the development.

%prep
%setup -q -n onnx-%{version}
# avoid bundles
rm -rf third_party
# say that the cmake was already built (we used our macros)
sed -i -e 's:built = False:built = True:g' setup.py
# do not require extra pytest modules
sed -i -e '/addopts/d' setup.cfg
# do not pull in pytest-runner as it is deprecated
sed -i -e '/pytest-runner/d' setup.py

%build
# define same folder like is used for the setup.py later
%define __builddir .setuptools-cmake-build
# Force the cmake to build static libs as otherwise we end
# up with unresolvable package.
%{python_expand # we need to generate for each python
%cmake \
  -DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
  -DONNX_WERROR=OFF \
  -DBUILD_ONNX_PYTHON=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_STATIC_LIBS=ON \
  -DPY_EXT_SUFFIX="`$python-config --extension-suffix`"
%cmake_build ; cd ..
}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
shebang_files="%{python_sitearch}/onnx/backend/test/stat_coverage.py %{python_sitearch}/onnx/defs/gen_doc.py %{python_sitearch}/onnx/gen_proto.py"
for file in $shebang_files ; do
  sed -i 's@%{_bindir}/env python@%{_bindir}/python3@' %{buildroot}/$file
  chmod 755 %{buildroot}/$file
done

%check
export PYTHONDONTWRITEBYTECODE=1
# copy inplace for tests
cp %{__builddir}/*cpp2py* ./onnx/
# skip online tests
%pytest_arch -n auto -k 'not (test_bvlc_alexnet_cpu or test_shufflenet_cpu or test_densenet121_cpu or test_squeezenet_cpu or test_inception_v1_cpu or test_vgg19_cpu or test_inception_v2_cpu or test_zfnet512_cpu or test_resnet50_cpu)'

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/check-model
%python3_only %{_bindir}/check-node
%python3_only %{_bindir}/backend-test-tools
%{python_sitearch}/*
%exclude %{python_sitearch}/onnx/*.[hc]
%exclude %{python_sitearch}/onnx/common
%exclude %{python_sitearch}/onnx/optimizer
%exclude %{python_sitearch}/onnx/version_converter
%exclude %{python_sitearch}/onnx/shape_inference

%files %{python_files devel}
%{python_sitearch}/onnx/*.[hc]
%{python_sitearch}/onnx/common
%{python_sitearch}/onnx/optimizer
%{python_sitearch}/onnx/version_converter
%{python_sitearch}/onnx/shape_inference

%changelog
