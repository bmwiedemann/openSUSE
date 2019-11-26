#
# spec file for package python-onnx
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1

Name:           python-onnx
Version:        1.6.0
Release:        0
License:        MIT
Summary:        Open Neural Network Exchange
Url:            https://onnx.ai/
Group:          Development/Languages/Python
Source0:        https://github.com/onnx/onnx/archive/v%{version}.tar.gz#/onnx-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pybind11}
BuildRequires:  python-pybind11-devel
BuildRequires:  fdupes
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel
Requires:       python-numpy
Requires:       python-protobuf
Requires:       python-six
Requires:       python-typing_extensions >= 3.6.2.1
Suggests:       python-mypy >= 0.600

%python_subpackages

%description
Open format to represent deep learning models. With ONNX, AI developers can more easily move models between state-of-the-art tools and choose the combination that is best for them. ONNX is developed and supported by a community of partners.

%package devel
Summary:        C/C++ - header files which are used for development
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description devel
The headers and other files needed for the development.

%prep
%setup -q -n onnx-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
shebang_files="%{python_sitearch}/onnx/backend/test/stat_coverage.py %{python_sitearch}/onnx/defs/gen_doc.py %{python_sitearch}/onnx/gen_proto.py"
for file in $shebang_files ; do
  sed -i 's@/usr/bin/env python@/usr/bin/python3@' %{buildroot}/$file
  chmod 755 %{buildroot}/$file
done
# check fails with buitling typing of python 3.7.3
# https://github.com/pybind/pybind11/issues/1949

%files %{python_files}
%doc LICENSE README.md
%python3_only %{_bindir}/check-model
%python3_only %{_bindir}/check-node
%python3_only %{_bindir}/backend-test-tools
%{python_sitearch}/*
%exclude %{python_sitearch}/onnx/*.[hc]
%exclude %{python_sitearch}/onnx/common
%exclude %{python_sitearch}/onnx/defs
%exclude %{python_sitearch}/onnx/optimizer
%exclude %{python_sitearch}/onnx/version_converter
%exclude %{python_sitearch}/onnx/shape_inference

%files %{python_files devel}
%{python_sitearch}/onnx/*.[hc]
%{python_sitearch}/onnx/common
%{python_sitearch}/onnx/defs
%{python_sitearch}/onnx/optimizer
%{python_sitearch}/onnx/version_converter
%{python_sitearch}/onnx/shape_inference

%changelog
