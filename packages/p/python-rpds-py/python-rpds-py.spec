#
# spec file for package python-rpds-py
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%{?sle15_python_module_pythons}
Name:           python-rpds-py
Version:        2026.6.3
Release:        0
Summary:        Python bindings to Rust's persistent data structures (rpds)
License:        MIT
URL:            https://github.com/Julian/rpds.py
Source0:        https://files.pythonhosted.org/packages/source/r/rpds-py/rpds_py-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
BuildRequires:  rust
BuildRequires:  zstd
# Tests
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-maturin >= 1.2
%python_subpackages

%description
Python bindings to Rust's persistent data structures (rpds)

%prep
%autosetup -a1 -n rpds_py-%{version}

%build
export RUSTFLAGS=%{rustflags}
%pyproject_wheel

%install
export RUSTFLAGS=%{rustflags}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/rpds
%{python_sitearch}/rpds_py-%{version}.dist-info/

%changelog
