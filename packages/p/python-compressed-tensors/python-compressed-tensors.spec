#
# spec file for package python-compressed-tensors
#
# Copyright (c) 2026 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-compressed-tensors
Version:        0.17.1
Release:        0
Summary:        Library for utilization of compressed safetensors of neural network models
License:        Apache-2.0
URL:            https://github.com/vllm-project/compressed-tensors
Source:         https://files.pythonhosted.org/packages/source/c/compressed_tensors/compressed_tensors-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-loguru
Requires:       python-pydantic >= 2.0
Requires:       python-torch >= 2.10.0
Requires:       python-transformers >= 4.45.0
BuildArch:      noarch
%python_subpackages

%description
compressed-tensors extends the safetensors format, providing a versatile
and efficient way to store and manage compressed (quantized and sparse)
tensor data for neural network models. It supports a variety of
quantization and sparsity schemes and integrates with the safetensors
storage layout used by machine-learning frameworks.

%prep
%autosetup -p1 -n compressed_tensors-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests are not run: the test suite requires the transformers Python
# module (not available in openSUSE:Factory) and most tests additionally
# require a GPU (upstream states "most tests do require a GPU"), so even
# an import smoke test fails without transformers in the build root.

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/compressed_tensors
%{python_sitelib}/compressed_tensors-%{version}.dist-info

%changelog
