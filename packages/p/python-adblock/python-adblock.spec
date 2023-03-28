#
# spec file for package python-adblock
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python36 1
Name:           python-adblock
Version:        0.6.0
Release:        0
Summary:        Brave's adblock library in Python
License:        Apache-2.0 OR MIT
URL:            https://pypi.org/project/adblock/
Source:         https://github.com/ArniDagur/python-adblock/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
# PATCH-FIX-OPENSUSE allow building with newer maturin, which is pedantic about PEP 621
Patch0:         python-adblock-maturin-0-14-compat.patch
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
ExclusiveArch:  %{rust_arches}
%python_subpackages

%description
Python wrapper for Brave's adblocking library.

%prep
%autosetup -a1 -p1
# build flavor-specific versions -- otherwise wheels will not work
sed -i 's/"abi3-py37", //' Cargo.toml
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{python_sitearch}/*

%changelog
