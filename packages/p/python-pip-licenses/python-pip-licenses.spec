#
# spec file for package python-pip-licenses
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
Name:           python-pip-licenses
Version:        1.18.0
Release:        0
Summary:        Python packages license list
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/raimon49/pip-licenses
Source:         https://files.pythonhosted.org/packages/source/p/pip-licenses/pip-licenses-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Dump the software license list of Python packages installed with pip.

%prep
%setup -q -n pip-licenses-%{version}
# PTable is an incompatible PrettyTable fork, and pip-licenses supports
# either https://github.com/raimon49/pip-licenses/pull/52
sed -i 's/PTable/PrettyTable/' setup.py

sed -i '/addopts/d' setup.cfg
sed -i '/pytest-/d' setup.py
sed -i '1{/^#!/d}' piplicenses.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/pip-licenses -s

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/pip-licenses
%{python_sitelib}/*

%changelog
