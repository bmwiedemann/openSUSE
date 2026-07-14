#
# spec file for package python-einops
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
Name:           python-einops
Version:        0.8.2
Release:        0
Summary:        A new flavour of deep learning operations
License:        MIT
URL:            https://github.com/arogozhnikov/einops
Source:         https://files.pythonhosted.org/packages/source/e/einops/einops-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.10.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Flexible and powerful tensor operations for readable and reliable code.
Supports numpy, pytorch, tensorflow, jax, and others.

%prep
%autosetup -p1 -n einops-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Only the numpy backend is exercised; torch/jax/tensorflow/paddle/oneflow
# backends are not in Factory, and their tests self-skip when not listed in
# EINOPS_TEST_BACKENDS.
export EINOPS_TEST_BACKENDS=numpy
%pytest --pyargs einops.tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/einops
%{python_sitelib}/einops-%{version}.dist-info

%changelog
