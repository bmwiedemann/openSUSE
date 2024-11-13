#
# spec file for package python-python-nmap
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


Name:           python-python-nmap
Version:        0.7.1
Release:        0
Summary:        Python class for using nmap from Python
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://xael.org/pages/python-nmap-en.html
Source:         https://files.pythonhosted.org/packages/source/p/python-nmap/python-nmap-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# python-python-nmap depends on an installed nmap binary
# which lives in non-oss so we cannot not add it a hard dependeny.
# see: https://build.opensuse.org/request/show/1206265
# In case nmap is not found it raises the following error:
# "ScannerError: 'nmap program was not found in path."
# Users should then know how to handle this.
Recommends:     nmap
BuildArch:      noarch
%python_subpackages

%description
This is a Python class for using nmap and accessing scan results from Python.

%prep
%setup -q -n python-nmap-%{version}
sed -i "1,4{/\/usr\/bin\/env/d}" nmap/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No check section since the tests use hardcoded non-local ip numbers.

%files %{python_files}
%doc CHANGELOG README.rst
%{python_sitelib}/nmap
%{python_sitelib}/python_nmap-%{version}.dist-info

%changelog
