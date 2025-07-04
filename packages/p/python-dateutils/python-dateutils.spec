#
# spec file for package python-dateutils
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
Name:           python-dateutils
Version:        0.6.12
Release:        0
Summary:        Python library for working with date and datetime objects
License:        0BSD
Group:          Development/Languages/Python
URL:            https://github.com/jmcantrell/python-dateutils
Source:         https://files.pythonhosted.org/packages/source/d/dateutils/dateutils-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
Python library for working with date and datetime objects.

%prep
%setup -q -n dateutils-%{version}
sed -i '/argparse/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
# Avoid conflicts with dateutils; these scripts lack many features of the other package
rm %{buildroot}%{_bindir}/dateadd %{buildroot}%{_bindir}/datediff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.mkd
%license LICENSE
%{python_sitelib}/dateutils
%{python_sitelib}/dateutils-%{version}*-info

%changelog
