#
# spec file for package python-python-jose
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
Name:           python-python-jose
Version:        3.0.1
Release:        0
Summary:        JOSE implementation in Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/mpdavis/python-jose
Source:         https://github.com/mpdavis/python-jose/archive/%{version}.tar.gz#/python-jose-%{version}.tar.gz
Patch0:         unpin-deps.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ecdsa
Requires:       python-rsa
Requires:       python-six
Recommends:     python-cryptography
Recommends:     python-pycryptodome >= 3.3.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module pycryptodome >= 3.3.1}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A JavaScript Object Signing and Encryption (JOSE) technologies
implementation in Python.

%prep
%setup -q -n python-jose-%{version}
%patch0 -p1
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
