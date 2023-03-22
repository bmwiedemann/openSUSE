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


Name:           python-y-py
Version:        0.5.5
Release:        0
Summary:        Python bindings for the Y-CRDT built from yrs (Rust)
License:        MIT
URL:            https://github.com/y-crdt/ypy
# Update through `osc service runall`
Source:         ypy-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module maturin}
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
%doc README.md
%license LICENSE
%{python_sitearch}/y_py
%{python_sitearch}/y_py-%{version}.dist-info

%changelog
