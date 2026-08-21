#
# spec file for package python-kornia
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
Name:           python-kornia
Version:        0.8.3
Release:        0
Summary:        Differentiable computer vision library for PyTorch
License:        Apache-2.0
URL:            https://github.com/kornia/kornia
Source:         https://files.pythonhosted.org/packages/source/k/kornia/kornia-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module kornia-rs >= 0.1.9}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module torch >= 2.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kornia-rs >= 0.1.9
Requires:       python-packaging
Requires:       python-torch >= 2.0.0
BuildArch:      noarch
# python-kornia-rs is ExclusiveArch %%{rust_tier1_arches}; also matches
# Factory python-torch (no ix86/arm).
ExclusiveArch:  %{rust_tier1_arches}
%python_subpackages

%description
Kornia is a differentiable computer vision library built on PyTorch.
It provides image processing operators, geometric transforms, feature
detection, and augmentations that integrate with autograd and GPU
acceleration.

%prep
%autosetup -p1 -n kornia-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/kornia
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream tests are not in the sdist (NixOS also skips them: the
# suite hangs with no single test clearly responsible).
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import kornia; assert kornia.__version__ == '%{version}', kornia.__version__"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/kornia
%{python_sitelib}/kornia-%{version}.dist-info

%changelog
