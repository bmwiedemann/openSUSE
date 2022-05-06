#
# spec file for package python-onnxconverter-common
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-onnxconverter-common
Version:        1.9.0
Release:        0
Summary:        ONNX Converter and Optimization Tools
License:        MIT
URL:            https://github.com/microsoft/onnxconverter-common
Source:         https://github.com/microsoft/onnxconverter-common/archive/v%{version}.tar.gz#/onnxconverter_common-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module onnx}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-onnx
Requires:       python-protobuf
BuildArch:      noarch
%python_subpackages

%description
The onnxconverter-common package provides common functions and utilities for
use in converters from various AI frameworks to ONNX. It also enables the
different converters to work together to convert a model from mixed frameworks,
like a scikit-learn pipeline embedding a xgboost model.

%prep
%setup -q -n onnxconverter-common-%{version}

%build
%python_build
dos2unix README.md

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no onnxruntime in Factory
ignorefiles="--ignore tests/test_float16.py"
ignorefiles+=" --ignore tests/test_onnx2py.py"
ignorefiles+=" --ignore tests/test_onnxfx.py"
ignorefiles+=" --ignore tests/test_auto_mixed_precision.py"
%pytest $ignorefiles

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/onnxconverter_common
%{python_sitelib}/onnxconverter_common-%{version}*-info

%changelog
