#
# spec file for package python-safetensors
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-safetensors
Version:        0.4.5
Release:        0
Summary:        Safetensors is a simple format for storing tensors safely
License:        Apache-2.0
URL:            https://github.com/huggingface/safetensors
Source:         https://github.com/huggingface/safetensors/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module torch}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
%python_subpackages

%description
This repository implements a new simple format for storing tensors safely (as
opposed to pickle) and that is still fast (zero-copy).

%prep
%autosetup -p1 -n safetensors-%{version} -a1

%build
cd bindings/python
%pyproject_wheel

%install
cd bindings/python
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}/*

%check
cd bindings/python
# No tensorflow or jax
ignore="--ignore tests/test_tf_comparison.py --ignore tests/test_flax_comparison.py"
# PyTorch breaks under Python 3.13 currently
dontest="not (test_deserialization_safe or test_difference_torch_odd or test_difference_with_torch)"
%pytest_arch $ignore -k "$dontest" tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/safetensors
%{python_sitearch}/safetensors-%{version}.dist-info

%changelog
