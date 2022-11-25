#
# spec file for package python-maturin
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-maturin
Version:        0.14.2
Release:        0
Summary:        Rust/Python Interoperability
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
Source:         https://files.pythonhosted.org/packages/source/m/maturin/maturin-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-rust >= 1.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli >= 1.1.0 if %python-base < 3.11}
BuildRequires:  %{python_module wheel >= 0.36.2}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%python_subpackages

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

This project is a zero-configuration replacement for
setuptools-rust milksnake. It supports building wheels for Python
3.6+, can upload them to PyPI and has basic PyPy support.

%prep
%autosetup -a1 -n maturin-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config
sed -i '1{/env python/d}' maturin/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/maturin

%post
%python_install_alternative maturin

%postun
%python_uninstall_alternative maturin

%files %{python_files}
%license license-apache license-mit
%doc Changelog.md README.md
%python_alternative %{_bindir}/maturin
%{python_sitearch}/maturin
%{python_sitearch}/maturin-%{version}*-info

%changelog
