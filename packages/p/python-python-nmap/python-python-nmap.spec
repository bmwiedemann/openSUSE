#
# spec file for package python-python-nmap
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
Name:           python-python-nmap
Version:        0.6.1
Release:        0
Summary:        Python class for using nmap from Python 3
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            http://xael.org/pages/python-nmap-en.html
Source:         https://files.pythonhosted.org/packages/source/p/python-nmap/python-nmap-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       nmap

%python_subpackages

%description
This is a Python class for using nmap and accessing scan results from Python 3.

%prep
%setup -q -n python-nmap-%{version}
sed -i "1,4{/\/usr\/bin\/env/d}" nmap/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No check section since the tests use hardcoded non-local ip numbers.

%files %{python_files}
%doc CHANGELOG README.txt
%{python_sitelib}/*

%changelog
