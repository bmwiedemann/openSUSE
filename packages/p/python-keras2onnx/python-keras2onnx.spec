#
# spec file for package python-keras2onnx
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
%define         skip_python2 1
Name:           python-keras2onnx
Version:        1.6.5
Release:        0
Summary:        Converts Machine Learning models to ONNX for use in Windows ML
License:        MIT
URL:            https://github.com/onnx/keras-onnx
Source:         https://github.com/onnx/keras-onnx/archive/v%{version}.tar.gz#/keras2onnx-%{version}.tar.gz
BuildRequires:  %{python_module Keras}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module fire}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module onnxconverter-common >= 1.6.5}
BuildRequires:  %{python_module onnx}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tensorflow}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Keras
Requires:       python-fire
Requires:       python-numpy
Requires:       python-onnx
Requires:       python-onnxconverter-common >= 1.6.5
Requires:       python-protobuf
Requires:       python-requests
Requires:       python-tensorflow
ExcludeArch:    %ix86
%python_subpackages

%description
The keras2onnx model converter enables users to convert Keras models into the
[ONNX](https://onnx.ai) model format.  Initially, the Keras converter was
developed in the project [onnxmltools](https://github.com/onnx/onnxmltools).
keras2onnx converter development was moved into an [independent
repository](https://github.com/onnx/keras-onnx) to support more kinds of Keras
models and reduce the complexity of mixing multiple converters.

%prep
%setup -q -n keras-onnx-%{version}
# remove bundled tf2onnx
rm -r keras2onnx/ktf2onnx

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/keras2onnx*

%changelog
