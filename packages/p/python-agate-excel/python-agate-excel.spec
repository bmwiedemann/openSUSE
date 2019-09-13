#
# spec file for package python-agate-excel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-agate-excel
Version:        0.2.3
Release:        0
Summary:        Read support for Excel files (xls and xlsx) for agate
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/agate-excel
Source:         https://github.com/wireservice/agate-excel/archive/%{version}.tar.gz
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module openpyxl >= 2.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xlrd >= 0.9.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-agate >= 1.5.0
Requires:       python-openpyxl >= 2.3.0
Requires:       python-xlrd >= 0.9.4
BuildArch:      noarch
%python_subpackages

%description
Agate-excel adds read support for Excel files (xls and xlsx)
to agate.

%prep
%setup -q -n agate-excel-%{version}

sed -i -e '/^#!\//, 1d' agateexcel/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst
%license COPYING
%{python_sitelib}/*

%changelog
