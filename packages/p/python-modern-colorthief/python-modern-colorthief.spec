#
# spec file for package python-modern-colorthief
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
%define         pyname modern_colorthief
Name:           python-modern-colorthief
Version:        0.1.8
Release:        0
Summary:        Colorthief reimagined
License:        MIT
URL:            https://github.com/baseplate-admin/modern_colorthief
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
%python_subpackages

%description
Python-modern-colorthief is a rewritten rust python-colorthief replacement

%prep
%autosetup -a1 -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%check
# the singular test is relying on the old abandoned python-colorthief.

%files %{python_files}
%license LICENSE
%{python_sitearch}/%{pyname}
%pycache_only %{python_sitearch}/%{pyname}/__pycache__
%{python_sitearch}/%{pyname}-%{version}.dist-info

%changelog
