#
# spec file for package python-edk2toollib
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


%define skip_python2 1
%{?sle15_python_module_pythons}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-edk2toollib
Version:        0.21.9
Release:        0
Summary:        Tianocore Edk2 PyTool Library
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/edk2-pytool-library
Source:         edk2-pytool-library-%{version}.tar.gz
Source1:        readme.md
Source2:        license.txt
Group:          Development/Tools/Other
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py >= 1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This is a Tianocore maintained project consisting of a python library supporting UEFI firmware development. This package's intent is to provide an easy way to organize and share python code to facilitate reuse across environments, tools, and scripts.

%prep
%setup -q -n edk2-pytool-library-%{version}
%autopatch -p1
cp %{SOURCE1} readme.md
cp %{SOURCE2} license.txt

%build
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post

%postun

%files %{python_files}
%license license.txt
%doc readme.md
%{python_sitelib}/*

%changelog
