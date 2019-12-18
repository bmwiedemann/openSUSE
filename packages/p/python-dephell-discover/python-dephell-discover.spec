#
# spec file for package python-dephell-discover
#
# Copyright (c) 2019 SUSE LLC
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
%define skip_python2 1
Name:           python-dephell-discover
Version:        0.2.10
Release:        0
Summary:        Module to find project modules and data files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dephell/dephell_discover
Source:         https://files.pythonhosted.org/packages/source/d/dephell_discover/dephell_discover-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attr
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attr}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This Python module finds project modules and data files (packages and package_data for setup.py).

%prep
%setup -q -n dephell_discover-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
