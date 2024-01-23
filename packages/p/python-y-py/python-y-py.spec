#
# spec file for package python-y-py
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


%define pyversion 0.7.0a1
Name:           python-y-py
# Update through editing _service and running `osc service runall`
Version:        0.7.0~a1
Release:        0
Summary:        Python bindings for the Y-CRDT built from yrs (Rust)
License:        MIT
URL:            https://github.com/y-crdt/ypy
Source:         ypy-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module maturin >= 1.2.3 with %python-maturin < 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-y_py = %{version}-%{release}
%python_subpackages

%description
Python binding for Y-CRDT. It provides distributed data types that enable
real-time collaboration between devices. Ypy can sync data with any other
platform that has a Y-CRDT binding, allowing for seamless cross-domain
communication. The library is a thin wrapper around Yrs, taking advantage of
the safety and performance of Rust.

Project is still experimental. Expect the API to change before a version 1.0
stable release.

%prep
%setup -q -n ypy-%{version} -a1

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
%{python_sitearch}/y_py
%{python_sitearch}/y_py-%{pyversion}.dist-info

%changelog
