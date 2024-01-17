#
# spec file for package python-crayons
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname crayons
Name:           python-crayons
Version:        0.4.0
Release:        0
Summary:        Colored strings for terminal usage
License:        MIT
URL:            https://github.com/MasterOdin/crayons
Source:         https://github.com/MasterOdin/%{modname}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-colorama
BuildArch:      noarch
%python_subpackages

%description
Crayons is a simple module to give you colored strings for terminal usage.
Included colors are red, green, yellow, blue, black, magenta, cyan, white,
and normal.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec test_crayons.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{modname}.py
%{python_sitelib}/%{modname}-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/%{modname}*

%changelog
