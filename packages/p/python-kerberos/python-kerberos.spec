#
# spec file for package python-kerberos
#
# Copyright (c) 2019 SUSE LLC.
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
%bcond_without test
Name:           python-kerberos
Version:        1.3.0
Release:        0
Summary:        Kerberos high-level interface
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/apple/ccs-pykerberos
Source:         https://files.pythonhosted.org/packages/source/k/kerberos/kerberos-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/apple/ccs-pykerberos/master/LICENSE.txt
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(krb5)
%python_subpackages

%description
A high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps
the entire Kerberos.framework, and instead offer a limited set of
functions that do what is needed for client/server Kerberos
authentication based on <http://www.ietf.org/rfc/rfc4559.txt>.

%prep
%setup -q -n kerberos-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.rst
%{python_sitearch}/*
%license LICENSE.txt

%changelog
