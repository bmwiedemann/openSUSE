#
# spec file for package python-pycrdt
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


Name:           python-pycrdt
Version:        0.8.17
Release:        0
Summary:        Python bindings for Yrs
License:        MIT
URL:            https://github.com/jupyter-server/pycrdt
Source0:        pycrdt-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.4.0}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.4.2}
#BuildRequires: %%{python_module pydantic >= 2.5.2 with %%python-pydantic < 3}
BuildRequires:  %{python_module y-py >= 0.7.0~a1}
BuildRequires:  %{python_module objsize}
# /SECTION
%python_subpackages

%description
Pycrdt is a Python CRDT library that provides bindings for Yrs, the Rust port of the Yjs framework.

Conflict-free Replicated Data Types (CRDTs) allow creating shared documents that can automatically
merge changes made concurrently on different "copies" of the data. When the data lives on different
machines, they make it possible to build distributed systems that work with local data, leaving the
synchronization and conflict resolution with remote data to the CRDT algorithm, which ensures that
all data replicas eventually converge to the same state.

%prep
%autosetup -p1 -n pycrdt-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# pydantic is too old
%pytest_arch --ignore tests/test_model.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/pycrdt
%{python_sitearch}/pycrdt-%{version}.dist-info

%changelog
