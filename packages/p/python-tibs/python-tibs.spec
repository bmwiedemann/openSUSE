#
# spec file for package python-tibs
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


Name:           python-tibs
Version:        2.0.2
Release:        0
Summary:        A sleek Python library for binary data
License:        MIT
URL:            https://github.com/scott-griffiths/tibs
Source0:        https://files.pythonhosted.org/packages/source/t/tibs/tibs-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.11.5}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 6.151.0}
BuildRequires:  %{python_module gfloat >= 0.5}
BuildRequires:  %{python_module ml-dtypes >= 0.5.4}
BuildRequires:  %{python_module pytest >= 9.0.0}
BuildRequires:  %{python_module pytest-benchmark >= 5.2.0}
# /SECTION
Suggests:       python-bitarray
Suggests:       python-gfloat >= 0.5
Suggests:       python-ml-dtypes >= 0.5.4
%python_subpackages

%description
tibs is a Python library for binary data.
It's 100% written in Rust and has excellent performance.

Use it for packets, registers, instruction
formats, bitsets, compressed data and streams where fields can have many different
interpretations and be any number of bits long.

It is used to power the popular [bitstring](https://github.com/scott-griffiths/bitstring)
library, which is by the same author. The full documentation is available on [Read the Docs](https://tibs.readthedocs.io/en/latest/).

%prep
%autosetup -p1 -n tibs-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/tibs
%{python_sitearch}/tibs-%{version}.dist-info

%changelog
