#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Dr. Axel Braun
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
%define modname pytzdata
Name:           python-%{modname}
Version:        2020.1
Release:        0
Summary:        The pytzdata module for Python-pendulum
License:        MIT
URL:            https://github.com/sdispater/pytzdata
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       timezone
%python_subpackages

%description
The Olson timezone database for Python. This version is linked to the systemwide zone info

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
# delete internal database
%{python_expand rm -r %{buildroot}%{$python_sitelib}/pytzdata/zoneinfo
ln -s /usr/share/zoneinfo %{buildroot}%{$python_sitelib}/pytzdata/zoneinfo
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
