#
# spec file for package python-tablib
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
%if 0%{?rhel}
# I get syntax errors in the brp-python-bytecompile step...
%define _python_bytecompile_errors_terminate_build 0
%endif
Name:           python-tablib
Version:        0.13.0
Release:        0
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)
License:        MIT
Group:          Development/Languages/Python
URL:            http://python-tablib.org
Source:         https://files.pythonhosted.org/packages/source/t/tablib/tablib-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module odfpy >= 1.3.5}
BuildRequires:  %{python_module openpyxl >= 2.4.8}
BuildRequires:  %{python_module pandas >= 0.20.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xlrd >= 1.1.0}
BuildRequires:  %{python_module xlwt >= 1.3.0}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-backports.csv
Requires:       python-PyYAML >= 3.12
Requires:       python-odfpy >= 1.3.5
Requires:       python-openpyxl >= 2.4.8
Requires:       python-xlrd >= 1.1.0
Requires:       python-xlwt >= 1.3.0
Requires:       python-xml
Suggests:       python-pandas >= 0.20.3
BuildArch:      noarch
%ifpython2
Requires:       python2-backports.csv
%endif
%python_subpackages

%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

- Excel (Sets + Books)
- JSON (Sets + Books)
- YAML (Sets + Books)
- HTML (Sets)
- TSV (Sets)
- CSV (Sets)

%prep
%setup -q -n tablib-%{version}
# Remove shebang lines from non-executable scripts:
find tablib -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%python_build

%install
%python_install
# Remove dependency on backports.csv from egg-info, as it isnt
# installed on Python 3, breaking pkg_resources resolver.
sed -i '/backports.csv/d' %{buildroot}%{python3_sitelib}/tablib*egg-info/requires.txt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_tablib.py

%files %{python_files}
%license LICENSE
%doc README.rst HISTORY.rst
%{python_sitelib}/*

%changelog
