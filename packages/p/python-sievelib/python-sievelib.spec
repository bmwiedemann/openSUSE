#
# spec file for package python-sievelib
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define modname sievelib
Name:           python-%{modname}
Version:        1.4.2
Release:        0
Summary:        Client-side Sieve and Managesieve library written in Python
License:        MIT
URL:            https://github.com/tonioo/sievelib
Source:         https://files.pythonhosted.org/packages/source/s/sievelib/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-typing-extensions
%python_subpackages

%description
Client-side Sieve and Managesieve library written in Python.
* Sieve: An Email Filtering Language (RFC 5228)
* ManageSieve: A Protocol for Remotely Managing Sieve Scripts (RFC 5804)

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '/^#!\/usr\/bin.*python/d' sievelib/parser.py
chmod -x sievelib/parser.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/sievelib
%{python_sitelib}/sievelib-%{version}.dist-info

%changelog
