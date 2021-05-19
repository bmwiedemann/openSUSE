#
# spec file for package python-cramjam
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python36 1
Name:           python-cramjam
Version:        2.3.1
Release:        0
Summary:        Thin Python bindings to de/compression algorithms in Rust
License:        MIT
URL:            https://github.com/milesgranger/pyrus-cramjam
# use `rm -rf pyrus-cramjam; osc service runall` in order to update
Source:         pyrus-cramjam-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module maturin}
BuildRequires:  rust-packaging
# SECTION test dependencies
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
Extremely thin Python bindings to de/compression algorithms in Rust.
Allows for using algorithms such as Snappy, without any system dependencies.

%prep
%setup -q -n pyrus-cramjam-%{version} -a1
cp %{SOURCE2} .cargo/config

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --ignore benchmarks

%files %{python_files}
%license LICENSE
%{python_sitearch}/cramjam*.so
%{python_sitearch}/cramjam-%{version}*-info

%changelog