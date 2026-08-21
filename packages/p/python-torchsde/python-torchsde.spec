#
# spec file for package python-torchsde
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-torchsde
Version:        0.2.6
Release:        0
Summary:        SDE solvers and stochastic adjoint sensitivity analysis in PyTorch
License:        Apache-2.0
URL:            https://github.com/google-research/torchsde
Source:         https://files.pythonhosted.org/packages/source/t/torchsde/torchsde-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.5}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module torch >= 1.6.0}
BuildRequires:  %{python_module trampoline >= 0.1.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# The auto Python dep generator does not pick up Requires-Dist from this
# setuptools wheel (RPM only gets python(abi)); declare them by hand.
Requires:       python-numpy >= 1.19
Requires:       python-scipy >= 1.5
Requires:       python-torch >= 1.6.0
Requires:       python-trampoline >= 0.1.2
BuildArch:      noarch
# Match Factory python-torch (ExcludeArch: %%ix86 %%{arm})
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
PyTorch implementation of differentiable stochastic differential
equation (SDE) solvers with GPU support and efficient
backpropagation.

This is a research project, not an official Google product.

%prep
%autosetup -p1 -n torchsde-%{version}
rm -rf torchsde.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The upstream suite is large and GPU-oriented (Fedora: thousands of
# tests, many skipped without CUDA). Restrict %%check to an import
# smoke test of the installed package under every Python flavour.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import torchsde"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/torchsde
%{python_sitelib}/torchsde-%{version}.dist-info

%changelog
