#
# spec file for package python-ty
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-ty
Version:        0.0.4
Release:        0
Summary:        An extremely fast Python type checker and language server, written in Rust
License:        MIT
URL:            https://github.com/astral-sh/ty
Source:         https://files.pythonhosted.org/packages/source/t/ty/ty-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       ty = %{version}-%{release}
Requires:       alts
BuildRequires:  alts
%python_subpackages

%description
An extremely fast Python type checker and language server, written in Rust.

%prep
%autosetup -a1 -p1 -n ty-%{version}
# Set consistent mtime for all files to fix python-bytecode-inconsistent-mtime
find . -type f -exec touch -h -r %{SOURCE0} {} +
# Remove dots from summaries to satisfy rpmlint
sed -i 's/description = ".*."/description = "An extremely fast Python type checker, written in Rust"/' pyproject.toml ruff/crates/ty/Cargo.toml
mv ruff/.cargo .
mv ruff/vendor .

%build
export CARGO_NET_OFFLINE=true
%pyproject_wheel

%check
%{python_expand #
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=%{buildroot}%{$python_sitearch}
# Run the binary directly to ensure it works
%{buildroot}%{_bindir}/ty-%{$python_bin_suffix} --help
}

%install
export PYTHONDONTWRITEBYTECODE=1
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/ty
%python_group_libalternatives ty

%pre
%python_libalternatives_reset_alternative ty

%files %{python_files}
%python_alternative %{_bindir}/ty
%{python_sitearch}/ty
%{python_sitearch}/ty-%{version}.dist-info

%changelog
