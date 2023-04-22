#
# spec file for package python-gssapi
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-gssapi
Version:        1.8.2
Release:        0
Summary:        A Python interface to RFC 2743/2744 (plus common extensions)
License:        ISC
URL:            https://pythongssapi.github.io/python-gssapi/stable/
Source:         https://files.pythonhosted.org/packages/source/g/gssapi/gssapi-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module k5test}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  krb5-devel
BuildRequires:  python-rpm-macros
Requires:       python-decorator
%python_subpackages

%description
Python-GSSAPI provides both low-level and high level wrappers around the GSSAPI
C libraries. While it focuses on the Kerberos mechanism, it should also be
usable with other GSSAPI mechanisms.

%prep
%setup -q -n gssapi-%{version}
sed -i "s/'gssapi.tests'//" setup.py

mv gssapi/tests .

%build
export CFLAGS="%{optflags} -DHAS_GSSAPI_EXT_H -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv gssapi gssapi_temp
%pytest_arch tests
mv gssapi_temp gssapi

%files %{python_files}
%{python_sitearch}/gssapi*
%doc README.rst
%license LICENSE.txt

%changelog
