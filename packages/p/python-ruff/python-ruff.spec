#
# spec file for package python-ruff
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-ruff
Version:        0.5.1
Release:        0
Summary:        An extremely fast Python linter, written in Rust
License:        MIT
URL:            https://github.com/astral-sh/ruff
Source:         https://files.pythonhosted.org/packages/source/r/ruff/ruff-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildRequires:  alts
%python_subpackages

%description
Ruff extremely fast Python linter written in rust supperseding many other linting tools

%prep
%autosetup -a1 -p1 -n ruff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/ruff
%python_group_libalternatives ruff

%pre
%python_libalternatives_reset_alternative ruff

%files %{python_files}
%python_alternative %{_bindir}/ruff
%{python_sitearch}/ruff
%{python_sitearch}/ruff-%{version}.dist-info

%changelog
