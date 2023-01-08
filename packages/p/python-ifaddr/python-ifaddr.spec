#
# spec file for package python-ifaddr
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without python2
Name:           python-ifaddr
Version:        0.2.0
Release:        0
Summary:        Module for enumerating IP addresses on system network adapters
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pydron/ifaddr
Source:         https://files.pythonhosted.org/packages/source/i/ifaddr/ifaddr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-ipaddress
%endif
# /SECTION
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
ifaddr is a Python library that allows finding the
IP addresses assigned to the system.

%prep
%setup -q -n ifaddr-%{version}
sed -i -e "s/install_requires = \['ipaddress'\],//" setup.py
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest ifaddr

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/ifaddr
%{python_sitelib}/ifaddr-%{version}*-info

%changelog
