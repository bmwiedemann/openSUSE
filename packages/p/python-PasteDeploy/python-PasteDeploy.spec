#
# spec file for package python-PasteDeploy
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
Name:           python-PasteDeploy
Version:        3.1.0
Release:        0
Summary:        Tool to load, configure, and compose WSGI applications and servers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/pastedeploy
Source:         https://files.pythonhosted.org/packages/source/p/PasteDeploy/PasteDeploy-%{version}.tar.gz
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Paste
Requires:       python-setuptools
Provides:       python-pastedeploy = %{version}
Obsoletes:      python-pastedeploy < %{version}
BuildArch:      noarch
%python_subpackages

%description
This tool provides code to load WSGI applications and servers from URIs; these
URIs can refer to Python Eggs for INI-style configuration files. Paste Script
provides commands to serve applications based on this configuration file.

%prep
%autosetup -p1 -n PasteDeploy-%{version}

sed -i -e '/^addopts/s/ --cov//' pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license license.txt
%{python_sitelib}/[pP]aste[dD]eploy-%{version}.dist-info
%{python_sitelib}/PasteDeploy-%{version}*-nspkg.pth
%{python_sitelib}/paste/deploy

%changelog
