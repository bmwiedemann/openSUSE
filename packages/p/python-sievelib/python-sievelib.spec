#
# spec file for package python-sievelib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Aeneas Jaissle <aj@ajaissle.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define modname sievelib
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.1.1
Release:        0
Summary:        Client-side Sieve and Managesieve library written in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/sievelib
Source:         https://files.pythonhosted.org/packages/source/s/sievelib/%{modname}-%{version}.tar.gz
Patch0:         fix_pip_version.patch
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Client-side Sieve and Managesieve library written in Python.
* Sieve: An Email Filtering Language (RFC 5228)
* ManageSieve: A Protocol for Remotely Managing Sieve Scripts (RFC 5804)

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1 
sed -i -e '/^#!\/usr\/bin.*python/d' sievelib/parser.py
chmod -x sievelib/parser.py

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/*

%changelog
