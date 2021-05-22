#
# spec file for package python-maturin
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-maturin
Version:        0.10.6
Release:        0
Summary:        Rust/Python Interoperability
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
Source:         https://files.pythonhosted.org/packages/source/m/maturin/maturin-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust-packaging
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

This project is a zero-configuration replacement for
setuptools-rust milksnake. It supports building wheels for Python
3.5+, can upload them to PyPI and has basic PyPy support.

%prep
%setup -q -n maturin-%{version}
tar -xf %{SOURCE1}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/maturin

%post
%python_install_alternative maturin

%postun
%python_uninstall_alternative maturin

%files %{python_files}
%license license-apache license-mit
%doc Changelog.md Readme.md
%python_alternative %{_bindir}/maturin
%{python_sitelib}/*

%changelog
